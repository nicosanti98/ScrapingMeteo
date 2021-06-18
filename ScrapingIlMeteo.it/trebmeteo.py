#Classe contenente il comportamento del parser html per il sito 3bmeteo.com

import requests
from bs4 import BeautifulSoup

class trebmeteo:
   def __init__(self, localita):
        self.localita = localita

    #Metodo che calcola le previsioni del meteo del sito 3bmeteo.com
   def prendiPrevisioni(self):
        r = ""
        try:
            r = requests.get('https://3bmeteo.com/meteo/'+self.localita).text
            print("\tDati scaricati da 3bmeteo.com ...")

        except:
            print("\tQualcosa è andato storto")


        soup = BeautifulSoup(r, features="html.parser")
        meteo = []
        oraArr = []
        previsioneArr = []
        temperaturaArr = []
        for val in soup.find_all('div', attrs = {'class': 'table table-border-v table-previsioni table-previsioni-ora'}):
    
            for ora in val.find_all('div', attrs = {'class':'col-xs-1-4 big zoom_prv'}):
               
                oraArr.append(ora.text.replace(" ", ""))
            for ora in val.find_all('div', attrs = {'class': 'col-xs-1-4 big'}):
                oraArr.append(ora.text.replace(" ", ""))

            for situazione in val.find_all('div', attrs = {'class': 'col-xs-2-4'}):
                previsioneArr.append(situazione.text.replace("\n","")[1:-1])


            for spantemperatura in val.find_all('span', attrs = {'class': 'switchcelsius switch-te active'}):
                    temperaturaArr.append(spantemperatura.text)



        #Elimino il primo elemento delle temperature che corrisponde al valore attuale rilevato dalla centralina meteo (solo se presente),
        #tale valore è poco utile al fine di confrontarlo con gli altri siti
        try: 
            if(len(temperaturaArr) > len(oraArr)):
                temperaturaArr.pop(0)
        except: 
            print("La lista è vuota")
        

        for i in range(len(oraArr)): 
            previsione = {"ora": oraArr[i], "situazione":previsioneArr[i], "temperatura":temperaturaArr[i]}
            meteo.append(previsione)
 

        

     

        

        return meteo





