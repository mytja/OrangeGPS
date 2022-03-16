# OrangeGPS
A simple library to interface GPS modules using PySerial and MicroPython/CircuitPython.

# Installation
```shell
pip install git+https://github.com/mytja/OrangeGPS
pip install pyserial
```

# Usage
```python
import serial
from orangegps import GPS

# Use /dev/ttyS1 for UART1 and /dev/ttyS2 for UART2
ser = serial.Serial("/dev/ttyS1")
gps = GPS(ser)
print(gps.get())
```
Note that GPS module MUST be facing outside or outside to be able to catch any GPS satellites.

GPS module might take up to 2 minutes (from our testing) to connect to a satellite.
Minimum number of satellites is around 7 to be able to fix the position.
