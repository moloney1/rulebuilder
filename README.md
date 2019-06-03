# RuleBuilder

Not the most creative title :sleeping: 

For my FYP I needed to spin up and throw away a bunch of Docker containers while all traffic on port 22 was being routed to one of the live containers at random. I implemented something pretty hacky at the time to get the job done. Now that it's all over, I decided to build the package I wish I had at the time. 

## Modules

The `rule_builder.py` module contains a class that takes a single "dport" (e.g. 22) and a list of "to-ports" (e.g. [2000, 2001, 2002]) and builds up iptables rules to perform random routing. The rules can have their attributes modified using instance setters before calling `.commit_all()` on the RuleBuilder object.

`tables.py` is a remnant of early development, but it contains some helper functions used by `rule_builder`.

`docker_route.py` queries for running docker containers and naively assumes you want to include all of them in a rule build. It then commits rules automatically. 

`scripts/restore.sh` - run this to flush all the tables the modules modify. Dangerous if you have other applications relying on iptables...

## TODO

* Design a tidier command line interface
* Possibly add interop with docker-compose :thinking:
* Think of a better title
