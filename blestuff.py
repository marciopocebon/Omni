from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import unicodedata

ble = BLERadio()

uart_connection = None

while True:
    if not uart_connection:
        print("Trying to connect...")
        for adv in ble.start_scan(ProvideServicesAdvertisement):
            if UARTService in adv.services:
                uart_connection = ble.connect(adv)
                print("Connected")
                break
        ble.stop_scan()

    if uart_connection and uart_connection.connected:
        uart_service = uart_connection[UARTService]
        while uart_connection.connected:
#             s = input("Eval: ")
#             uart_service.write(s.encode("utf-8"))
#             uart_service.write(b'\n')
            raw = uart_service.readline().decode("utf-8")
            raw = raw.replace('\r\n', '')
            raw = raw.replace('t', '')
            
            if raw == '':
                pass
            else:
                sensor_value = int(raw)
                print(sensor_value)