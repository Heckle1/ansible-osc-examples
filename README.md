# Introduction
Some usefull Ansible receip for Outscale

# Outscale Endpoints
Ansible works with boto which uses boto/endpoints.json file.

1.
To be able to use Outscale you should us both "region" and "ec2_url" in your Ansible role

``` yaml
    region:           "{{ osc_region }}"
    ec2_url:          "{{ fcu_url }}"
```

2.
Use update_endpoints.py to inject Outscale endpoint for FCU/EC2 service:
- eu-west-2
- us-east-2
- us-west-1

# Note
Python 3.5+
