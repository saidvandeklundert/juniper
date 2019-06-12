# !/usr/bin/env python
#
#
# Created by Said van de Klundert
#
# Gathers the IP addresses configured on a Juniper device.
#
#
from jnpr.junos import Device
from json import dumps

def interface_to_instance_mapping(cfg_routing_instances):
    """
    Return a dictionary that contains the mapping of interfaces to instance
    :return: { interface-name : routing-instance-name }
    """
    routing_instances_info = {}
    routing_instances = cfg_routing_instances.findall('.//instance')

    for routing_instance in routing_instances:
        routing_instance_name = routing_instance.find('.//name').text

        for interface in routing_instance.findall('.//interface'):
            routing_instance_interface_name = interface.find('.//name').text
            routing_instances_info[routing_instance_interface_name] = routing_instance_name

    return routing_instances_info


def build_host_ip_info(cfg_interfaces, routing_instances_info):
    """
    Takes in lxml objects and returns the following:
    { interface-name : (('instance', instance-name), ('ipv4', ipv4-address), ('ipv6', ipv6-address)))
    """
    host_ip_info = {}
    main_interfaces = cfg_interfaces.findall('.//interface')

    for interface in main_interfaces:

        if len(interface.findall('.//unit')):
            name = interface.find('.//name').text

            for unit in interface.findall('.//unit'):
                
                unit_number = unit.find('.//name').text
                interface_id = name + '.' + unit_number
                instance = tuple(['instance', routing_instances_info.get(interface_id, None)])

                if unit.find('.//family/inet/address/name') is None:
                    unit_ipv4_address = tuple(['ipv4', None])
                else:                                                                 
                    ipv4_list = [ipv4.text for ipv4 in unit.findall('.//family/inet/address/name') ]                    
                    unit_ipv4_address = tuple(['ipv4', ipv4_list ])
                    

                if unit.find('.//family/inet6/address/name') is None:
                    unit_ipv6_address = tuple(['ipv6', None])
                else:                    
                    ipv6_list = [ipv6.text for ipv6 in unit.findall('.//family/inet6/address/name') ]                    
                    unit_ipv6_address = tuple(['ipv6', ipv6_list ])
                
                if unit_ipv4_address[1] is None and unit_ipv6_address[1] is None:
                    continue

                host_ip_info[interface_id] = (instance, unit_ipv4_address, unit_ipv6_address)

    return host_ip_info

def get_ip_info(host, username, pwd):
    """
    Logs in to a Junos OS device, retrieves interface and instance information and returns a dictionary with the following format:
    { interface-name : (('instance', instance-name), ('ipv4', ipv4-address), ('ipv6', ipv6-address)))
    """

    # opening the device connection and talking to MGD
    dev = Device(host=host, user=username, password=pwd, normalize=True, auto_probe=4, timeout=10)
    dev.open()
    cfg_interfaces = dev.rpc.get_config(filter_xml='interfaces')
    cfg_routing_instances = dev.rpc.get_config(filter_xml='routing-instances')
    dev.close()

    # building the dict that containst the interface to instance-name mapping:
    routing_instances_info = interface_to_instance_mapping(cfg_routing_instances)

    # building the dict that contains information for all interfaces
    host_ip_info = build_host_ip_info(cfg_interfaces, routing_instances_info)

    return host_ip_info


def write_as_json(file_path, data):
    """"
    file_path: example: /var/tmp/data.sls
    data: dictionary
    """
    with open(file_path, "w") as file:
        file.write(dumps(data, indent=4, separators=(',', ': ')))





if __name__ == "__main__":
    """
    You can run the script targeting a single host:
    
    python juniper_gather_ips.py < hostname >
    
    """
    from os import getlogin, getcwd
    import getpass, sys

    username = getlogin()
    pwd = getpass.getpass()
    file_path = getcwd() + '/data.json'
    host = sys.argv[1]
    ip_host_info = get_ip_info(host, username, pwd)
    
    for k,v in sorted(ip_host_info.items()):
        print(k)    # interface name, example: 'ae20.0'
        print(v)    # tuple(('instance', 'routing_instance'), ('ipv4', ['192.168.1.1/24',]), ('ipv6', ['2001:0000:0000:0000::130/127']))
    
    write_as_json(file_path, ip_host_info)
