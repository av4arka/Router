## Purpose:
The router contains a route table and can find the most suitable route among the known ones for a given destination address.
### Usage example:
```python
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

### Sample route table:
| Network Destination | Netmask      | Gateway     | Interface | Metric |
|---------------------|--------------|-------------|-----------|--------|
| 20.0.0.0            | 255.0.0.0    | 192.168.0.1 | en2       | 10     |
| 192.168.0.0         | 255.255.255.0| None        | en0       | 10     |
| 20.0.0.0            | 255.0.0.0    | 10.123.0.1  | lo2       | 5      |

---
### Additional modules:
#### IPv4Address:
 This class provides the ability to create, manage, and work with IPv4 addresses.
 
##### Usage example:
```python
address = IPv4Address('127.0.0.1')
print(address.to_long())
print(address.to_string())
print(address.equals('127.0.1.1'))
print(address.equals(2130706433))
print(address.greater_than('10.10.1.1'))
print(address.less_than(2130706432))

```
#### Network:
This class provides the capabilities to create, manipulate and operate on IPv4 addresses and networks.
##### Usage example:
```python
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

