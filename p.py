"""import smbus
import time
import matplotlib.pyplot as plt

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

# Initialize data lists
timestamps = []
adxl_data = {'X': [], 'Y': [], 'Z': []}
hmc_data = {'X': [], 'Y': [], 'Z': []}

try:
    plt.ion()  # Turn on interactive mode for real-time plotting

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

        timestamp = time.time()
        timestamps.append(timestamp)

        adxl_data['X'].append(adxl_x)
        adxl_data['Y'].append(adxl_y)
        adxl_data['Z'].append(adxl_z)

        hmc_data['X'].append(hmc_x)
        hmc_data['Y'].append(hmc_y)
        hmc_data['Z'].append(hmc_z)

        print(f"ADXL345: X={adxl_x}, Y={adxl_y}, Z={adxl_z} | HMC5883L: X={hmc_x}, Y={hmc_y}, Z={hmc_z}")

        # Plotting accelerometer data
        plt.figure(1)
        plt.subplot(211)
        plt.plot(timestamps, adxl_data['X'], label='X-axis')
        plt.plot(timestamps, adxl_data['Y'], label='Y-axis')
        plt.plot(timestamps, adxl_data['Z'], label='Z-axis')
        plt.title('ADXL345 Accelerometer Data')
        plt.xlabel('Timestamp')
        plt.ylabel('Acceleration')
        plt.legend()

        # Plotting magnetometer data
        plt.subplot(212)
        plt.plot(timestamps, hmc_data['X'], label='X-axis')
        plt.plot(timestamps, hmc_data['Y'], label='Y-axis')
        plt.plot(timestamps, hmc_data['Z'], label='Z-axis')
        plt.title('HMC5883L Magnetometer Data')
        plt.xlabel('Timestamp')
        plt.ylabel('Magnetic Field')
        plt.legend()

        plt.pause(0.1)

except KeyboardInterrupt:
    pass
finally:
    bus.close()
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Display the final plots when the program ends
"""




























import smbus
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


adxl345_address = 0x53

hmc5883l_address = 0x1E


bus = smbus.SMBus(1) 


bus.write_byte_data(adxl345_address, 0x2D, 8)  

bus.write_byte_data(hmc5883l_address, 0x02, 0)  

adxl_data = {'X': [], 'Y': [], 'Z': []}
hmc_data = {'X': [], 'Y': [], 'Z': []}


fig_adxl = plt.figure()
ax_adxl = fig_adxl.add_subplot(111, projection='3d')


fig_hmc = plt.figure()
ax_hmc = fig_hmc.add_subplot(111, projection='3d')

try:
    plt.ion()  

    while True:
  
        time.sleep(0.1)

        adxl_x_l = bus.read_byte_data(adxl345_address, 0x32)
        adxl_x_h = bus.read_byte_data(adxl345_address, 0x33)
        adxl_y_l = bus.read_byte_data(adxl345_address, 0x34)
        adxl_y_h = bus.read_byte_data(adxl345_address, 0x35)
        adxl_z_l = bus.read_byte_data(adxl345_address, 0x36)
        adxl_z_h = bus.read_byte_data(adxl345_address, 0x37)
        adxl_x = (adxl_x_h << 8 | adxl_x_l) if adxl_x_h < 0x80 else (adxl_x_h << 8 | adxl_x_l - 0x10000)
        adxl_y = (adxl_y_h << 8 | adxl_y_l) if adxl_y_h < 0x80 else (adxl_y_h << 8 | adxl_y_l - 0x10000)
        adxl_z = (adxl_z_h << 8 | adxl_z_l) if adxl_z_h < 0x80 else (adxl_z_h << 8 | adxl_z_l - 0x10000)

      
        hmc_x = bus.read_word_data(hmc5883l_address, 0x03)
        hmc_y = bus.read_word_data(hmc5883l_address, 0x05)
        hmc_z = bus.read_word_data(hmc5883l_address, 0x07)
        hmc_x = hmc_x if hmc_x < 0x8000 else hmc_x - 0x10000
        hmc_y = hmc_y if hmc_y < 0x8000 else hmc_y - 0x10000
        hmc_z = hmc_z if hmc_z < 0x8000 else hmc_z - 0x10000

        adxl_data['X'].append(adxl_x)
        adxl_data['Y'].append(adxl_y)
        adxl_data['Z'].append(adxl_z)

        hmc_data['X'].append(hmc_x)
        hmc_data['Y'].append(hmc_y)
        hmc_data['Z'].append(hmc_z)

        print(f"ADXL345: X={adxl_x}, Y={adxl_y}, Z={adxl_z} | HMC5883L: X={hmc_x}, Y={hmc_y}, Z={hmc_z}")

       
        ax_adxl.cla()
        ax_adxl.scatter(adxl_data['X'], adxl_data['Y'], adxl_data['Z'], label='ADXL345')
        ax_adxl.set_title('ADXL345 Accelerometer Data (3D)')
        ax_adxl.set_xlabel('X-axis')
        ax_adxl.set_ylabel('Y-axis')
        ax_adxl.set_zlabel('Z-axis')
        ax_adxl.legend()

       
        ax_hmc.cla()
        ax_hmc.scatter(hmc_data['X'], hmc_data['Y'], hmc_data['Z'], label='HMC5883L')
        ax_hmc.set_title('HMC5883L Magnetometer Data (3D)')
        ax_hmc.set_xlabel('X-axis')
        ax_hmc.set_ylabel('Y-axis')
        ax_hmc.set_zlabel('Z-axis')
        ax_hmc.legend()

        plt.pause(0.1)

except KeyboardInterrupt:
    pass
finally:
    bus.close()
    plt.ioff() 
    plt.show() 







