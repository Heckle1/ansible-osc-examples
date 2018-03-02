"""
Override boto/endpoints.json within your environment with Outscale endpoints
"""

import boto
import json
import logging
import os
import sys

my_logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
my_logger.addHandler(out_hdlr)
my_logger.setLevel(logging.INFO)

outscale_endpoints = {
    'ec2': {
        'eu-west-2': 'fcu.eu-west-2.outscale.com',
        'us-east-2': 'fcu.us-east-2.outscale.com',
        'us-west-1': 'fcu.us-east-2.outscale.com'
    }
}


def find_boto_endpoints():
    """
    Find the boto endpoints.json file based on boto module
    :return: path th endpoints.json file
    :rtype: str
    """
    path = os.path.dirname(boto.__file__)
    return '{0}/endpoints.json'.format(path)


def inject_outscale_endpoints(endpoints_path):
    """
    Override boto/endpoints.json with Outscale endpoints
    :param endpoints_path: file path to endpoints.json file
    :type endpoints_path: str
    """
    with open(endpoints_path, 'r') as fi:
        boto_endpoints = json.load(fi)
    for service, endpoints in outscale_endpoints.items():
        for region_name, endpoint_url in endpoints.items():
            try:
                if region_name in boto_endpoints['partitions'][0]['services'][service]['endpoints']:
                    boto_endpoints['partitions'][0]['services'][service]['endpoints'][region_name] = {'sslCommonName': endpoint_url}
                else:
                    boto_endpoints['partitions'][0]['services'][service]['endpoints'] = {region_name: {'sslCommonName': endpoint_url}}
            except KeyError as err:
                my_logger.warning('Can not inject {0}. Reason: {1}'.format(endpoint_url, err))
            else:
                my_logger.info('{0} updated !'.format(endpoint_url))
    with open(endpoints_path, 'w') as fi:
        fi.write(json.dumps(boto_endpoints))
    my_logger.info('{0} update with succes'.format(endpoints_path))
    my_logger.info('Done.')


if __name__ == '__main__':
    endpoints_path = find_boto_endpoints()
    inject_outscale_endpoints(endpoints_path)
