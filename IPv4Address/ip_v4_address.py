from exceptions import InvalidIPv4Address

class IPv4Address:

    def __init__(self, address):
        if valid_address(address) is False:
            raise InvalidIPv4Address('Invalid address!')
        self._ip = address

    def convert_ip_to_number(self):
        pow = 3
        num = 0

        if isinstance(self._ip, int):
            return self._ip

        for octet in self._ip.split('.'):
            num += (int(octet) * (256 ** pow))
            pow -= 1
        return num

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

    def less_than(self, address):
        if valid_address(address):
            address2 = IPv4Address(address)
            return self.convert_ip_to_number() < address2.convert_ip_to_number()
        raise InvalidIPv4Address('Invalid address!')

    def greater_than(self, address):
        return not self.less_than(address)

    def equals(self, address):
        if valid_address(address):
            address2 = IPv4Address(address)

            return self.convert_ip_to_number() == address2.convert_ip_to_number()
        raise InvalidIPv4Address('Invalid address!')

    def to_string(self):
        return self.convert_number_to_ip()

    def to_long(self):
        return self.convert_ip_to_number()

def valid_address(address):
    if isinstance(address, int):
        max = 4294967295
        if address > max or address < 0:
            return False
        else:
            return True
    try:
        max = 4
        index = 0
        octet = address.split('.')
        if len(octet) > max:
            return False
        while index < max:
            if int(octet[index]) < 0 or int(octet[index]) > 255:
                return False
            if octet[index][0] == '0' and len(octet[index]) != 1:
                return False
            if octet[index][0] == '-':
                return False
            index += 1
    except Exception:
        return False
    return True

if __name__ == '__main__':
    address = IPv4Address('127.0.0.1')
    print(address.to_string())
    print(address.to_long())

    address = IPv4Address(2130706433)
    print(address.to_string())
    print(address.to_long())

    print(address.equals('127.0.1.1'))
    print(address.equals(2130706433))
    print(address.greater_than('10.10.1.1'))
    print(address.greater_than(543070343))
    print(address.less_than('25.38.38.5'))
