import smbus
import time

# ADXL345 Address
adxl345_address = 0x53
# HMC5883L Address
hmc5883l_address = 0x1E

# Create an I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, which is the default I2C bus on Raspberry Pi

# ADXL345 Configuration
bus.write_byte_data(adxl345_address, 0x2D, 8)  # Enable measurement mode

# HMC5883L Configuration
bus.write_byte_data(hmc5883l_address, 0x02, 0)  # Continuous measurement mode

try:
    while True:
        # Add a delay for the sensors to stabilize
        time.sleep(0.1)

        # Read ADXL345 data
        adxl_x_l = bus.read_byte_data(adxl345_address, 0x32)
        adxl_x_h = bus.read_byte_data(adxl345_address, 0x33)
        adxl_y_l = bus.read_byte_data(adxl345_address, 0x34)
        adxl_y_h = bus.read_byte_data(adxl345_address, 0x35)
        adxl_z_l = bus.read_byte_data(adxl345_address, 0x36)
        adxl_z_h = bus.read_byte_data(adxl345_address, 0x37)
        adxl_x = (adxl_x_h << 8 | adxl_x_l) if adxl_x_h < 0x80 else (adxl_x_h << 8 | adxl_x_l - 0x10000)
        adxl_y = (adxl_y_h << 8 | adxl_y_l) if adxl_y_h < 0x80 else (adxl_y_h << 8 | adxl_y_l - 0x10000)
        adxl_z = (adxl_z_h << 8 | adxl_z_l) if adxl_z_h < 0x80 else (adxl_z_h << 8 | adxl_z_l - 0x10000)

        # Read HMC5883L data
        hmc_x = bus.read_word_data(hmc5883l_address, 0x03)
        hmc_y = bus.read_word_data(hmc5883l_address, 0x05)
        hmc_z = bus.read_word_data(hmc5883l_address, 0x07)
        hmc_x = hmc_x if hmc_x < 0x8000 else hmc_x - 0x10000
        hmc_y = hmc_y if hmc_y < 0x8000 else hmc_y - 0x10000
        hmc_z = hmc_z if hmc_z < 0x8000 else hmc_z - 0x10000

        print(f"ADXL345: X={adxl_x}, Y={adxl_y}, Z={adxl_z} | HMC5883L: X={hmc_x}, Y={hmc_y}, Z={hmc_z}")
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    bus.close()
