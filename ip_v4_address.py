from exceptions import InvalidIPv4Address

class IPv4Address:

    def valid_address(self, address):
        if type(address) is int:
            max = 4294967295

            if address > max or address < 0:
                return False
            else:
                return True

        try:
            max = 4
            index = 0

            points = address.split('.')

            if len(points) > max:
                return False

            while index < max:
                if int(points[index]) < 0 or int(points[index]) > 255:
                    return False
                if points[index][0] == '0' and len(points[index]) != 1:
                    return False
                if points[index][0] == '-':
                    return False

                index += 1

        except Exception:
            return False
        return True

    def __init__(self, address):
        if self.valid_address(address) is False:
            raise IPv4Address('Invalid address!')
        self._ip = address

    def convert_ip_to_number(self):
        pow = 3
        num = 0

        if type(self._ip) is not str:
            return int(self._ip)

        for quad in self._ip.split('.'):
            num += (int(quad) * (256 ** pow))
            pow -= 1
        return num

    def convert_number_to_ip(self):
        div = 16777216
        index = 0
        address = [0, 0, 0, 0]
        point = '.'
        ip = self._ip

        if type(self._ip) is str:
            return self._ip

        while index < 4:
            num = int(ip / div)
            ip -= div * num
            address[index] = str(num)
            div /= 256
            index += 1

        return point.join(address)

    def less_than(self, address):
        if self.valid_address(address):
            address2 = IPv4Address(address)

            return self.convert_ip_to_number() < address2.convert_ip_to_number()

    def greater_than(self, address):
        return not self.less_than(address)

    def equals(self, address):
        if self.valid_address(address):
            address2 = IPv4Address(address)

            return self.convert_ip_to_number() == address2.convert_ip_to_number()

    def to_string(self):
        return self.convert_number_to_ip()

    def to_long(self):
        return self.convert_ip_to_number()
