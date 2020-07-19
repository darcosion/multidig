#!/usr/bin/env python3

import argparse
from dns import resolver as dnsresolver

#import locaux
import utils

print("Multisig par darcosion (https://github.com/darcosion/multidig)")

# paramètres de CLI
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str,
                    help="type of DNS request (MX, A, CNAME, etc...)")
parser.add_argument("DOMAIN", type=str,
                    help="domain to investigate")
parser.add_argument('-frd', '--file-resolver-dns', type=str,
                    help="File containing list of DNS resolver to test")

args = parser.parse_args()
print(args)

dnstypequery= ''
if(args.type):
    dnstypequery=args.type
# on change de resolver dns : https://dnspython.readthedocs.io/en/stable/resolver-override.html?highlight=resolver

resolver.override_system_resolver('5.132.191.104')

response = dnsresolver.query(args.DOMAIN, dnstypequery)

for rdata in response:
    print(rdata)
    pass
