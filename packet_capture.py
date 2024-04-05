
import json

json_data = '''
{
  "path_mirroring": {
    "mirror_interfaces": [
    {
     "portid": 1,
     "name": "port1"
    },
    {
     "portid": 2,
     "name": "port2"
    }
    ]
  }
}
'''
class PortMirror:
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
    def __init__(self):
        self.head = None
        self.str_arr = ""
        pass
    def load_json_config(self):
        data = json.loads(json_data)
        print(data)
        print(data["path_mirroring"]["mirror_interfaces"])
        self.str_arr = data["path_mirroring"]["mirror_interfaces"]
    def add_tail(self, node):
        cur = self.head
        if cur is None:
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    # either only fetching params, or function reflection from json
    def parse(self):
        for i in self.str_arr:
            portid = i["portid"]
            node = PortMirror.Node(portid)
            self.add_tail(node)
            print(f"port i={i}, portid={portid}")
    def dispatch(self):
        curr = self.head
        print('dispatch', curr)
        while curr:
            self.conf_vlan(curr)
            self.conf_mirror(curr, curr.next)
            curr = curr.next
    def conf_vlan(self, node):
        print("conf-vlan")
        pass
    def conf_mirror(self, cur, next):
        print("conf-mirror")
        pass
    def output(self):
        print('output for mirror')

pm = PortMirror()
pm.output()
pm.load_json_config()
pm.parse()
pm.dispatch()
