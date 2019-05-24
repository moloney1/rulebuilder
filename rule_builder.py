import iptc
from tables import find_probability

protocol = "tcp"
table = iptc.Table(iptc.Table.NAT)
chain = iptc.Chain(table, "PREROUTING")

class RuleBuilder:
	def __init__(self, dport, to_ports):
		self.dport = dport
		self.to_ports = to_ports        
		self.num_rules = len(self.to_ports)
		self.rules = [] # hold all rules

		self.protocol = "tcp"
		self.table = iptc.Table(iptc.Table.NAT)
		self.chain = iptc.Chain(self.table, "PREROUTING")

		print(f'Route {self.dport} to {self.to_ports} - {self.num_rules} rules')

	def set_protocol(self):
		print(self.protocol)
		pass

	def init_rules(self):
		for i in range(0, len(self.to_ports)):
			rule = iptc.Rule()
			rule.protocol = self.protocol

			dport_match = rule.create_match(self.protocol)
			dport_match.dport = str(self.dport)

			rule.target = iptc.Target(rule, "REDIRECT")
			rule.target.to_ports = str(self.to_ports[i])
			
			self.rules.append(rule)		
			
	def commit_all(self):
		for rule in self.rules:
			self.chain.insert_rule(rule, position=0)

r = RuleBuilder(2002, [2000])
r.init_rules()
r.commit_all()
