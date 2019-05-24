import iptc
from tables import add_stat_random_match

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
		self.stat_type = "random"

		print(f'Route {self.dport} to {self.to_ports} - {self.num_rules} rules')

	def set_protocol(self):
		print(self.protocol)
		pass

	def build_rules(self):
		for i in range(0, len(self.to_ports)):
			rule = iptc.Rule()
			rule.protocol = self.protocol

			dport_match = rule.create_match(self.protocol)
			dport_match.dport = str(self.dport)

			rule.target = iptc.Target(rule, "REDIRECT")
			rule.target.to_ports = str(self.to_ports[i])
			
			if self.stat_type == "random":
				add_stat_random_match(rule, self.num_rules, i + 1)
			
			# prepend so that rules are executed in correct order later
			self.rules.insert(0, rule)
			
	def commit_all(self):
		for rule in self.rules:
			self.chain.insert_rule(rule, position=0)

	def set_stat_type(self, stat_type):
		self.stat_type = stat_type
 	
r = RuleBuilder(2002, [2000, 2001, 2003])
r.build_rules()
r.commit_all()
