# multidig
Outil à l'invite de commande qui va effectuer une requête dns équivalente à la commande `dig` mais sur une liste de DNS passé en paramètre.

Par défaut, il utilise un DNS de google et un DNS de Cloudflare.
Des listes de DNS sont donnés dans le dossier `publicdnslist/`.

## Installation

```
git clone https://github.com/darcosion/multidig
cd multidig
python3 install -r requirements.txt
```

Cet outil utilise le module pythondns, c'est son unique dépendance.

## Commande 

```
# python3 multidig.py
Multisig par darcosion (https://github.com/darcosion/multidig)
usage: multidig.py [-h] [-t TYPE] [-frd FILE_RESOLVER_DNS] DOMAIN
multidig.py: error: the following arguments are required: DOMAIN
```

### Exemple d'utilisation : 

```
python3 multidig.py  -t TXT exxonmobil.com -frd publicdnslist/valid.txt
Multisig par darcosion (https://github.com/darcosion/multidig)
Liste des éléments sortis par les resolvers :
"docusign=288e0f5d-82f0-41da-a809-b3853080b9e7"
"cdddc66bd5"
"docusign=0db93793-f066-48ad-a763-c88fa025923c"
"DFIsoLViNPhwDWZCUWqluopqvYHT7T9Qrzv3McBBo3DzVYDmzJKck2QncSxvGgYXzef/g0giB4fPLUXoecdn5Q=="
"google-site-verification=ddlsR_-L1AT1PtAHzRfH6WC0ECzBrO2Wzz5PlcXNIbI"
"a9c197eaa82716cf662277e4375eea166d308b1a9a859d0d826fd637b83cb9af"
"v=spf1 a:dalmxp131.exxonmobil.com a:dalmxp132.exxonmobil.com a:hoemxp131.exxonmobil.com a:hoemxp132.exxonmobil.com ip4:158.26.24.0/28 -all"
"wygyqnztmhbjsnjt2y2zztqq7nj2wgdf"
"MS=ms31734318"
"oTxRsE0X3S4ef9p6sAhaFZ1H8JftdlRLirSZ47YMMgXSP8PJ6NpvuZCCoqKQ81Kaf/IShkobCSXIZYs3wtQ/gw=="
"MS=ms23383015"
"nintex.5e12ed3c8068360f2be6150b"
"Dynatrace-site-verification=03db2a82-9403-420d-ae3b-39b639f1f585__531a1g72s0cpgs83bs9ar7h477"
"onetrust-domain-verification=e7ab282580e64c2aa3d73b6e3ecfe8c9"
```
