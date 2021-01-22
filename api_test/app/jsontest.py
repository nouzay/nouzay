# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:38:14 2020

@author: -
"""

import json

f = open('json')
data = json.load(f)
f.close()    
print(data)
print(data["features"])
print(data["features"][0]["geometry"])

for i in data["features"]:
    print(i["geometry"]["coordinates"][0])
