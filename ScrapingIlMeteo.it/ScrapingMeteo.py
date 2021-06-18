######################################################################################################################
#Programma che fa uso di web scraping per confrontare i dati meteo provenienti da diversi siti della città selezionata
######################################################################################################################

import Ilmeteo
import trebmeteo
import meteoam
import meteo
import datetime


now = datetime.datetime.now()

print("\t########################################################################################################")
print("\tTool che effettua lo scraping dei dati meteo odierni ("+str(now.date())+") da ilmeteo.it, 3bmeteo.com e meteo.it")
print("\t########################################################################################################")
print("\n\n\n")
#Variabile di controllo per il programma principale
res = "s"

#Programma principale-parte "grafica"
while res != "n":
    scelta = input("\tDigitare [1] se si vuole effettuare la prova del sito meteoam.it\n\tDigitare [2] se si vogliono consultare le previsioni meteo\n\n\t")
    if(scelta == "1"):
        meteoa = meteoam.meteoam()
        meteoa.scaricaTuttePrevisioni()
    if(scelta == "2"):
        location = input("\tInserisci la città italiana di cui vuoi analizzare le previsioni metereologiche:\n\t")
        print("\tLOCALITA:\t"+location)

        ilmeteo = Ilmeteo.Ilmeteo(location)
        treb = trebmeteo.trebmeteo(location)
        mediasetmeteo = meteo.meteo(location)

        mediasetmeteo = mediasetmeteo.prendiPrevisioni()
        treb = treb.prendiPrevisioni()
        ilmeteo = ilmeteo.prendiPrevisioni()

        variazioneLunghezza = len(ilmeteo) - len(treb)
        for i in range(variazioneLunghezza): 
            treb.append({'situazione': "null", "temperatura": "null"})
   

        print("\n\n\n\t\t\t\tPREVISIONE DI OGGI PER LA LOCALITA: "+location+"\n\n")
        print("\t\tilMeteo.it")
        print("\t\t___________________________________________\n")
        for i in range(len(ilmeteo)):
            try:
                print("\t\t"+ilmeteo[i]['ora']+"\t\t"+ilmeteo[i]['situazione']+"-"+ilmeteo[i]['temperatura'])
            except:
                print("\t\tnull")
        print("\n\n\n")
        print("\t\t3bMeteo.com")
        print("\t\t____________________________________________\n")
        for i in range(len(treb)):
            try:
                print("\t\t"+treb[i]['ora']+"\t\t"+treb[i]['situazione']+"-"+treb[i]['temperatura'])
            except: 
                print("\t\tnull")

        print("\n\n\n")
        print("\t\tMeteo.it")
        print("\t\t____________________________________________\n")
        for i in range(len(mediasetmeteo)):
            try:
                print("\t\t"+mediasetmeteo[i]['ora']+"\t\t"+mediasetmeteo[i]['situazione']+"-"+mediasetmeteo[i]['temperatura'])
            except: 
                print("\t\tnull")

    res = input("\n\n\n\tVuoi continuare? [s/n]\t")
        







