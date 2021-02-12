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
[root@said /]# python -i /var/tmp/example.py admin vmx-02
Password: 
>>> 
>>> ns = {"re": "http://exslt.org/regular-expressions"}
>>> 
>>> # RE to get 100G:
>>> rpc.xpath('physical-interface[re:match(name, "et")]/name/text()', namespaces=ns) 
['et-0/0/0', 'et-0/0/1', 'et-0/0/2', 'et-0/0/3', 'et-0/0/5', 'et-0/0/6', 'et-0/0/7', 'et-0/0/8', 'et-0/0/10', 'et-0/0/11', 'et-0/0/12', 'et-0/0/13', 'et-0/0/14', 'et-0/0/15', 'et-0/0/16', 'et-0/0/17', 'et-0/0/18', 'et-0/0/20', 'et-0/0/21', 'et-0/0/22', 'et-0/0/25', 'et-0/0/26', 'et-0/0/27', 'et-0/0/28', 'et-1/0/0', 'et-1/0/1', 'et-1/0/2', 'et-1/0/3', 'et-1/0/5', 'et-1/0/6', 'et-1/0/7', 'et-1/0/8', 'et-1/0/10', 'et-1/0/11', 'et-1/0/12', 'et-1/0/13', 'et-1/0/15', 'et-1/0/16', 'et-1/0/17', 'et-1/0/18', 'et-1/0/20', 'et-1/0/21', 'et-1/0/22', 'et-1/0/25', 'et-1/0/26', 'et-1/0/27', 'et-1/0/28', 'et-2/0/1', 'et-2/0/5', 'et-2/0/6', 'et-2/0/9', 'et-2/0/11', 'et-2/0/12', 'et-2/0/14', 'et-2/0/16', 'et-2/0/21', 'et-2/0/26', 'et-2/0/28', 'et-3/0/1', 'et-3/0/5', 'et-3/0/6', 'et-3/0/9', 'et-3/0/11', 'et-3/0/12', 'et-3/0/16', 'et-3/0/21', 'et-3/0/26', 'et-3/0/28']
>>> 
>>> # RE to get 100G on linecard position 1 and 2:
>>> rpc.xpath('physical-interface[re:match(name, "et-[1,2]")]/name/text()', namespaces=ns)
['et-1/0/0', 'et-1/0/1', 'et-1/0/2', 'et-1/0/3', 'et-1/0/5', 'et-1/0/6', 'et-1/0/7', 'et-1/0/8', 'et-1/0/10', 'et-1/0/11', 'et-1/0/12', 'et-1/0/13', 'et-1/0/15', 'et-1/0/16', 'et-1/0/17', 'et-1/0/18', 'et-1/0/20', 'et-1/0/21', 'et-1/0/22', 'et-1/0/25', 'et-1/0/26', 'et-1/0/27', 'et-1/0/28', 'et-2/0/1', 'et-2/0/5', 'et-2/0/6', 'et-2/0/9', 'et-2/0/11', 'et-2/0/12', 'et-2/0/14', 'et-2/0/16', 'et-2/0/21', 'et-2/0/26', 'et-2/0/28']
>>> 
>>> # RE to get 100G on linecard position 1 and 2 while ignoring upper and lower case:
>>> rpc.xpath('physical-interface[re:match(name, "ET-[1,2]", "i")]/name/text()', namespaces=ns)
['et-1/0/0', 'et-1/0/1', 'et-1/0/2', 'et-1/0/3', 'et-1/0/5', 'et-1/0/6', 'et-1/0/7', 'et-1/0/8', 'et-1/0/10', 'et-1/0/11', 'et-1/0/12', 'et-1/0/13', 'et-1/0/15', 'et-1/0/16', 'et-1/0/17', 'et-1/0/18', 'et-1/0/20', 'et-1/0/21', 'et-1/0/22', 'et-1/0/25', 'et-1/0/26', 'et-1/0/27', 'et-1/0/28', 'et-2/0/1', 'et-2/0/5', 'et-2/0/6', 'et-2/0/9', 'et-2/0/11', 'et-2/0/12', 'et-2/0/14', 'et-2/0/16', 'et-2/0/21', 'et-2/0/26', 'et-2/0/28']
>>> # RE to filter to AE's:
>>> rpc.xpath('physical-interface[re:match(name, "ae10" )]/name/text()', namespaces=ns) 
['ae101', 'ae102', 'ae103', 'ae104', 'ae105', 'ae106', 'ae107', 'ae108']
>>> rpc.xpath('physical-interface[re:match(name, "ae10[6-7]" )]/name/text()', namespaces=ns)
['ae106', 'ae107']
