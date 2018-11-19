from network import Network
from ip_v4_address import IPv4Address
from exceptions import InvalidIPv4Address, InvalidNetwork
from router import Route, Router

if __name__ == '__main__':
    try:
        ip_v4_address = IPv4Address('255.123.145.23')
        network1 = Network(ip_v4_address, 0)
        network2 = Network(ip_v4_address, 0)
        network3 = Network(ip_v4_address, 0)
        network4 = Network(ip_v4_address, 0)
        network5 = Network(ip_v4_address, 10)
    except InvalidIPv4Address:
        print(InvalidIPv4Address.text)
    except InvalidNetwork:
        print(InvalidNetwork.text)

    route1 = Route(Network(IPv4Address("0.0.0.0"), 0), "192.168.0.1", "en0", 1)
    route2 = Route(Network(IPv4Address("192.168.0.0"), 24), None, "en0", 2)
    route3 = Route(Network(IPv4Address("10.0.0.0"), 8), "10.123.0.1", "en1", 3)
    route4 = Route(Network(IPv4Address("10.123.0.0"), 20), None, "en1", 4)
    route5 = Route(network5, None, '5', 5)
    router = Router([route1])

    router.add_route(route2)
    router.add_route(route3)
    router.add_route(route4)
    router.add_route(route5)

    router.remove_route(route2)
    router.remove_route(route4)
    # route = router.get_route_for_address(IPv4Address('192.168.0.176'))
    # print(route.metric)
    # print(route.interface_name)
    # net = route.network
    # print(net)
    #
    # route = router.get_route_for_address(IPv4Address('10.0.1.1'))
    # print(route.metric)
    # print(route.interface_name)
    # net = route.network
    # print(net)
    #
    for r in router.routes:
        print(r)
