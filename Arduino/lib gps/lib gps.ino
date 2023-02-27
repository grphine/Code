
#include <SPI.h>
#include <RH_RF95.h>
#include <Adafruit_GPS.h>

#define GPSSerial Serial1
Adafruit_GPS GPS(&GPSSerial);

#define GPSECHO false

uint32_t timer = millis();

void setup() {
  while (!Serial)
    ;
  Serial.begin(115200);
  GPS.begin(9600);
  // GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_ALLDATA);
  // GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_200_MILLIHERTZ);  // 10 second update time
  // GPS.sendCommand(PGCMD_ANTENNA);
}

void loop() {
  char c = GPS.read();
  // if (GPSECHO) {
  //   if (c) {
  //     Serial.print(c);
  //   }
  // }

  if (GPS.newNMEAreceived()) {
    // Serial.print(GPS.lastNMEA());
    if (!GPS.parse(GPS.lastNMEA())) {
      return;
    }
  }
  if (millis() - timer > 2000) {
    timer = millis(); 

    if (GPS.fix) {
      Serial.print(GPS.latitude,4);
      Serial.print(GPS.lat);
      Serial.print(", ");
      Serial.print(GPS.longitude,4);
      Serial.println(GPS.lon);
    }
  }
}