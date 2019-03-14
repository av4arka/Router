from ip_v4_address import IPv4Address
from exceptions import InvalidNetwork


class Network:

    def __init__(self, address, mask):
        if not valid_network(address, mask):
            raise InvalidNetwork('Invalid network!')
        if mask < 0 or mask > 32 or type(mask) is not int:
            raise InvalidNetwork('Invalid network mask!')

        self._mask = mask
        bin_address = bin(address.to_long())[2:]
        bin_mask = bin(IPv4Address(self.get_mask_string()).to_long())[2:]
        network_address = IPv4Address(int(bin_address, 2) & int(bin_mask, 2))

        self._address = network_address

    def __repr__(self):
        return f'{self._address.to_string()}/{self._mask}'

    @property
    def address(self):
        return self._address

    @property
    def mask(self):
        return (1 << 32) - (1 << 32 >> self._mask)

    def get_first_usable_address(self):
        first_address = self._address.to_long() + 1
        return IPv4Address(first_address)

    def get_last_usable_address(self):
        last_address = self.get_broadcast_address().to_long() - 1
        return IPv4Address(last_address)

    def get_mask_string(self):
        return IPv4Address(self.mask).to_string()

    def get_mask_length(self):
        return self._mask

    def get_broadcast_address(self):
        bin_address = ''.join([bin(int(x) + 256)[3:]
                               for x in self._address.to_string().split('.')])
        broadcast_max = 32 - self._mask
        bit_sequence = ''

        for counter in range(broadcast_max):
            bit_sequence += '1'

        broadcast_address = bin_address[:self._mask] + bit_sequence
        return IPv4Address(int(broadcast_address, 2))

    def contains(self, address):
        try:
            number_address = address.to_long()
            min_address = self.get_first_usable_address().to_long()
            max_address = self.get_last_usable_address().to_long()
            if number_address < min_address or number_address > max_address:
                return False

            return True
        except Exception:
            return False

    def is_public(self):
        address = self._address.to_string().split('.')

        if address[0] == '10' and self._mask > 7:
            return False
        if address[0] == '192' and address[1] == '168' and self._mask > 15:
            return False
        if address[0] == '172' and int(address[1]) > 15 and int(address[1]) < 32:
            return False
        return True

    def get_total_hosts(self):
        if self._mask == 32:
            return 0

        total_free_bit = 32 - self._mask
        return (2**total_free_bit) - 2

    def get_subnets(self):
        if self._mask == 32 or self._mask == 31:
            raise InvalidNetwork('subnet mask too large!')

        half_subnet_hosts = self.get_total_hosts() / 2
        second_subnet = self._address.to_long() + half_subnet_hosts + 1

        return [Network(IPv4Address(self._address.to_long()), self._mask + 1),
                Network(IPv4Address(int(second_subnet)), self._mask + 1)]

def valid_network(address, mask):
    if not isinstance(address, IPv4Address):
        return False
    if mask < 0 or mask > 32 or not isinstance(mask, int):
        return False
    return True

if __name__ == '__main__':
    address = IPv4Address('192.0.0.0')
    network = Network(address, 24)

    print(network)
    print(network.address.to_string())
    print(network.get_first_usable_address().to_string())
    print(network.get_last_usable_address().to_string())
    print(network.get_mask_string())
    print(network.get_mask_length())
    print(network.is_public())
    print(network.contains(IPv4Address('127.0.0.1')))
    print(network.contains(IPv4Address('192.0.0.42')))
    print(network.get_total_hosts())
    print(network.get_broadcast_address().to_string())
    print()

    subnets = network.get_subnets()

    print(subnets[0])
    print(subnets[1])
    print(subnets[0].address.to_string())
    print(subnets[0].get_first_usable_address().to_string())
    print(subnets[0].get_last_usable_address().to_string())
    print(subnets[0].get_broadcast_address().to_string())
    print(subnets[0].get_mask_length())
