#include <Wire.h>
#include <Adafruit_BMP085.h>
#define seaLevelPressure_hPa 1013.25

Adafruit_BMP085 bmp;

unsigned long getTemper_lastExecutionTime = 0;
int getTemper_interval = 1000;

void setup() {
  Serial.begin(115200);
  if (!bmp.begin()) {
  Serial.println("BMP180 Not Found. CHECK CIRCUIT!");
  while (1) {}
  }
}

int getTemperature(){
  int BMPTemperature = bmp.readTemperature();
  Serial.print("Temperature = ");
  Serial.print(BMPTemperature);
  Serial.println(" *C");
  return BMPTemperature;
}
  
void loop() {
  unsigned long currentTime = millis();
  if(currentTime - getTemper_lastExecutionTime > getTemper_interval){
    getTemper_lastExecutionTime = currentTime;
    getTemperature();
  } // 2초에 한 번씩 실행됨.

}