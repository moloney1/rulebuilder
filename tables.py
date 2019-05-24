#!/usr/bin/env python
import iptc

def find_probability(n_rules, i_cur_rule):
    return str(1 / (n_rules - i_cur_rule + 1))

def add_stat_random_match(rule, n_rules, i_cur_rule):
    stat_match = rule.create_match("statistic")
    stat_match.mode = "random"
    stat_match.probability = find_probability(n_rules,i_cur_rule)

def add_stat_roundrobin_match(rule, n_rules, i_cur_rule):
    every = n_rules - i_cur_rule
    if every != 0:
        stat_match = rule.create_match("statistic")
        stat_match .mode = "nth"
        stat_match.every = str(every)
        stat_match.packet = "0"

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

# match tcp traffic onto port 2002 (for now)
dport_match = rule.create_match("tcp")
dport_match.dport = "2002"

# beginning statistic match
stat_match = rule.create_match("statistic")
stat_match.mode = "random"
stat_match.probability = find_probability(2, 1)

rule.target = iptc.Target(rule, "REDIRECT")
rule.target.to_ports = "2000"

# try to insert rule into prerouting chain of nat table
table = iptc.Table(iptc.Table.NAT)
pre_chain = iptc.Chain(table, "PREROUTING")
#pre_chain.insert_rule(rule, position=0)

