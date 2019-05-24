import iptc
from tables import find_probability

protocol = "tcp"
table = iptc.Table(iptc.Table.NAT)
pre_chain = iptc.Chain(table, "PREROUTING")

class RuleBuilder:
	def __init__(self, dport, to_ports):
		self.dport = dport
		self.to_ports = to_ports        
		self.num_rules = len(self.to_ports)
		self.rules = [] # hold all rules

		print(f'Route {self.dport} to {self.to_ports} - {self.num_rules} rules')

	def set_protocol(self):
		print(protocol)
		pass

	def init_rules(self):
		for i in range(0, len(self.to_ports)):
			rule = iptc.Rule()
			rule.protocol = protocol
			
	def commit_all(self):
		for rule in rules:
			pre_chain.insert_rule(rule, position=0)

r = RuleBuilder(12, [4, 5, 6, 7])
r.init_rules()
r.set_protocol()
