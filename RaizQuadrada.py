# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:14:23 2018

@author: Girolamo Santoro
"""

x=int(input("Entre com um número inteiro positivo para cálculo da raiz quadrada :  "))
erro = 0.001
guess = int(x/10)
while (  abs(x - guess*guess)  > erro ):
    guess = (guess+x/guess)/2

iguess=int(guess)
if (iguess*iguess == x):
    print("Raiz exata : ", iguess)
else:
    print ("Raiz aproximada : ",guess)   
