import time
import os
import sys
import RPi.GPIO as GPIO
import smbus

class Light_sensor():

    # class attributes
    FREQUENCY        = 20
    subID            = None  # id of the object instance

    def __init__(self,subID,FREQUENCY=20, *args, **kwargs):

        ''' Initialize object '''
        self.subID = subID

    def get_luminosity(self):
        
        bus = smbus.SMBus(1)
        #TSL2561 address, 0x39(57)

        bus.write_byte_data(self.subID, 0x00 | 0x80, 0x03)   
        bus.write_byte_data(self.subID, 0x01 | 0x80, 0x02)
        time.sleep(0.5)
            
        data = bus.read_i2c_block_data(self.subID, 0x0C | 0x80, 2)
            
        data1 = bus.read_i2c_block_data(self.subID, 0x0E | 0x80, 2)
          
        ch0 = data[1] * 256 + data[0]
        ch1 = data1[1] * 256 + data1[0]

        #print("Full Spectrum(IR + Visible) :%d lux" %ch0)
        #print("Infrared Value :%d lux" %ch1)
        #print("Visible Value :%d lux" %(ch0 - ch1))
        return ch0

def main():
    t = Light_sensor(0x39)
    print(t.get_luminosity())


# Execution or import
if __name__ == "__main__":
    # Start executing
    main()
