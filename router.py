from network import Network
from ip_v4_address import IPv4Address
from exceptions import InvalidRoute, InvalidRouter

class Route:


    def valid_arguments(self, network, gateway, interface_name, metric):
        try:
            if not isinstance(gateway, IPv4Address):
                gateway = IPv4Address(gateway)
        except Exception:
            if gateway is not None:
                return False

        if not isinstance(network, Network):
            return False
        if not isinstance(interface_name, str):
            return False
        if not isinstance(metric, int):
            return False
        return True

    def __init__(self, network, gateway, interface_name, metric):
        if not self.valid_arguments(network, gateway, interface_name, metric):
            raise InvalidRoute('Invalid route!')

        self._network = network
        self._interface_name = interface_name
        self._metric = metric
        if isinstance(gateway, str):
            self._gateway = IPv4Address(gateway)
        else:
            self._gateway = gateway


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

    def __repr__(self):
        if self._gateway is None:
            return 'net: %s, interface: %s, metric: %d' % (
                self._network, self._interface_name, self._metric)

        return 'net: %s, gateway: %s, interface: %s, metric: %d' % (
            self._network, self._gateway.to_string(), self._interface_name, self._metric)


class Router:


    def valid_routes(self, routes):
        if type(routes) is not list or not len(routes):
            return False

        for route in routes:
            if not isinstance(route, Route):
                return False

        return True

    def __init__(self, routes):
        if not self.valid_routes(routes):
            raise InvalidRouter('Invalid router!')

        self._routes = routes

    def add_route(self, route):
        if not isinstance(route, Route):
            raise TypeError
        self._routes.append(route)

    def get_route_for_address(self, address):
        if not isinstance(address, IPv4Address ):
            raise TypeError
        try:
            best_route = self._routes[0]
        except IndexError:
            raise Exception('Router is empty!')

        if len(self._routes) == 1:
            network_purpose = Network(address, best_route.network.get_mask_length())
            if best_route.network.address.to_string() == network_purpose.address.to_string():
                return best_route
            else:
                return 0

        for route in self._routes:
            network = Network(address, route.network.get_mask_length())

            if network.address.to_string() == route.network.address.to_string():
                if network.mask > best_route.network.mask:
                    best_route = route
                if network.mask == best_route.network.mask:
                    if route.metric < best_route.metric:
                        best_route = route


        return best_route

    @property
    def routes(self):
        return self._routes

    def remove_route(self, route):
        if not isinstance(route, Route):
            raise TypeError

        if route in self._routes:
            self._routes.remove(route)
