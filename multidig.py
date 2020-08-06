#!/usr/bin/env python3

import argparse
from dns import resolver as dnsresolver

#import locaux
import utils

print("Multidig par darcosion (https://github.com/darcosion/multidig)")

# paramètres du CLI
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str,
                    help="type of DNS request (MX, A, CNAME, etc...)")
parser.add_argument("DOMAIN", type=str,
                    help="domain to investigate")
parser.add_argument('-frd', '--file-resolver-dns', type=str,
                    help="file containing list of DNS resolver to test")

args = parser.parse_args()
#print(args)

dnstypequery= ''
if(args.type):
    dnstypequery=args.type

listresolver = ['8.8.8.8', '1.1.1.1']
# on change de resolver dns : https://dnspython.readthedocs.io/en/stable/resolver-override.html?highlight=resolver
if(args.file_resolver_dns):
	f = open(args.file_resolver_dns)
	listresolver = f.read().strip('\n')
	f.close()

sortie = set()
for i in listresolver:
	dnsresolver.override_system_resolver(i)
	
	response = dnsresolver.query(args.DOMAIN, dnstypequery)
	
	for rdata in response:
		sortie.add(rdata)
		#print(type(rdata))
		#print(str(rdata))
		pass

print("Liste des éléments sortis par les resolvers : ")
print('\n'.join([str(elem) for elem in sortie]))
