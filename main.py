#!/usr/bin/env python
import iptc

# access the NAT table
table = iptc.Table(iptc.Table.NAT)

# print table name
print(f'Table: {table.name}')

# list names of chains in nat table
for chain in table.chains:
    print(f'Chain: {chain.name}')

# begin building a rule
rule = iptc.Rule()

'''
    trying to build up following rule:
        iptables -t nat -I PREROUTING --src 0/0 --dst 0/0 
        -p tcp --dport 22 -j REDIRECT --to-ports 4000
'''
rule = iptc.Rule()
rule.protocol = "tcp"

# seems src, dst = anywhere is implicit, but anyway...
rule.src = "0.0.0.0/0"
rule.dst = "0.0.0.0/0" 

# library doesn't seem to support "-p tcp --dport", so...
match = rule.create_match("tcp")
match.dport = "2002"

rule.target = iptc.Target(rule, "REDIRECT")
rule.target.to_ports = "2000"

# try to insert rule into prerouting chain of nat table
table = iptc.Table(iptc.Table.NAT)
pre_chain = iptc.Chain(table, "PREROUTING")
pre_chain.insert_rule(rule, position=0)