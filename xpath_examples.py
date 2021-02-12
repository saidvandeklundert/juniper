"""
/var/tmp/example.py:
from lxml import etree
from jnpr.junos import Device
import getpass
import sys

username = sys.argv[1]
host = sys.argv[2]
password = getpass.getpass()

with Device(host=host, user=username, password=password, normalize=True) as dev:                                  
    rpc = dev.rpc.get_interface_information(extensive=True)
"""
[root@said /]# python -i /var/tmp/example.py admin vmx-01
Password: 
>>> 
>>> 
>>> #XPATH getting all the interface names:
>>> rpc.xpath('//physical-interface/name/text()')
['lc-1/0/0', 'pfe-1/0/0', 'pfh-1/0/0', 'xe-1/0/0', 'xe-1/0/1', 'xe-1/0/2', 'xe-1/0/3', 'lc-1/1/0', 'pfe-1/1/0', 'xe-1/1/0', 'xe-1/1/1', 'xe-1/1/2', 'xe-1/1/3', 'lc-1/2/0', 'pfe-1/2/0', 'xe-1/2/0', 'xe-1/2/1', 'xe-1/2/2', 'xe-1/2/3', 'lc-1/3/0', 'pfe-1/3/0', 'xe-1/3/0', 'xe-1/3/1', 'xe-1/3/2', 'xe-1/3/3', '.local.', 'ae0', 'ae1', 'ae2', 'ae3', 'ae6', 'ae7', 'ae8', 'ae9', 'ae10', 'ae11', 'ae13', 'ae21', 'ae22', 'cbp0', 'demux0', 'dsc', 'em0', 'em1', 'esi', 'fxp0', 'gre', 'ipip', 'irb', 'jsrv', 'lo0', 'lsi', 'mtun', 'pimd', 'pime', 'pip0', 'pp0', 'rbeb', 'tap', 'vtep']
>>> 
>>> #XPATH getting all the logical interface names:
>>> rpc.xpath('//physical-interface/logical-interface/name/text()')
['lc-1/0/0.32769', 'pfe-1/0/0.16383', 'pfh-1/0/0.16383', 'pfh-1/0/0.16384', 'xe-1/0/0.0', 'xe-1/0/1.0', 'xe-1/0/2.0', 'xe-1/0/3.0', 'lc-1/1/0.32769', 'pfe-1/1/0.16383', 'xe-1/1/0.0', 'xe-1/1/1.0', 'xe-1/1/2.0', 'xe-1/1/3.0', 'lc-1/2/0.32769', 'pfe-1/2/0.16383', 'xe-1/2/0.1', 'xe-1/2/0.2', 'xe-1/2/0.32767', 'xe-1/2/1.0', 'xe-1/2/2.0', 'xe-1/2/3.0', 'lc-1/3/0.32769', 'pfe-1/3/0.16383', 'xe-1/3/0.0', 'xe-1/3/1.0', 'xe-1/3/2.0', 'xe-1/3/3.0', '.local..0', '.local..1', '.local..2', '.local..3', '.local..4', '.local..5', '.local..6', '.local..7', '.local..8', '.local..9', '.local..36735', '.local..36736', 'ae0.0', 'ae1.0', 'ae2.1', 'ae2.2', 'ae2.32767', 'ae3.0', 'ae6.0', 'ae7.0', 'ae8.0', 'ae9.0', 'ae10.0', 'ae11.0', 'ae13.0', 'ae21.0', 'ae22.0', 'em0.0', 'em1.0', 'fxp0.0', 'jsrv.1', 'lo0.0', 'lo0.16384', 'lo0.16385', 'lsi.0', 'lsi.1']
>>> 
>>> # XPATH getting all the interface names of the physicall as well as the logical interfaces:
>>> rpc.xpath('//physical-interface/name/text()|//physical-interface/logical-interface/name/text()')
['lc-1/0/0', 'lc-1/0/0.32769', 'pfe-1/0/0', 'pfe-1/0/0.16383', 'pfh-1/0/0', 'pfh-1/0/0.16383', 'pfh-1/0/0.16384', 'xe-1/0/0', 'xe-1/0/0.0', 'xe-1/0/1', 'xe-1/0/1.0', 'xe-1/0/2', 'xe-1/0/2.0', 'xe-1/0/3', 'xe-1/0/3.0', 'lc-1/1/0', 'lc-1/1/0.32769', 'pfe-1/1/0', 'pfe-1/1/0.16383', 'xe-1/1/0', 'xe-1/1/0.0', 'xe-1/1/1', 'xe-1/1/1.0', 'xe-1/1/2', 'xe-1/1/2.0', 'xe-1/1/3', 'xe-1/1/3.0', 'lc-1/2/0', 'lc-1/2/0.32769', 'pfe-1/2/0', 'pfe-1/2/0.16383', 'xe-1/2/0', 'xe-1/2/0.1', 'xe-1/2/0.2', 'xe-1/2/0.32767', 'xe-1/2/1', 'xe-1/2/1.0', 'xe-1/2/2', 'xe-1/2/2.0', 'xe-1/2/3', 'xe-1/2/3.0', 'lc-1/3/0', 'lc-1/3/0.32769', 'pfe-1/3/0', 'pfe-1/3/0.16383', 'xe-1/3/0', 'xe-1/3/0.0', 'xe-1/3/1', 'xe-1/3/1.0', 'xe-1/3/2', 'xe-1/3/2.0', 'xe-1/3/3', 'xe-1/3/3.0', '.local.', '.local..0', '.local..1', '.local..2', '.local..3', '.local..4', '.local..5', '.local..6', '.local..7', '.local..8', '.local..9', '.local..36735', '.local..36736', 'ae0', 'ae0.0', 'ae1', 'ae1.0', 'ae2', 'ae2.1', 'ae2.2', 'ae2.32767', 'ae3', 'ae3.0', 'ae6', 'ae6.0', 'ae7', 'ae7.0', 'ae8', 'ae8.0', 'ae9', 'ae9.0', 'ae10', 'ae10.0', 'ae11', 'ae11.0', 'ae13', 'ae13.0', 'ae21', 'ae21.0', 'ae22', 'ae22.0', 'cbp0', 'demux0', 'dsc', 'em0', 'em0.0', 'em1', 'em1.0', 'esi', 'fxp0', 'fxp0.0', 'gre', 'ipip', 'irb', 'jsrv', 'jsrv.1', 'lo0', 'lo0.0', 'lo0.16384', 'lo0.16385', 'lsi', 'lsi.0', 'lsi.1', 'mtun', 'pimd', 'pime', 'pip0', 'pp0', 'rbeb', 'tap', 'vtep']
>>> 
>>> # XPATH getting all the physical and logical interface XML data:
>>> rpc.xpath('//physical-interface|//physical-interface/logical-interface')
[<Element physical-interface at 0x7fdceabd2e40>, <Element logical-interface at 0x7fdceab814c0>, <Element physical-interface at 0x7fdceab81500>, <Element logical-interface at 0x7fdceab81540>, <Element physical-interface at 0x7fdceab81580>, <Element logical-interface at 0x7fdceab81600>, <Element logical-interface at 0x7fdceab81640>, <Element physical-interface at 0x7fdceab81680>, <Element logical-interface at 0x7fdceab816c0>, <Element physical-interface at 0x7fdceab815c0>, <Element logical-interface at 0x7fdceab81700>, <Element physical-interface at 0x7fdceab81740>, <Element logical-interface at 0x7fdceab81780>, <Element physical-interface at 0x7fdceab817c0>, <Element logical-interface at 0x7fdceab81800>, <Element physical-interface at 0x7fdceab81840>, <Element logical-interface at 0x7fdceab81880>, <Element physical-interface at 0x7fdceab818c0>, <Element logical-interface at 0x7fdceab81900>, <Element physical-interface at 0x7fdceab81940>, <Element logical-interface at 0x7fdceab81980>, <Element physical-interface at 0x7fdceab819c0>, <Element logical-interface at 0x7fdceab81a00>, <Element physical-interface at 0x7fdceab81a40>, <Element logical-interface at 0x7fdceab81a80>, <Element physical-interface at 0x7fdceab81ac0>, <Element logical-interface at 0x7fdceab81b00>, <Element physical-interface at 0x7fdceab81b40>, <Element logical-interface at 0x7fdceab81b80>, <Element physical-interface at 0x7fdceab81bc0>, <Element logical-interface at 0x7fdceab81c00>, <Element physical-interface at 0x7fdceab81c40>, <Element logical-interface at 0x7fdceab81c80>, <Element logical-interface at 0x7fdceab81cc0>, <Element logical-interface at 0x7fdceab81d00>, <Element physical-interface at 0x7fdceab81d40>, <Element logical-interface at 0x7fdceab81d80>, <Element physical-interface at 0x7fdceab81dc0>, <Element logical-interface at 0x7fdceab81e00>, <Element physical-interface at 0x7fdceab81e40>, <Element logical-interface at 0x7fdceab81e80>, <Element physical-interface at 0x7fdceab81ec0>, <Element logical-interface at 0x7fdceab81f00>, <Element physical-interface at 0x7fdceab81f40>, <Element logical-interface at 0x7fdceab81f80>, <Element physical-interface at 0x7fdceab81fc0>, <Element logical-interface at 0x7fdceab7f040>, <Element physical-interface at 0x7fdceab7f080>, <Element logical-interface at 0x7fdceab7f0c0>, <Element physical-interface at 0x7fdceab7f100>, <Element logical-interface at 0x7fdceab7f140>, <Element physical-interface at 0x7fdceab7f180>, <Element logical-interface at 0x7fdceab7f1c0>, <Element physical-interface at 0x7fdceab7f200>, <Element logical-interface at 0x7fdceab7f240>, <Element logical-interface at 0x7fdceab7f280>, <Element logical-interface at 0x7fdceab7f2c0>, <Element logical-interface at 0x7fdceab7f300>, <Element logical-interface at 0x7fdceab7f340>, <Element logical-interface at 0x7fdceab7f380>, <Element logical-interface at 0x7fdceab7f3c0>, <Element logical-interface at 0x7fdceab7f400>, <Element logical-interface at 0x7fdceab7f440>, <Element logical-interface at 0x7fdceab7f480>, <Element logical-interface at 0x7fdceab7f4c0>, <Element logical-interface at 0x7fdceab7f500>, <Element physical-interface at 0x7fdceab7f540>, <Element logical-interface at 0x7fdceab7f580>, <Element physical-interface at 0x7fdceab7f5c0>, <Element logical-interface at 0x7fdceab7f600>, <Element physical-interface at 0x7fdceab7f640>, <Element logical-interface at 0x7fdceab7f680>, <Element logical-interface at 0x7fdceab7f6c0>, <Element logical-interface at 0x7fdceab7f700>, <Element physical-interface at 0x7fdceab7f740>, <Element logical-interface at 0x7fdceab7f780>, <Element physical-interface at 0x7fdceab7f7c0>, <Element logical-interface at 0x7fdceab7f800>, <Element physical-interface at 0x7fdceab7f840>, <Element logical-interface at 0x7fdceab7f880>, <Element physical-interface at 0x7fdceab7f8c0>, <Element logical-interface at 0x7fdceab7f900>, <Element physical-interface at 0x7fdceab7f940>, <Element logical-interface at 0x7fdceab7f980>, <Element physical-interface at 0x7fdceab7f9c0>, <Element logical-interface at 0x7fdceab7fa00>, <Element physical-interface at 0x7fdceab7fa40>, <Element logical-interface at 0x7fdceab7fa80>, <Element physical-interface at 0x7fdceab7fac0>, <Element logical-interface at 0x7fdceab7fb00>, <Element physical-interface at 0x7fdceab7fb40>, <Element logical-interface at 0x7fdceab7fb80>, <Element physical-interface at 0x7fdceab7fbc0>, <Element logical-interface at 0x7fdceab7fc00>, <Element physical-interface at 0x7fdceab7fc40>, <Element physical-interface at 0x7fdceab7fc80>, <Element physical-interface at 0x7fdceab7fcc0>, <Element physical-interface at 0x7fdceab7fd00>, <Element logical-interface at 0x7fdceab7fd40>, <Element physical-interface at 0x7fdceab7fd80>, <Element logical-interface at 0x7fdceab7fdc0>, <Element physical-interface at 0x7fdceab7fe00>, <Element physical-interface at 0x7fdceab7fe40>, <Element logical-interface at 0x7fdceab7fe80>, <Element physical-interface at 0x7fdceab7fec0>, <Element physical-interface at 0x7fdceab7ff00>, <Element physical-interface at 0x7fdceab7ff40>, <Element physical-interface at 0x7fdceab7ff80>, <Element logical-interface at 0x7fdceab7ffc0>, <Element physical-interface at 0x7fdceab85040>, <Element logical-interface at 0x7fdceab85080>, <Element logical-interface at 0x7fdceab850c0>, <Element logical-interface at 0x7fdceab85100>, <Element physical-interface at 0x7fdceab85140>, <Element logical-interface at 0x7fdceab85180>, <Element logical-interface at 0x7fdceab851c0>, <Element physical-interface at 0x7fdceab85200>, <Element physical-interface at 0x7fdceab85240>, <Element physical-interface at 0x7fdceab85280>, <Element physical-interface at 0x7fdceab852c0>, <Element physical-interface at 0x7fdceab85300>, <Element physical-interface at 0x7fdceab85340>, <Element physical-interface at 0x7fdceab85380>, <Element physical-interface at 0x7fdceab853c0>]
>>> 
>>> for interface_xml in rpc.xpath('//physical-interface|//physical-interface/logical-interface'):    
...     print(etree.tostring(interface_xml))
... 
b'<physical-interface><name>lc-1/0/0</name><admin-status format="Enabled">up</admin-status><oper-status>up</oper-status><local-index>146</local-index><snmp-index>511</snmp-index><generation>149</generation><if-type>Unspecified</if-type><link-level-type>Unspecified</link-level-type><mtu>0</mtu><speed>800mbps</speed><clocking>Unspecified</clocking><if-device-flags><ifdf-present/><ifdf-running/></if-device-flags><ifd-specific-config-flags><internal-flags>0x200</internal-flags></ifd-specific-config-flags><if-config-flags/><link-type>Unspecified</link-type><if-media-flags><ifmf-none/></if-media-flags><physical-information>Unspecified</physical-information><up-hold-time>0</up-hold-time><down-hold-time>0</down-hold-time><damp-half-life>0</damp-half-life><damp-max-suppress>0</damp-max-suppress><damp-reuse-level>0</damp-reuse-level><damp-suppress-level>0</damp-suppress-level><damp-suppress-state>unsuppressed</damp-suppress-state><current-physical-address>Unspecified</current-physical-address><hardware-physical-address>Unspecified</hardware-physical-address><alternate-physical-address>Unspecified</alternate-physical-address><interface-flapped seconds="0">Never</interface-flapped><statistics-cleared>Never</statistics-cleared><traffic-statistics style="verbose"><input-bytes>0</input-bytes><output-bytes>0</output-bytes><input-packets>0</input-packets><output-packets>0</output-packets><ipv6-transit-statistics><input-bytes>0</input-bytes><output-bytes>0</output-bytes><input-packets>0</input-packets><output-packets>0</output-packets></ipv6-transit-statistics></traffic-statistics><input-error-list><input-errors>0</input-errors><input-drops>0</input-drops><framing-errors>0</framing-errors><input-runts>0</input-runts><input-giants>0</input-giants><input-discards>0</input-discards><input-resource-errors>0</input-resource-errors></input-error-list><output-error-list><carrier-transitions>0</carrier-transitions><output-errors>0</output-errors><output-drops>0</output-drops><mtu-errors>0</mtu-errors><output-resource-errors>0</output-resource-errors></output-error-list><logical-interface><name>lc-1/0/0.32769</name><local-index>344</local-index><snmp-index>512</snmp-index><generation>153</generation><if-config-flags><iff-up/></if-config-flags><encapsulation>ENET2</encapsulation><policer-overhead/><logical-interface-bandwidth>0</logical-interface-bandwidth><traffic-statistics style="verbose" indent="2"><input-bytes>0</input-bytes><output-bytes>0</output-bytes><input-packets>0</input-packets><output-packets>0</output-packets></traffic-statistics><local-traffic-statistics><input-bytes>0</input-bytes><output-bytes>0</output-bytes><input-packets>0</input-packets><output-packets>0</output-packets></local-traffic-statistics><transit-traffic-statistics><input-bytes>0</input-bytes><input-bps>0</input-bps><output-bytes>0</output-bytes><output-bps>0</output-bps><input-packets>0</input-packets><input-pps>0</input-pps><output-packets>0</output-packets><output-pps>0</output-pps></transit-traffic-statistics><filter-information/><address-family><address-family-name>vpls</address-family-name><mtu>Unlimited</mtu><generation>202</generation><route-table>1</route-table><address-family-flags><ifff-is-primary/><internal-flags>0x4000000</internal-flags></address-family-flags></address-family></logical-interface></physical-interface>'
< output omitted >
>>> 
>>> import xml.dom.minidom
>>> 
>>> for interface_xml in rpc.xpath('//physical-interface|//physical-interface/logical-interface'):
...     xml_minidom = xml.dom.minidom.parseString(etree.tostring(interface_xml))
...     interface_xml_pretty = xml_minidom.toprettyxml()
...     print(interface_xml_pretty)
... 
<?xml version="1.0" ?>
<physical-interface>
        <name>lc-1/0/0</name>
