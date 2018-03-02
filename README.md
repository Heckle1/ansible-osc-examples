# Introduction
Some usefull Ansible receip for Outscale

# Outscale Endpoints
If you want to work with Outscale please follow those rules:


1. To be able to use Outscale you should us both "region" and "ec2_url" in your Ansible role

``` yaml
    region:           "{{ osc_region }}"
    ec2_url:          "{{ fcu_url }}"
```


2. Use Ansible for Outscale
   * https://github.com/Heckle1/ansible
   * Difference with official Ansible is this https://github.com/Heckle1/ansible/commit/cc010035e55a58211c5b8f50915ca9e4644505e8


3. Use update_endpoints.py to inject Outscale endpoint for FCU/EC2 service
   This program will update the endpoints.json file used within your current environment (because of course you are using virtual environment) with Outscale endpoints

	``` python
	(work_env)$>python update_endpoints.py
	INFO fcu.us-east-2.outscale.com updated !
	INFO fcu.us-east-2.outscale.com updated !
	INFO fcu.us-west-1.outscale.com updated !
	INFO /<YOUR_ENV>/lib64/python3.5/site-packages/boto/endpoints.json update with succes
	INFO Done.
	```


# Hint
If you have multiple Ansible installed, you may have to add -extra-vars to your ansible-playbook command
``` bash
ansible-playbook --extra-vars "ansible_python_interpreter=/<PATH_TO_ENV>/bin/python"
```

# Note
Python 3.5+
