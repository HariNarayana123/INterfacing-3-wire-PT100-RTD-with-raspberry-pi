# install the Adafruit MAX31865 library to interact with the MAX31865 amplifier 
# sudo pip3 install adafruit-circuitpython-max31865 // run this command on rspi



import board
import time
import busio
import adafruit_max31865

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.CE0)
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)

while True:
  try:  
    temperature = sensor.temperature
    print(f"Temperature: {tempeparture}{chr(248)}C")
    time.sleep(0.2)
  except KeyboardInterrupt:
      print("user interrupted the programme")
      sys.exit()
  finally:
      GPIO.cleanup()
      spi.close()  
        
