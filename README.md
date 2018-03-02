# Introduction
Some usefull Ansible receip for Outscale

# Outscale Endpoints
If you want to work with Outscale please respect those 2 following rules


1. To be able to use Outscale you should us both "region" and "ec2_url" in your Ansible role

``` yaml
    region:           "{{ osc_region }}"
    ec2_url:          "{{ fcu_url }}"
```

2. Use update_endpoints.py to inject Outscale endpoint for FCU/EC2 service
This program will update the endpoints.json file used within your current environment (because of course you are using virtual environment) with Outscale endpoints
- eu-west-2 / fcu.eu-west-2.outscale.com
- us-east-2 / fcu.us-east-2.outscale.com
- us-west-1 / fcu.us-west-1.outscale.com

# Hint
If you have multiple Ansible installed, you may have to add -extra-vars to your ansible-playbook command
``` bash
ansible-playbook --extra-vars "ansible_python_interpreter=/<PATH_TO_ENV>/bin/python"
```

# Note
Python 3.5+