< output omitted >

>>> # XPATH getting the physical interface names in case they include 'et':
>>> rpc.xpath('physical-interface[contains(name, "et-")]/name/text()')
[]
>>> # XPATH getting the physical interface names in case they include 'xe':
>>> rpc.xpath('physical-interface[contains(name, "xe-")]/name/text()')     
['xe-1/0/0', 'xe-1/0/1', 'xe-1/0/2', 'xe-1/0/3', 'xe-1/1/0', 'xe-1/1/1', 'xe-1/1/2', 'xe-1/1/3', 'xe-1/2/0', 'xe-1/2/1', 'xe-1/2/2', 'xe-1/2/3', 'xe-1/3/0', 'xe-1/3/1', 'xe-1/3/2', 'xe-1/3/3']
>>> 
>>> 
>>> # Using regular expresions in lxml:
>>> ns = {"re": "http://exslt.org/regular-expressions"}
>>> # RE to get 10G: 
>>> rpc.xpath('physical-interface[re:match(name, "xe")]/name/text()', namespaces=ns)   
['xe-1/0/0', 'xe-1/0/1', 'xe-1/0/2', 'xe-1/0/3', 'xe-1/1/0', 'xe-1/1/1', 'xe-1/1/2', 'xe-1/1/3', 'xe-1/2/0', 'xe-1/2/1', 'xe-1/2/2', 'xe-1/2/3', 'xe-1/3/0', 'xe-1/3/1', 'xe-1/3/2', 'xe-1/3/3']
>>>
>>> rpc.xpath('physical-interface[re:match(name, "XE-[1]")]/name/text()', namespaces=ns)    
[]
>>> rpc.xpath('physical-interface[re:match(name, "XE-[1,2]", "i")]/name/text()', namespaces=ns)  
['xe-1/0/0', 'xe-1/0/1', 'xe-1/0/2', 'xe-1/0/3', 'xe-1/1/0', 'xe-1/1/1', 'xe-1/1/2', 'xe-1/1/3', 'xe-1/2/0', 'xe-1/2/1', 'xe-1/2/2', 'xe-1/2/3', 'xe-1/3/0', 'xe-1/3/1', 'xe-1/3/2', 'xe-1/3/3']
>>> # XPATH to get all interfaces, physical as well as logical:
>>> all_interfaces = rpc.xpath('//physical-interface|//physical-interface/logical-interface')
>>> 
>>> # Now we can iterate `all_interfaces` to get the name of the interfaces using the `find` method:
>>> 
>>> for interface in all_interfaces:
...     # extract the name using find:
...     interface.find('./name').text if interface.find('./name') is not None else None
... 
'lc-1/0/0'
'lc-1/0/0.32769'
'pfe-1/0/0'
'pfe-1/0/0.16383'
'pfh-1/0/0'
'pfh-1/0/0.16383'
'pfh-1/0/0.16384'
'xe-1/0/0'
'xe-1/0/0.0'
'xe-1/0/1'
'xe-1/0/1.0'
< output omitted >
>>> # Alternatively, we use an XPATH to accomplish the same thing again:
>>> for interface in all_interfaces:
...     # extract the name using XPATH:
...     interface.xpath('./name/text()') 
... 
['lc-1/0/0']
['lc-1/0/0.32769']
['pfe-1/0/0']
['pfe-1/0/0.16383']
['pfh-1/0/0']
['pfh-1/0/0.16383']
['pfh-1/0/0.16384']
['xe-1/0/0']
['xe-1/0/0.0']
['xe-1/0/1']
['xe-1/0/1.0']
< output omitted >
>>> 
>>> # We can also inspect the text of all the child nodes, just to see what is on offer:
>>> for interface in all_interfaces:
...     interface.xpath('child::*/text()')
...     interface.xpath('child::*/text()')
... 

