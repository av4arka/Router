from ip_v4_address import IPv4Address
from exceptions import InvalidNetwork


class Network:

    def __init__(self, address, mask_length):
        if not valid_network(address, mask_length):
            raise InvalidNetwork('Invalid network!')

        free_part = 32 - mask_length
        self._address = IPv4Address(address.to_long() >> free_part << free_part)
        self._mask_length = mask_length

    def __str__(self):
        return f'{self._address.to_string()}/{self._mask_length}'

    @property
    def address(self):
        return self._address

    @property
    def mask(self):
        return (1 << 32) - (1 << 32 >> self._mask_length)

    def get_first_usable_address(self):
        if self._mask_length == 32:
            first_address = self._address.to_long()
        else:
            first_address = self._address.to_long() + 1
        return IPv4Address(first_address)

    def get_last_usable_address(self):
        if self._mask_length == 32:
            first_address = self._address.to_long()
        else:
            first_address = self.get_broadcast_address().to_long() - 1
        return IPv4Address(first_address)

    def get_mask_string(self):
        return IPv4Address(self.mask).to_string()

    def get_mask_length(self):
        return self._mask_length

    def get_broadcast_address(self):
        bin_address = ''.join([bin(int(x) + 256)[3:]
                               for x in self._address.to_string().split('.')])
        broadcast_max = 32 - self._mask_length
        bit_sequence = ''

        for counter in range(broadcast_max):
            bit_sequence += '1'

        broadcast_address = bin_address[:self._mask_length] + bit_sequence
        return IPv4Address(int(broadcast_address, 2))

    def __contains__(self, address):
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
        for network in private_networks:
            if self._address == network.address.to_string():
                return False
        return True

    def get_total_hosts(self):
        if self._mask_length == 32:
            return 0

        total_free_bit = 32 - self._mask_length
        return (2 ** total_free_bit) - 2

    def get_subnets(self):
        if self._mask_length == 32 or self._mask_length == 31:
            raise InvalidNetwork('subnet mask too large!')

        half_subnet_hosts = self.get_total_hosts() / 2
        second_subnet = self._address.to_long() + half_subnet_hosts + 1

        return [Network(IPv4Address(self._address.to_long()), self._mask_length + 1),
                Network(IPv4Address(int(second_subnet)), self._mask_length + 1)]


def valid_network(address, mask_length):
    if not isinstance(address, IPv4Address):
        return False
    if mask_length < 0 or mask_length > 32 or not isinstance(mask_length, int):
        return False
    return True


private_networks = (Network(IPv4Address('10.0.0.0'), 8),
                    Network(IPv4Address('192.168.0.0'), 16),
                    Network(IPv4Address('172.16.0.0'), 12)
                    )

if __name__ == '__main__':
    address = IPv4Address('172.16.0.0')
    network = Network(address, 8)

    print(network)
    print(network.get_first_usable_address().to_string())
    print(network.get_last_usable_address().to_string())
    print(network.is_public())
    if IPv4Address('172.255.255.255') in network:
        print('Yes')
    else:
        print('No')

    print(network.get_mask_string())
    print(network.get_mask_length())
    print(network.is_public())
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

