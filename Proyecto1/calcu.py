from django.shortcuts import get_object_or_404

# def calculadora(funcion, a, b):
    
    
#      funcion(a,b)
# def suma(x,y):
#     print("suma",x+y)
# #    c=x+y
# #    return print(c)
# def resta(x,y):
#     return x-y
    
# def multi(x,y):
#     print("suma",x*y)
         
# def div(x,y):
#     print("suma",x/y)   
    
# a=int(input("ingrese el primer valor"))
# b=int(input("ingrese el segundo valor"))     
# calculadora(suma, a, b)
   
# calculadora(resta, a,b)

# calculadora(multi, a,b)
# calculadora(div, a,b)
# c=''
# n=int(input("valor "))
# def rec_fib(n):
#     if n > 1:
#         return rec_fib(n-1) + rec_fib(n-2)
#     return n
# for i in range(n):
#    print(rec_fib(i))
  
# class Calculadora:
#     def __init__(self, a, b):
#         self.suma=a+b
#         self.resta=a-b
#         self.producto=a*b
#         self.divison=a/b
# a=int(input("valor1"))   
# b=int(input("valor2"))        
# operacion=Calculadora(a,b)
# def cal(funcion, a,b):
#     funcion(a, b)
# #print(operacion.suma)
# cal(operacion.suma, a, b)

n=int(input("valor"))
def fact_1(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total
print(fact_1(n))




