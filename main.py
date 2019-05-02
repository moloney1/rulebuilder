#!/usr/bin/env python
import iptc

# access the NAT table
table = iptc.Table(iptc.Table.NAT)

# create "TEST" chain in nat table
'''
chain = table.create_chain("TEST")
chain = iptc.Chain(table, "TEST")
print(f'test chain: {chain.name}')
'''

# print table name
print(f'Table: {table.name}')

# list names of chains in nat table
for chain in table.chains:
    print(f'Chain: {chain.name}')

# begin building a rule
rule = iptc.Rule()

rule.protocol = "tcp"
rule.target = iptc.Target(rule, "ACCEPT")
match = iptc.Match(rule, "state")
chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
match.state = "RELATED,ESTABLISHED"
rule.add_match(match)
chain.insert_rule(rule)

# trying to build up following rule
rule = iptc.Rule()
rule.protocol = "tcp"
rule.src = "0.0.0.0/0"
# rule.dst = "0.0.0.0/0" # seems src + dst "anywhere" is implicit?

rule.dport = "22" # does this do anything??
# match = rule.create_match("tcp")
# match.dport = "22"

rule.target = iptc.Target(rule, "REDIRECT")
rule.target.set_parameter("to-ports", "2000")

# iptables -t nat -I PREROUTING --src 0/0 --dst 0/0 -p tcp --dport 22 -j REDIRECT --to-ports 4000

# try to insert rule into prerouting chain of nat table
table = iptc.Table(iptc.Table.NAT)
pre_chain = iptc.Chain(table, "PREROUTING")
pre_chain.insert_rule(rule, position=0)