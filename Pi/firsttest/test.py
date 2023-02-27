
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x
from datetime import datetime

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 868.0)
rfm9x.tx_power = 23
prev_packet = None
file = open((datetime.now()).strftime("%d%m%y.txt"), 'w+')
print("Start")

try:
    while True:
        packet = None
        packet = rfm9x.receive()
        if packet is not None:
            prev_packet = packet
            try: 
                now = datetime.now()
                date_time = now.strftime("%y/%m/%d,%H:%M:%S")

                packet_text = str(prev_packet, "utf-8")
                text = (date_time + ", " + packet_text)
            except UnicodeDecodeError:
                print(date_time + ", " + "unicode parse error", file=file, flush=True)
            print(text, file=file, flush=True)
except KeyboardInterrupt:
    print("\nTerminating")
    file.close()
    raise SystemExit
        