< output omitted >
['lo0', 'up', 'up', '6', '6', '7', 'HELLO WORLD', 'Loopback', 'Unspecified', 'Unlimited', 'Unspecified', 'Unspecified', 'Unspecified', 'Unspecified', '0', '0', '0', '0', '0', '0', 'unsuppressed', 'Unspecified', 'Unspecified', 'Unspecified', 'Never', 'Never']
['lo0', 'up', 'up', '6', '6', '7', 'HELLO WORLD', 'Loopback', 'Unspecified', 'Unlimited', 'Unspecified', 'Unspecified', 'Unspecified', 'Unspecified', '0', '0', '0', '0', '0', '0', 'unsuppressed', 'Unspecified', 'Unspecified', 'Unspecified', 'Never', 'Never']
< output omitted >
>>> 
>>> # Sometimes, the atributes offer more interested data. In order to access attributes, we can use the following:
>>> for interface in all_interfaces:
...     interface.find('./interface-flapped').attrib['seconds'] if interface.find('./interface-flapped') is not None else None
... 
'0'
'0'
'0'
'42636301'
'42636301'
< output omitted >
>>> # Safely accessing attributes of can also be done using the Python built-in `getattr`:
>>> all_interfaces = rpc.xpath('//physical-interface|//physical-interface/logical-interface')
>>> for interface in all_interfaces:
...     getattr(interface.find('./name'), 'text' , '')
...     getattr(interface.find('./description'), 'text' , '')    
...     getattr(interface.find('./oper-status'), 'text', None)
...     getattr(interface.find('./mtu'), 'text', None)
...     interface.find('./interface-flapped').attrib['seconds'] if interface.find('./interface-flapped') is not None else None    
...     getattr(interface.find('.//input-pps'), 'text' , '')
...     getattr(interface.find('.//output-pps'), 'text' , '')
... 
'lc-1/0/0'
''
'up'
'0'
'0'
'0'
'0'
< output omitted >
>>> # Short example where we put the collected information into a dictionary:
>>> 
>>> from collections import OrderedDict # ensure the ordering of the dict key/values
>>> 
>>> all_interfaces = rpc.xpath('//physical-interface|//physical-interface/logical-interface')
>>> interfaces_list_of_dict = []
>>> 
>>> for interface in all_interfaces:
...     interfaces_list_of_dict.append(
...         OrderedDict({
...         'interface-name' : getattr(interface.find('./name'), 'text' , ''),
...         'interface-description' : getattr(interface.find('./description'), 'text' , ''),
...         'interface-status' : getattr(interface.find('./oper-status'), 'text', None),
...         'interface-mtu' : getattr(interface.find('./mtu'), 'text', None),
...         'interface-last-flapped' : interface.find('./interface-flapped').attrib['seconds'] if interface.find('./interface-flapped') is not None else None,
...         'interface-input-pps' : getattr(interface.find('.//input-pps'), 'text' , ''),
...         'interface-output-pps' : getattr(interface.find('.//output-pps'), 'text' , ''),
... 
...     })
...     )
... 
>>> from json import dumps
>>> print(dumps(interfaces_list_of_dict, indent=4))
[
< output omitted >
    {
        "interface-name": "xe-1/0/0",
        "interface-description": "LAB",
        "interface-status": "down",
        "interface-mtu": "9192",
        "interface-last-flapped": "42636301",
        "interface-input-pps": "0",
        "interface-output-pps": "0"
    },
    {
        "interface-name": "xe-1/0/0.0",
        "interface-description": "",
        "interface-status": null,
        "interface-mtu": null,
        "interface-last-flapped": null,
        "interface-input-pps": "0",
        "interface-output-pps": "0"
    },
< output omitted >
    {
        "interface-name": "ae22",
        "interface-description": "LAB",
        "interface-status": "up",
        "interface-mtu": "9176",
        "interface-last-flapped": "23337585",
        "interface-input-pps": "177",
        "interface-output-pps": "589"
    },
    {
        "interface-name": "ae22.0",
        "interface-description": "",
        "interface-status": null,
        "interface-mtu": null,
        "interface-last-flapped": null,
        "interface-input-pps": "177",
        "interface-output-pps": "570"
    },
< output omitted >
]
>>> 
>>> # There are a lot of 'uninteresting' interfaces that Juniper has for internal use. Filtering them out is easy:
>>> 
>>> 
>>> uninteresting = ["jsrv", "local", "igb", "ixlv", "bme", "32768", "16384", "32767"]
>>> 
>>> for interface in all_interfaces:
...     if any(s in getattr(interface.find('./name'), 'text' , '') for s in uninteresting):
...         continue
...     if len(interface.xpath('./address-family/interface-address/ifa-local/text()')):
...         getattr(interface.find('./name'), 'text' , '')
...         interface.xpath('./address-family/interface-address/ifa-local/text()')
... 
'ae0.0'
['168.1.1.0', '2001:db8::1300:1::4', 'fe80::42a6:77ff:fec2:2bc0']
'ae1.0'
['10.0.1.222']
'ae2.1'
< output omitted >
