# What is does
- 1 vpc
- 1 Internet Gateway
- 1 public subnet
  - 1 route table
  - 1 route 0.0.0.0 to IGW
  - 1 nat gateway
- 1 "Public" Security Group
  - 1 rule to allow port 22 from `my_ip`
- 1 private subnet
  - 1 route table
  - 1 route 0.0.0.0 to NatGW
- 1 "Private" Security Group
  - 1 rule to allow port 22 from "Public Security Group"

![Image of Infrastructure]
(http://github.osu.eu-west-2.outscale.com/ansible-vpc-basic.png)

# How to run

1. First edit the ./vars.yml file

2. Run
```bash
ansible-playbook playbook.yml -i inventory -e @vars.yml
```
