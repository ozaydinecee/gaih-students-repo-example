# -- coding: utf-8 --
"""
Created on Tue Mar  9 21:21:21 2021

@author: Ece Ozaydin
@since 9.03.2021
"""
  

evenNums = list(range(0,10,2))
oddNums=list(range(1,10,2))
nums=evenNums+oddNums
print(nums)
myNum=2
dividedList=[x/myNum for x in nums]
#print(dividedList)
for i in range(0,len(dividedList)):
    print(dividedList[i])
