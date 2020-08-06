#!/usr/bin/env python3

import re

# vérifie si il y a bien un nom de domaine
def tld_check(domain):
    check = re.findall("^([aA-zZ\-]*\.)*[aA-zZ]*", domain)
    return check != None and len(check) == 1
