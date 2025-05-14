from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

# Create datastore
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [75]*100),  # Water level at address 0
    ir=ModbusSequentialDataBlock(0, [0]*100))

# Create server context
context = ModbusServerContext(slaves=store, single=True)

print("Starting Modbus TCP server...")

# Start the server
StartTcpServer(context, address=("0.0.0.0", 502))

print("Modbus server should now be running.")
