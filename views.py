# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:52:35 2020

@author: zayou noura
"""

import sqlite3
from app import app
from flask import render_template, request


@app.route('/')
def index():
    

    return render_template ('index4.html')

    
@app.route('/', methods=['POST'])


def addetudiant():
    
    nom=request.form.get('n')
    pincode=request.form.get('pin')
    add=request.form.get('addr')
    mail=request.form.get('m')
    
 
    with sqlite3.connect("database4.db") as con: 
        cur = con.cursor()
        cur.execute("INSERT OR REPLACE INTO patient (nom,pin,addr,m) VALUES (?,?,?,?)", (nom, pincode, add, mail))
     
         
        con.commit()
    con.close()
        
   # if class="header"
    
    if nom=="5" and pincode== "Bhanudjah" :
        
        return render_template ('bhan.html')
    
    elif nom=="2" and pincode=="Noura" :
        
        return render_template ('noura.html')
    
    elif nom=="3" and pincode=="Thiago" :
        
        return render_template ('Thiago.html')
    
    elif nom=="18" and pincode=="Sadio" :
        
        return render_template ('sadio.html')
    
    elif nom=="4" and pincode=="Sinthu" :
        
        return render_template ('sinthu.html')
    
    
    elif add!= None and mail!= None :
        
        return render_template ('validé.html')
    
    
    else:
        return render_template ('erreur1.html')
    
    
@app.route('/index4.html')

def acc():
    
    return render_template ('index4.html')


@app.route('/apropos.html')

def  apropos():
    return render_template ('apropos.html')


@app.route('/contact.html')

def  contact():
    return render_template ('contact.html')






    
    


        


   
    



