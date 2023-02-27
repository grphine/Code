
#define VBATPIN A7
   


void setup() {
  // put your setup code here, to run once:
  

}

void loop() {
  // put your main code here, to run repeatedly:
  
float measuredvbat = analogRead(VBATPIN);
measuredvbat = (measuredvbat*6.6)/1024;
Serial.print("VBat: " ); Serial.println(measuredvbat);

}
