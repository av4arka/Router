from IPv4Address import  IPv4Address


class Network:

    def __init__(self, address, mask):
        if type(address) is not IPv4Address:
            print('Invalid address!')
            return

        if type(mask) is not int or mask < 0 or mask > 32:
            print('Invalid mask!')
            return
        self._mask = mask

        bin_address = bin(address.to_long())[2:]
        bin_mask = bin(IPv4Address(self.get_mask_string()).to_long())[2:]
        network_address = IPv4Address(int(bin_address, 2) & int(bin_mask, 2))

        self._address = network_address

    def get_address(self):
        return self._address

    def get_first_usable_address(self):
        first_address = self._address.to_long() + 1
        return IPv4Address(first_address)

    def get_last_usable_address(self):
        last_address = self.get_broadcast_address().to_long() - 1
        return IPv4Address(last_address)

    def get_mask(self):
        return (1<<32) - (1<<32>>self._mask)

    def get_mask_string(self):
        ip_address = IPv4Address(self.get_mask()).to_string()
        return ip_address

    def get_mask_length(self):
        return self._mask


    def get_broadcast_address(self):
        bin_address = ''.join([bin(int(x) + 256)[3:] for x in self._address.to_string().split('.')])
        broadcast_max = 32 - self._mask
        counter = 0
        bit_sequence = ''

        while counter < broadcast_max:
            bit_sequence += '1'
            counter += 1

        broadcast_address = bin_address[0:self._mask] + bit_sequence
        return IPv4Address(int(broadcast_address, 2))

    def contains(self, address):
        try:
            number_address = address.to_long()
            min_address = self.get_first_usable_address().to_long()
            max_address = self.get_last_usable_address().to_long()
            if number_address < min_address or number_address > max_address:
                return False

            return True
        except ValueError:
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

