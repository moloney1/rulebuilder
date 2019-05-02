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
match = rule.create_match("tcp")
match.dport = "80"