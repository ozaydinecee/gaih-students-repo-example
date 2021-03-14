# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:25:56 2021

@author: Ece Ozaydin
@date 14.03.2021
"""
ece = { "name":"Ece","project" : 80,"midterm" : 75,"final" : 78} 
ali = { "name":"Ali","project" : 82,"midterm" : 80,"final" : 67} 
ege = { "name":"Ege","project" : 77,"midterm" : 78,"final" : 80} 
efe = { "name":"Efe","project" : 67,"midterm" : 40,"final" : 69} 
eda = { "name":"Eda","project" : 29,"midterm" : 65,"final" : 50} 

def calculate_passing_grade(students):
    passing_grade=students["project"]*(0.3)+students["midterm"]*(0.3)+students["final"]*(0.3)
    return passing_grade

students=[ece,ali,ege,efe,eda]

for i in students :
    print("Average marks of {0} is :{1} " .format(i["name"], calculate_passing_grade(i))) 
    print("{0} 's grades: \n project grade: {1} \n midterm grade: {2} \n final grade: {3}".format(i["name"],i["project"],i["midterm"],i["final"]))
