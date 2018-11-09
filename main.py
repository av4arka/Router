from network import Network
from ip_v4_address import IPv4Address
from exceptions import InvalidIPv4Address, InvalidNetwork

if __name__ == '__main__':
    try:
        ip_v4_address = IPv4Address('255.123.145.23')
        network = Network(ip_v4_address, 29)
    except InvalidIPv4Address:
        print(InvalidIPv4Address.text)
    except InvalidNetwork:
        print(InvalidNetwork.text)

    # print(network)

