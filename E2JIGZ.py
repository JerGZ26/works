import os
import sys
try: 
    import requests 
except ImportError: 
    os.system('pip install requests') 
    print('Installing requests...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
try: 
    import webbrowser 
except ImportError: 
    os.system('pip install webbrowser') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install BeautifulSoup') 
    print('Installing BeautifulSoup...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
    
# Jeremy Isai Garcia Zuñiga
# El script realiza una busqueda de la facultad que desee
# con un rango de paginas inicial y final em la que se  
# recorrera uno por uno y se g¡hace una peticion de la url
# si el estatus de esta pagina es solicitada correctamente
# se le dara una forma bonita al contenido del codigo y se
# seleccionaran la informacion que haya en las etiquetas h3
# y para cada etiqueta en esta informacion se buscara un segundo
# url con la etiqueta href y de nuevo se guardara la peticion
# si el estatus de este es correcto se le da un formato bonito
# nuevamente, y ahora se seleccionaran los parrafos de esta
# peticion y para cada elemento de este si la facultad esta
# en el elemto del texto obtenido se abrira el url encontrado
# en nuestro navegador preferido.

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
