import serial
import struct
import random
import time

# Define the serial port and baud rate
serial_port = "COM1"  # Change this to match your serial port
baud_rate = 115200

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while True:
        # Generate random data for telemetry
        packetCount = 0
        mode = 0
        state = 0
        altitude = 0
        temperature = 0
        pressure = 0
        voltage = 0
        gpsTime = 0
        gpsLatitude = 0
        gpsLongitude = 0
        gpsSats = 0
        tiltX = 0
        tiltY = 1
        rotZ = 0

        # Pack the telemetry data into a binary string
        telemetry_data = struct.pack(
            "B" * 14,
            packetCount,
            mode,
            state,
            altitude,
            temperature,
            pressure,
            voltage,
            gpsTime,
            gpsLatitude,
            gpsLongitude,
            gpsSats,
            tiltX,
            tiltY,
            rotZ,
        )

        # Send the telemetry data over the serial port
        ser.write(telemetry_data)

        # Print the sent telemetry data
        print("Sent telemetry data:", telemetry_data)

        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping script...")
    ser.close()
