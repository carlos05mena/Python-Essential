# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:50 2019

@author: Juan Carlos
"""

class Employee:
   empCount = 0

   def __init__(a,nombre, salario):
      a.nombre = nombre
      a.salario = salario     
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.nombre,  ", Salary: ", self.salario)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Sandra", 5000)
emp3 = Employee("Ana",8000)
emp4 = Employee("Briguitte",8000)
emp5 = Employee ('Juan',1200)
emp6 = Employee ('Carlos',1600)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

