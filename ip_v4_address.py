from exceptions import InvalidIPv4Address


class IPv4Address:

    def __init__(self, address):
        if not valid_address(address):
            raise InvalidIPv4Address('Invalid address!')
        self._ip = address
        self._ip = self.convert_ip_to_number()

    def convert_ip_to_number(self):
        if isinstance(self._ip, int):
            return self._ip
        octet = self._ip.split('.')
        return (int(octet[0]) << 24) + (int(octet[1]) << 16) + (int(octet[2]) << 8) + (int(octet[3]))

    def convert_number_to_ip(self):
        div = 16777216
        address = [0, 0, 0, 0]
        ip = self._ip

        if isinstance(self._ip, str):
            return self._ip

        for index in range(4):
            num = int(ip / div)
            ip -= div * num
            div /= 256
            address[index] = str(num)

        return '.'.join(address)

    def __lt__(self, address):
        try:
            return self._ip < IPv4Address(address).to_long()
        except Exception:
            raise InvalidIPv4Address('Invalid address!')

    def __gt__(self, address):
        return not self < address

    def __eq__(self, address):
        try:
            return self._ip == IPv4Address(address).to_long()
        except Exception:
            raise InvalidIPv4Address('Invalid address!')

    def to_string(self):
        return self.convert_number_to_ip()

    def to_long(self):
        return self._ip

def valid_address(address):
    if isinstance(address, int):
        max = 4294967295
        if address > max or address < 0:
            return False
        return True

    try:
        octet = address.split('.')
        if len(octet) > 4:
            return False

        for oct in octet:
            if int(oct) < 0 or int(oct) > 255:
                return False
            if oct[0] == '0' and len(oct) != 1:
                return False
            if oct[0] == '-':
                return False
    except Exception:
        return False
    return True

if __name__ == '__main__':
    address = IPv4Address('127.55.100.0')
    print(address.to_string())
    print(address.to_long())

    address = IPv4Address(2134336512)
    ip = address.to_long() >> 28 << 28
    print(IPv4Address(ip).to_string())
    print(address.to_string())
    print(address.to_long())

    print(address == '127.0.1.1')
    print(address == 2130706433)
    print(address > '10.10.1.1')
    print(address > 2130706434)
    print(address < '25.38.38.5')




