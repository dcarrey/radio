#!/usr/bin/python

# coding: utf-8

#============================================================
#= Listen radio with mplayer / Ecouter la radio avec mplayer
#=
#= author : Alix Boc
#= date : mars 2015
#============================================================

import json
import os
import sys

with open('radios.json') as data_file:    
    data = json.load(data_file)
plusGrandeCle = max(data.keys(), key=len)

if len (sys.argv) != 2:
    print "usage : " , sys.argv[0] , "radio"

    print "\nListe des radios:"

    for key in data.keys():
        print "%-*s : %s" % (len(plusGrandeCle), key, data[key])

    sys.exit(0)

os.system("mplayer " + data[sys.argv[1]])

