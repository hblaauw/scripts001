#! /usr/bin/python3
# -*- coding: utf-8 -*-

import string
import psycopg2
import sys



con = None
try:
    file = '/var/log/nginx/access.log.1'
    fp = open(file, 'r')
    lees = fp.readlines()
    
    tel=1
    for a in lees:
         lijst=(str.split(a))
         l_ip = lijst[0]
         l_datum = lijst[3] + lijst[4]
         l_tekst=  lijst[10:]
         print (l_ip)
         print (l_datum)
         print (l_tekst)
         print "--"

    
    
finally:
        fp.close()
