from django.http import HttpResponse
import datetime

def saludo(request):
#cargamos documento externo y lo renderizamos 
    saludo=""""""
    return HttpResponse(saludo) 

def despedida(resquest):
    return HttpResponse("hasta luego alumnos") 

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
         <h1>fecha y hora actual %s</h1>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual=18
    periodo=agno-2019 #el año actual 2019
    edadFutura=edadActual+periodo
    documento="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
         <h1>en el año %s tendras %s años </h1>
    </body>
    </html>"""  %(agno, edadFutura ) 
    return HttpResponse(documento)