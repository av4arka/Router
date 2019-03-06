## Purpose:
The router knows several routes and can find the most suitable route among the known ones.
## Usage example:
```python3.6
  route1 = Route(Network(IPv4Address('20.0.0.0'), 8), '192.168.0.1', 'en2', 10)
  route2 = Route(Network(IPv4Address('192.168.0.0'), 24), None, 'en0', 10)
  route3 = Route(Network(IPv4Address('20.0.0.0'), 8), '10.123.0.1', 'lo2', 5)
  
  router = Router()
  router.add_route(route1)
  router.add_route(route2)
  router.add_route(route3)
  
  route = router.get_route_for_address(IPv4Address('20.168.0.0'))
  print(route) # net: 20.0.0.0/8, gateway: 10.123.0.1, interface: lo2, metric: 5
  route = router.get_route_for_address(IPv4Address('192.0.0.0'))
  print(route) # default route - net: 0.0.0.0/0, interface: default, metric: 10
```
---
## Additional modules:
### IPv4Address and Network:
These classes provide opportunities for creating, managing, and working with IPv4 addresses and networks.
## Usage example:
```python3.6
  address = IPv4Address('192.168.0.1')
  network = Network(address, 24)
  
  print(network) # 192.168.0.0/24
  print(network.get_first_usable_address().to_string()) # 192.168.0.1
  print(network.get_last_usable_address().to_string()) # 192.168.0.254
  print(network.get_total_hosts()) # 254
  print(network.get_broadcast_address().to_string()) # 192.168.0.255
  
  subnets = network.get_subnets()
  
  print(subnets[0]) # 192.168.0.0/25
  print(subnets[1]) # 192.168.0.128/25
  print(subnets[0].get_broadcast_address().to_string()) # 192.168.0.127
  print(subnets[1].get_broadcast_address().to_string()) # 192.168.0.255
```

