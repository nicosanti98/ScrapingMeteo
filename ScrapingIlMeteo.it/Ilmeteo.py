#Classe contenente il comportamento del parser html per il sito ilmeteo.it

import requests
from bs4 import BeautifulSoup
import time

class Ilmeteo:
    
    def __init__(self, localita):
        self.localita = localita

    #Metodo che calcola le previsioni del meteo del sito ilMeteo.it
    def prendiPrevisioni(self): 
        r = ""
        try:
            
            r = requests.get('https://ilmeteo.it/meteo/'+self.localita).text
            
            print("\tDati scaricati da ilmeteo.it ...")
        except:
            print("\tQualcosa è andato storto")
        


        soup = BeautifulSoup(r, features="html.parser")
        meteo = []
        oraArr = []
        previsioneArr = []
        temperaturaArr = []
        for val in soup.find_all('tr', id = True):
    
            for ora in val.find_all('td', attrs = {'class': 'f'}):
                ora = ora.find("span")
                oraArr.append(ora.text+":00")
            for situazione in val.find_all('td', attrs = {'class': 'col3'}):
                ##Rilevata la presenza di un carattere non tradotto lo sostituisco con uno spazio
                previsioneArr.append(situazione.text.replace("\xa0", " "))
            for temperatura in val.find_all('td', attrs = {'class': 'col4'}):
                temperatura = temperatura.find("span")
                temperaturaArr.append(temperatura.text)
        for i in range(len(oraArr)): 
            previsione = {"ora": oraArr[i], "situazione":previsioneArr[i], "temperatura":temperaturaArr[i]}
            meteo.append(previsione)
       

        return meteo


