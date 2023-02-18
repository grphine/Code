
#include <SPI.h>
#include <RH_RF95.h>
#include <Adafruit_GPS.h>

#define RFM95_CS      8
#define RFM95_INT     3
#define RFM95_RST     4

#define VBATPIN A7

#define GPSSerial Serial1
Adafruit_GPS GPS(&GPSSerial);

#define RF95_FREQ 868.0

RH_RF95 rf95(RFM95_CS, RFM95_INT);

uint32_t timer = millis();
int count = 0;
int length = 0;

void setup() {
  // make this baud rate fast enough to we aren't waiting on it
  Serial.begin(115200);
  
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  // wait for hardware serial to appear
  // while (!Serial) delay(10);

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    Serial.println("Uncomment '#define SERIAL_DEBUG' in RH_RF95.cpp for detailed debug info");
    while (1);
  }

  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }

  rf95.setTxPower(23, false);

  // 9600 baud is the default rate for the Ultimate GPS
  GPS.begin(9600);

  
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);

  
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_200_MILLIHERTZ);  // 5 second update time

  


}

void loop() {
  float measuredvbat = analogRead(VBATPIN);
  measuredvbat = (measuredvbat*6.6)/1024;
  char c = GPS.read();

  if (GPS.newNMEAreceived()) {
    // Serial.print(GPS.lastNMEA());
    if (!GPS.parse(GPS.lastNMEA())) {
      return;
    }
  }

  if (millis() - timer > 5000) {
    timer = millis(); 

    if (GPS.fix) {
      count++;      
    }
    String output = String(count) + "," + String(GPS.latitude,4) + "," + String(GPS.longitude,4) + "," + String(GPS.altitude) + "," + String(GPS.fixquality) + "," + String(measuredvbat, 4);
    length = output.length();
    char send[length];
    output.toCharArray(send, length);
    Serial.println(send);
      rf95.send((uint8_t *)send, length);
    
  }


}