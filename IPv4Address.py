class IPv4Address:

    def valid_address(self, address):
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
        if type(address) is int:
            number_ip = 4294967295
            if address > number_ip or address < 0 :
                print('Invalid address number!')
                return
        elif type(address) is str:
            if self.valid_address(address) is False:
                print('Invalid address!')
                return
        else:
            print('invalid address')
            return

        self._ip = address

    def convert_ip_to_number(self):
        pow = 3
        num = 0

        if type(self._ip) is int:
            return self._ip

        for quad in self._ip.split('.'):
            num += (int(quad) * (256 ** pow))
            pow -= 1
        return num

    def convert_number_to_ip(self):
        div = 16777216
        index = 0
        address = [0, 0, 0, 0]
        point = '.'

        if type(self._ip) is str:
            return self._ip

        while index < 4:
            num = int(self._ip / div)
            self._ip -= div * num
            address[index] = str(num)
            div /= 256
            index += 1

        return point.join(address)