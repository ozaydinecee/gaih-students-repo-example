# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:35:37 2021

@author: Ece Ozaydin
@date:10.03.2021
"""
# key is identity number
cv={'1234':{'Name':"Ece",'Surname':"Ozaydin",'Department': "Computer Engineering",'Abilities': "Python"},
    '1235':{'Name':"John",'Surname':"Wick",'Department': "Industrial Engineering",'Abilities': "Java"},
    '1236':{'Name':"Rose",'Surname':"Watson",'Department': "Chemical Engineering",'Abilities': "C++"},
    '1237':{'Name':"William",'Surname':"Shakespeare",'Department': "Computer Engineering",'Abilities': "C#"},
    '1238':{'Name':"Elon",'Surname':"Musk",'Department': "Electrical Engineering",'Abilities': "PLC"}}

for k,v in cv.items():
  print("Key:", k, "Value:", v)
