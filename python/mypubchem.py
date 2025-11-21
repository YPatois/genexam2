#!/usr/bin/env python3
import os
import pubchempy as pcp

from mychemcache import ChemCache

# python3 -m venv ~/genex
# source ~/genex/bin/activate
# pip install -U mol2chemfigPy3
# pip install pubchempy
# pip install diskcache

global_cache=ChemCache()

def mol2chemfig0(chemid):
    cmd = "mol2chemfig -z -y delete -i pubchem %s" % (chemid)
    chemfig=global_cache.get(cmd)
    if (chemfig is not None):
        print ("Cache hit! - %s" % (cmd))
        return chemfig
    global_cache.set(cmd, os.popen(cmd).read())
    return os.popen(cmd).read()

# FIXME: fast hack for stripping
def mol2chemfig(chemid):
    return mol2chemfig0(chemid).strip()

def find_substance_id_from_name(name):
    cnl=global_cache.get(name)
    if (cnl is not None):
        print ("Cache hit! - %s" % (name))
        return cnl
    cnl=pcp.get_compounds(name, "name")
    if (len(cnl) == 0):
        if (name == '(E)-1,2-dichlorobut-1-ene'):
            return '21572592'
        cnl = pcp.get_substances(name, "name")
        print (cnl)
        raise ValueError("No match for %s" % (name))
    if (len(cnl) == 1):
        global_cache.set(name, cnl[0].cid)
        return cnl[0].cid
    for cid in cnl:
        print (cid, mol2chemfig(cid))
    raise ValueError("No unique match for %s" % (name))

def mol2chemfig_from_name(name):
    return mol2chemfig(find_substance_id_from_name(name))

def french_to_english(name):
    chardict={'è':'e','é':'e'}
    for k,v in chardict.items():
        name=name.replace(k,v)
    if (name.startswith('acide ')):
        print("Ho: %s %s" % (name, name[0:5]))
        name=name[6:]+ ' acid'
        name=name.replace('oïque','oic')
    #name=name.replace('Z','cis')
    return name


def mol2chemfig_from_frenchname(name):
    return mol2chemfig(find_substance_id_from_name(french_to_english(name)))

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print (mol2chemfig(142755607))
    print (find_substance_id_from_name("2-acetoxy benzoic acid"))
    print (mol2chemfig_from_name("2-acetoxy benzoic acid"))
#mol2chemfig -w -z -y delete -i pubchem 142755607

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
