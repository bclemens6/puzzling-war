# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:33:10 2018

@author: Ben
"""

import numpy

WAR0=4.7
ExpiryYears=3
Age0=26
OptionValue=24
TenorYears=5
NoOptionSum=0.0
OptionSum=0.0
NetCost=0.0

for i in range (10000000):
    WARCount=WAR0
    YearCount=0
    AgeCount=Age0
    WinCost=8
    while YearCount < ExpiryYears:
        SkillChange=numpy.random.normal()*1.4
        WARCount+=SkillChange
        if AgeCount>29:
            WARCount-=.5
        CostChange=numpy.random.normal()*.8+0.25
        WinCost+=CostChange
        AgeCount+=1
        YearCount+=1
    AgeFinal=AgeCount+TenorYears
    AgePenalty = (max(AgeFinal,29)-max(AgeCount,29))*.5
    NoOptionSum+=max(0,(WARCount-AgePenalty/2)*WinCost*TenorYears)
    OptionSum+=max((WARCount-AgePenalty/2)*WinCost*TenorYears,OptionValue*TenorYears)

NetCost=OptionSum-NoOptionSum

print ("No option earnings are "+ str(round(NoOptionSum/10000000,2)))
print ("Option earnings are "+ str(round(OptionSum/10000000,2)))
print ("Option value is "+ str(round(NetCost/10000000,2)))


