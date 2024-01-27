import smbus
import time

# ADXL345 Address
adxl345_address = 0x53

# Create an I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, which is the default I2C bus on Raspberry Pi

# ADXL345 Configuration
bus.write_byte_data(adxl345_address, 0x2D, 8)  # Enable measurement mode

try:
    while True:
        # Add a delay for the sensor to stabilize
        time.sleep(0.1)

        # Read ADXL345 data (8-bit signed integers for each axis)
        adxl_x_l = bus.read_byte_data(adxl345_address, 0x32)
        adxl_x_h = bus.read_byte_data(adxl345_address, 0x33)
        adxl_y_l = bus.read_byte_data(adxl345_address, 0x34)
        adxl_y_h = bus.read_byte_data(adxl345_address, 0x35)
        adxl_z_l = bus.read_byte_data(adxl345_address, 0x36)
        adxl_z_h = bus.read_byte_data(adxl345_address, 0x37)

        # Combine low and high bytes and convert to signed value
        adxl_x = (adxl_x_h << 8 | adxl_x_l) if adxl_x_h < 0x80 else (adxl_x_h << 8 | adxl_x_l - 0x10000)
        adxl_y = (adxl_y_h << 8 | adxl_y_l) if adxl_y_h < 0x80 else (adxl_y_h << 8 | adxl_y_l - 0x10000)
        adxl_z = (adxl_z_h << 8 | adxl_z_l) if adxl_z_h < 0x80 else (adxl_z_h << 8 | adxl_z_l - 0x10000)

        print(f"ADXL345: X={adxl_x}, Y={adxl_y}, Z={adxl_z}")
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    bus.close()
