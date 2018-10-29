from IPv4Address import  IPv4Address

class Network:


    def __init__(self, address, mask):
        if type(address) is not IPv4Address:
            print('Invalid address!')
            return

        if 0 < mask > 32:
             print('Invalid mask!')
             return

        address_mask = (1<<32) - (1<<32>>mask)
        bin_address = bin(address.to_long())[2:]
        bin_mask = bin(address_mask)[2:]
        network_address = IPv4Address(int(bin_address, 2) & int(bin_mask, 2))

        self._mask = mask
        self._address = network_address.to_string()


    # def get_first_usable_addres(self):

