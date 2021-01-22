# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:16:19 2020

@author: Zayou
"""


import sqlite3
conn = sqlite3.connect ( 'database.db' )
print ("Base de données ouverte avec succès")
conn.execute ( 'CREATE TABLE etudiant (nom TEXT, addr TEXT, pin TEXT)' )
print ("Table créée avec succès")


#    cur = con.cursor()
#    cur.execute("INSERT INTO etudiant (nom,addr,pin) VALUES (?,?,?)", (" John Doe"," 122 rue paul armangot","123"))
#    con.commit() 
#con.close()