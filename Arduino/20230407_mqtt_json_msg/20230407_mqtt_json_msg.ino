#include <ArduinoJson.h>
StaticJsonDocument<256> doc;




void setup(){
  doc["sensor"] = "gps";
  doc["time"] = 1351824120;
  Serial.begin(19200);
  
}

void loop(){
  serializeJson(doc, Serial);
  Serial.println();
  delay(1000);
}