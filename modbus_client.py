from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("192.168.195.129", port=502)
client.connect()

while True:
    rr = client.read_holding_registers(address=0, count=1, slave=1)
    if rr.isError():
        print("Error reading Modbus data.")
    else:
        print(f"Water Level: {rr.registers[0]}")
    time.sleep(3)
