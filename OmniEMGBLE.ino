#include <bluefruit.h>

const int emgSensor = A3;

BLEDfu bledfu;
BLEUart bleuart;

void setup() {
  Serial.begin(57600);
  delay(10);
  Serial.println();
  Serial.println("Starting...");
  delay(10);
  Bluefruit.begin();
  Bluefruit.setTxPower(4);
  Bluefruit.setName("Bluefruit52");
  bledfu.begin();
  bleuart.begin();
  startAdv();


}

void loop() {
  int sensorValue = analogRead(emgSensor);
  Serial.println(sensorValue);
  bleuart.print(sensorValue);
  bleuart.println();
  delay(1);


}

void startAdv(void)
{
  // Advertising packet
  Bluefruit.Advertising.addFlags(BLE_GAP_ADV_FLAGS_LE_ONLY_GENERAL_DISC_MODE);
  Bluefruit.Advertising.addTxPower();
  
  Bluefruit.Advertising.addService(bleuart);

  Bluefruit.ScanResponse.addName();

  Bluefruit.Advertising.restartOnDisconnect(true);
  Bluefruit.Advertising.setInterval(32, 244);    // in unit of 0.625 ms
  Bluefruit.Advertising.setFastTimeout(30);      // number of seconds in fast mode
  Bluefruit.Advertising.start(0);                // 0 = Don't stop advertising after n seconds  
}
