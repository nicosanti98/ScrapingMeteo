
import requests


class meteoam:
       

       def scaricaTuttePrevisioni(self):
            #Vengono effettuate 50000 richieste per ricevere verosimilmente tutti i dati delle previsioni
            for i in range (50000):
                try:
                    r = requests.get("http://www.meteoam.it/ta/previsione/"+str(i))
                    print("\tRequested URL: "+"http://www.meteoam.it/ta/previsione/"+str(i)+"\t"+str(r))
                except: 
                    print("\tQualcosa è andato storto")
                    break
            
       





