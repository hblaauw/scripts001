#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Dagelijks de inhoud van de voorgaande acces.log naar database wegschrijven.
# Versie 1.0 2020
# Git Test regeltje
# Versie 2.0 2021


import string
import psycopg2
import sys



con = None
try:
    file = '/var/log/nginx/access.log.1'
    fp = open(file, 'r')
    lees = fp.readlines()
    con = psycopg2.connect("host='themis' dbname='athena' user='logrtp' password='st03ph03r'")   
    
    cur = con.cursor()
    
    tel=1
    for a in lees:
         lijst=(str.split(a))
         l_ip = lijst[0]
         l_datum = lijst[3] + lijst[4]
         l_tekst=  lijst[10:]
#         print (l_ip)
#         print (l_datum)
#         print (l_tekst)
         cur.execute("INSERT INTO public.nginxacceslog (ip, datum, tekst) VALUES(%s, %s, %s);", (l_ip,l_datum,l_tekst))
         tel=tel+1    
         if tel == 55:
            con.commit()
            tel = 0

except psycopg2.DatabaseError as e:
    
    if con:
        con.rollback()
    
    print ('Error %s') % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.commit()
        con.close()

                
fp.close()
