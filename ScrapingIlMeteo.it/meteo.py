#Classe contenente il comportamento del parser html per il sito meteo.it

import requests
from bs4 import BeautifulSoup
import json

class meteo:
    
    def __init__(self, localita):
        self.localita = localita

    #Metodo che calcola le previsioni del meteo del sito meteo.it
    def prendiPrevisioni(self): 

        #L'url a cui è associata la previsione odierna della località è cosi fatto: 
        # https://www.meteo.it/meteo/"nomecitta-oggi-idcitta
        #dobbiamo scoprire l'id della città e fortunatamente il sito mette a disposizione un
        #api che restituisce l'id della citta a partire dal nome della citta
        #https://api.meteosuper.it/v1//locations?name=nomecitta
        idCitta = ""
        try:
            idCitta = json.loads(requests.get('https://api.meteosuper.it/v1//locations?name='+self.localita).text)
             
        except:
            idCitta = "null"
            print("\tQualcosa è andato storto")

        

        #Ora la variabile idCitta contiene la stringa di riferimento della citta selezionata o null nel caso in cui la città non sia stata trovata

        #Effettuo la richiesta che ritorna la pagina del meteo della citaa selezionata
      
        r = "" 
        try:
            
            r = requests.get("https://www.meteo.it/meteo/"+self.localita+"-oggi-"+idCitta[0]['idLocation']).text
            print("\tDati scaricati da meteo.it ...")
        except:
            print("\tQualcosa è andato storto")
        


        soup = BeautifulSoup(r, features="html.parser")
        meteo = []
        oraArr = []
        previsioneArr = []
        temperaturaArr = []
        for val in soup.find_all('ul', attrs = {'class':'mb-24'}):
            
          
    
            for ora in val.find_all('span', attrs = {'class': 'hour'}):
                
                ora = ora.find("time")
                oraArr.append(ora.text+":00")

            for situazione in val.find_all('figure'):
                previsioneArr.append(situazione.img['alt'])
          
            for temperatura in val.find_all('span', attrs = {'class': 'replacedH5Temperature'}):
           
                temperaturaArr.append(temperatura.text)

        for i in range(len(oraArr)): 
            previsione = {"ora": oraArr[i], "situazione":previsioneArr[i], "temperatura":temperaturaArr[i]}
            meteo.append(previsione)
     
       

        return meteo
