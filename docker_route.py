import docker
from rule_builder import RuleBuilder

to_ports = []
client = docker.from_env()
containers = client.containers.list()

for container in containers:
	port_vals = list(container.attrs['NetworkSettings']['Ports'].values())[0]
	to_ports.append((port_vals[0]['HostPort']))

r = RuleBuilder(2002, to_ports)
r.build_rules()
r.commit_all()	



