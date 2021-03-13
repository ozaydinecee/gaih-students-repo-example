# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:14:47 2021

@author: Ece Ozaydin
@date: 13.03.2021
"""
def main():
    
    
    print("Welcome to Capital Cities Exam! Be careful not to make a typo")
    
    
    questions={'Where is the capital of England? ':'London', 
        'Where is the capital of Italy? ':'Rome', 
        'Where is the capital of Germany? ':'Berlin',
        'Where is the capital of France? ':'Paris', 
        'Where is the capital of Denmark? ':'Copenhagen', 
        'Where is the capital of Belgium? ':'Brussels', 
        'Where is the capital of Spain? ':'Madrid', 
        'Where is the capital of Poland? ':'Warsaw', 
        'Where is the capital of Finland? ':'Helsinki', 
        'Where is the capital of Turkey? ':'Ankara'}
    
    start = input("Enter your name and click enter when you are ready : ").title()
    print()
    print("\nKudos to  {0}, you scored {1} / {2} ".format(start, exam(questions), len(questions)))
def exam(questions):
    totalScore = 0
    
    for k,v in questions.items():
        if input(k) == v:
            totalScore += 1
            print("Correct answer!")
        else:
            print("Sorry, the answer is \"{}\".".format(v))
    return totalScore
    if(totalScore<=5):
        print("unsuccesful!")
    else:
        print("succesful!")

if __name__ == "__main__":
    main()
