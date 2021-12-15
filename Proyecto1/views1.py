from typing import get_args
from django.http import HttpResponse
import datetime
from django.template import Template, context
from django.template import loader
from django.shortcuts import get_object_or_404
import ast

#-------clase persona-------
class Persona(object):
    def __init__(self, nombre, apellido, apellido2):
        self.nombre=nombre
        self.apellido=apellido
        self.apellido2=apellido2
      
       

#---vista---------
def saludo1(request):
    
#cargamos documento externo y lo renderizamos 
    pn=Persona(" rodrigo manuel","laura","apaza")
    #nombre="manuel"
    #apellido="laura"
    ahora=datetime.datetime.now()
    temas=["plantillas","modelos","vistas","formulario","desplige"]
    #doc_externo=open("F:/319/django/Proyecto1/Proyecto1/plantillas/plantillas.html")#guardamos en una variable la ruta de template
    #plt=Template(doc_externo.read())#cargams el documento en doc_externo en la variable ply
    #doc_externo.close()#cerramos la comunicacion
    #--------------------------------------
    doc_externo=loader.get_template('plantillas.html')
    #-------creamos el contexto(generalmente el contexto llevan informacion )
    #ctx=context({"nombre_persona": pn.nombre,"apellido_persona":pn.apellido, "fecha_actual": ahora})
    #--renderizar el documento------
    documento=doc_externo.render({"nombre_persona": pn.nombre,"apellido_persona":pn.apellido, "apellido2": pn.apellido2,"fecha_actual": ahora,"temas_curso":temas,"c":c})
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2 
            elif opr=="-": 
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2          
    except:
        c="no es valido el operador ...." 
    print(c)      
    return HttpResponse(documento) #cargamos el documento
     
def saludo2(request):
#cargamos documento externo y lo renderizamos 
    saludo="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>hola desde vista 2</h1>
    <input type="text">
</body>
</html>
    """
    return HttpResponse(saludo) 
#------------------------------
# class Pregunta(object):
#     def __init__(self, a, b):
#         self.valor1=a
#         self.valor2=b
        
def calcu(request):
    
    def calculadora(funcion, a, b):
        return  funcion(a,b)
  
    def suma(x,y):
        print( x+y)
        suma=x+y
        return suma
       
    def resta(x,y):
        print( x-y)
        resta=x-y
        return resta
    
    def multi(x,y):
        print( x*y)
        multi=x*y
        return multi
         
    def div(x,y):
        print( x/y)
        
        div=x/y
        return div     
    resultado=''
    
    try:
        if request.method=="POST":
           # n1=ast.literal_eval(str(request.GET["num1"]))
            #n2=ast.literal_eval(str(request.GET["num1"]))
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
               #c=n1+n2 
               #resultado = str(resultado)
               resultado=calculadora(suma, n1,n2)
                
            elif opr=="-": 
                #c=n1-n2
                resultado=calculadora(resta, n1,n2)
            elif opr=="*":
                #c=n1*n2
                resultado=calculadora(multi, n1,n2)
            elif opr=="/":
                #c=n1/n2
                resultado=calculadora(div, n1,n2)          
    except:
        c="no es valido el operador ...." 
    
    doc=loader.get_template('index.html')
    documento=doc.render({'c':resultado})
    return HttpResponse(documento)

def fibonacci(request):
    c=''
    try:
        
        if request.method=="POST":
            num=eval(request.POST.get('num'))
                       
            def rec_fib(num):
                if num > 1:
                    return rec_fib(num-1) + rec_fib(num-2)
                return num
    
            for i in range(num):
                c=i
                print(rec_fib(c))
    except:
        c="no es valido el operador ...."             
    doc=loader.get_template('index1.html')
    documento=doc.render({'result':rec_fib(c)})
    return HttpResponse(documento)

#---------par-----------
def par(request):
    resultado=''
    try:
        
        if request.method=="POST":
            num=eval(request.POST.get('num'))    
            if num%2==0:
                    resultado="es par..."
            else:
                    resultado="no es par..."            
            
            print(resultado) 

    except:
        resultado="no es valido el operador ...."             
    doc=loader.get_template('index2.html')
    documento=doc.render({'result':resultado})
    return HttpResponse(documento)
#-----------------facotrial--------
def factorial(request):
    c=''
    try:
        if request.method=="POST":
            num=eval(request.POST.get('num')) 
            
            
            factorial_total = 1
            while num > 1:
                    factorial_total *= num
                    num -= 1
                    c=factorial_total
        
    
    except:
        c="no es valido el operador ...."             
    doc=loader.get_template('index3.html')
    documento=doc.render({'result':c})
    return HttpResponse(documento)    