#!/usr/bin/env python3
import os
import pubchempy as pcp
import argparse

from mychemcache import ChemCache

# python3 -m venv ~/genex
# source ~/genex/bin/activate
# pip install -U mol2chemfigPy3
# pip install pubchempy
# pip install diskcache

global_cache=ChemCache()

global args
args=None

def mol2chemfig0(chemid,m2copts="-z -y delete"):
    if (args and (args.m2c_opt is not None)):
        m2copts=args.m2c_opt
    cmd = "mol2chemfig %s -i pubchem %s" % (m2copts,chemid)
    print(cmd)
    chemfig=global_cache.get(cmd)
    if (chemfig is not None):
        print ("Cache hit! - %s" % (cmd))
        return chemfig
    global_cache.set(cmd, os.popen(cmd).read())
    return os.popen(cmd).read()

# FIXME: fast hack for stripping
def mol2chemfig(chemid):
    return mol2chemfig0(chemid).strip()

# FIXME: cnl should be stored in full in cache
# indexed by chemid
# Name index should return cid only

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

def find_substance_name_from_id(chemid):
    cnl=global_cache.get(chemid)
    if (cnl is not None):
        print ("Cache hit! - %s" % (chemid))
        return cnl
    cnl=pcp.get_compounds(chemid, "cid")
    if (len(cnl) == 0):
        cnl = pcp.get_substances(chemid, "cid")
        print (cnl)
        raise ValueError("No match for %s" % (chemid))
    if (len(cnl) == 1):
        global_cache.set(chemid, cnl[0].name)
        return cnl[0].name
    for cid in cnl:
        print (cid, mol2chemfig(cid))
    raise ValueError("No unique match for %s" % (chemid))

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


def full_latex_from_id(chemid):
    pass


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Convertir un nom français en chemfig.")
    parser.add_argument("--from-fr-name", type=str, default=None, required=False, help="Nom français à traiter.")
    parser.add_argument("--m2c-opt", type=str, default=None, required=False, help="Options pour mol2chemfig.")
    args = parser.parse_args()

    print(mol2chemfig_from_frenchname(args.from_fr_name))
    
    #print (mol2chemfig(142755607))
    #print (find_substance_id_from_name("2-acetoxy benzoic acid"))
    #print (mol2chemfig_from_name("2-acetoxy benzoic acid"))
    #mol2chemfig -w -z -y delete -i pubchem 142755607

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
