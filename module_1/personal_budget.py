# -*- coding: utf-8 -*-
"""personal_budget.ipynb

Kişisel Bütçe: Gelir ve giderleri alıp kalan parayı hesaplayan program            
Personal Budget: Program that takes income and expenses and calculates the remaining money
"""

gelir = float(input("Gelirinizi giriniz: "))
gider = float(input("Giderinizi giriniz: "))

kalan = gelir - gider
print("Kalan para: ", kalan)


# Fonksiyon ile yaparsak
def budget_calculate():
  income = float(input("Income: "))
  expenses = float(input("Expenses: "))

  remaining = income - expenses
  print("Remaining: ", remaining)

budget_calculate()
