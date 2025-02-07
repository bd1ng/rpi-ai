import smbus

# I2C setup
I2C_BUS = 1  # Use I2C bus 1
DEVICE_ADDRESS = 0x27  # Default I2C address for ADS7830
bus = smbus.SMBus(I2C_BUS)

def read_adc(channel):
    """
    Reads the analog value from the specified channel (0-7).
    The ADS7830 uses a control byte to specify the channel.
    """
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
  
    control_byte = 0x84 | (channel << 4)  # Channel selection bits
    bus.write_byte(DEVICE_ADDRESS, control_byte)
    data = bus.read_byte(DEVICE_ADDRESS)
    return data

# Example: Read from channel 0
try:
    channel = 3  # Select channel 0
    value = read_adc(channel)
    print(f"Analog value from channel {channel}: {value}")
except Exception as e:
    print(f"Error: {e}")