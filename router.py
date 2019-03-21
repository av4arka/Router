from network import Network
from ip_v4_address import IPv4Address
from exceptions import InvalidRoute, InvalidRouter, InvalidIPv4Address


class Route:

    def __init__(self, network, gateway, interface_name, metric):
        if not valid_route(network, gateway, interface_name, metric):
            raise InvalidRoute('Invalid route!')

        self._network = network
        self._interface_name = interface_name
        self._metric = metric

        if gateway is not None:
            gateway = IPv4Address(gateway)
        self._gateway = gateway

    def __repr__(self):
        if self._gateway is None:
            return f'net: {self._network}, interface: {self._interface_name}, metric: {self._metric}'

        return f'net: {self._network}, gateway: {self.gateway.to_string()}, interface: {self._interface_name}, metric: {self._metric}'

    @property
    def gateway(self):
        return self._gateway

    @property
    def interface_name(self):
        return self._interface_name

    @property
    def metric(self):
        return self._metric

    @property
    def network(self):
        return self._network

class Router:

    def __init__(self, routes=None):
        if routes is None:
            routes = []
        if not valid_routes(routes):
            raise InvalidRouter('Invalid router!')

        self._routes = routes
        self.add_route(Route(Network(IPv4Address('0.0.0.0'), 0), None, 'default', 10))

    @property
    def routes(self):
        return self._routes

    def add_route(self, route):
        if not isinstance(route, Route):
            raise InvalidRoute('Invalid route!')
        self._routes.append(route)

    def get_route_for_address(self, address):
        best_route = self.routes[0]

        if not isinstance(address, IPv4Address):
            raise InvalidIPv4Address('Invalid address!')

        for route in self._routes[1:]:
            network = Network(address, route.network.get_mask_length())

            if network.address.to_string() == route.network.address.to_string():
                if network.mask > best_route.network.mask:
                    best_route = route
                elif network.mask == best_route.network.mask:
                    if route.metric < best_route.metric:
                        best_route = route
        return best_route

    def remove_route(self, route):
        if route in self._routes:
            self._routes.remove(route)

def valid_route(network, gateway, interface_name, metric):
    try:
        IPv4Address(gateway)
    except InvalidIPv4Address:
        if gateway is not None:
            return False

    if not isinstance(network, Network):
        return False
    if not isinstance(interface_name, str):
        return False
    if not isinstance(metric, int):
        return False
    return True

def valid_routes(routes):
    if not isinstance(routes, list):
        return False
    for route in routes:
        if not isinstance(route, Route):
            return False
    return True

if __name__ == '__main__':
    route1 = Route(Network(IPv4Address('20.0.0.0'), 8), '192.168.0.1', 'en2', 10)
    route2 = Route(Network(IPv4Address('192.168.0.0'), 24), None, 'en0', 10)
    route3 = Route(Network(IPv4Address('20.0.0.0'), 8), '10.123.0.1', 'lo2', 5)
    route4 = Route(Network(IPv4Address('10.0.0.1'), 20), None, 'en1', 1)
    router = Router()

    router.add_route(route1)
    router.add_route(route2)
    router.add_route(route3)
    router.add_route(route4)

    route = router.get_route_for_address(IPv4Address('20.168.0.0'))
    print(route)

    route = router.get_route_for_address(IPv4Address('192.0.0.0'))
    print(route)

    router.remove_route(route2)
    router.remove_route(route3)

    print('\nRoutes:')
    for route in router.routes:
        print(route)

