import json
import glob

import collections
import numpy as np 
import matplotlib.pyplot as plt


TotcontaImmaginiCambiate=0
TotcontaDescrizioneCambiata=0
TotcontaTitoliCambiati=0
TotcontaCoordinateCambiate=0
TotcontaEntitaCambiate=0
TotcontaDgObjCambiate=0

totEvents=0

totEventiModificati=0


# get list of All json files in different folders:
originalJsonFilesList = glob.glob("C:/Python/JsonMoving/Original(in revisione)/*.json")
modifiedJsonFilesList = glob.glob("C:/Python/JsonMoving/Modified(in revisione)/*.json")

#print("lista dei json files")
#print(originalJsonFilesList)
#print(modifiedJsonFilesList)

# Loop all list
for originalfile, modifiedFile in zip(originalJsonFilesList, modifiedJsonFilesList):
    
    contaImmaginiCambiate=0
    contaDescrizioneCambiata=0
    contaTitoliCambiati=0
    contaCoordinateCambiate=0
    contaEntitaCambiate=0
    contaDgObjCambiate=0
    
    
    #print("file originale")
    #print(originalfile)
    
    #print("file modificato")
    #print(modifiedFile)
    
    # Opening JSON files (original and modified)
    originalJson = open(originalfile, encoding="utf8")
    modifiedJson = open(modifiedFile, encoding="utf8")
   
    
    # load as dictionary
    dataA = json.load(originalJson)
    data1 =  dataA["events"]
    data1= sorted(data1.items(), key=lambda x: x[1]['position'], reverse=False)
    data1= dict(data1)
    dataB = json.load(modifiedJson)
    data2 = dataB["events"]
    data2= sorted(data2.items(), key=lambda x: x[1]['position'], reverse=False)
    data2= dict(data2)
    
    # get list of all ids
    listKeyOriginal= list(data1.keys())
    listKeyModified= list(data2.keys())
    

    print(dataA["narra"]["name"])

    
    #print("numero di eventi in json originale")
    totOriginalEvents= len(listKeyOriginal)
    #print(totOriginalEvents)
    #print("numero di eventi in json originale")
    totModifiedEvents= len(listKeyModified)
    #print(totModifiedEvents)
    print("Totale eventi: " + str(totOriginalEvents))
    print()
    
    totEvents = totEvents + totOriginalEvents
    
    for listKeyOriginal, listKeyModified in zip(listKeyOriginal, listKeyModified):
        
        if data1[listKeyOriginal]["eventMedia"] != data2[listKeyModified]["eventMedia"]:
            #print(" "*1,"immagine diversa nell'evento: " + data1[listKeyOriginal]["title"])
            #print(" "*2,"Originale:")
            #print(" "*3,data1[listKeyOriginal]["eventMedia"])
            #print(" "*2,"Modificato:")
            #print(" "*3,data2[listKeyModified]["eventMedia"])
            contaImmaginiCambiate= contaImmaginiCambiate + 1
            TotcontaImmaginiCambiate= TotcontaImmaginiCambiate + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
        
        if data1[listKeyOriginal]["description"] != data2[listKeyModified]["description"]:
            #print(" "*1,"Descrizione diversa nell'evento: " + data1[listKeyOriginal]["title"], 'red')
            #print(" "*2,"Originale:")
            #print(" "*3,data1[listKeyOriginal]["description"])
            #print(" "*2,"Modificato:")
            #print(" "*3,data2[listKeyModified]["description"])
            contaDescrizioneCambiata= contaDescrizioneCambiata + 1
            TotcontaDescrizioneCambiata= TotcontaDescrizioneCambiata + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
            
        if data1[listKeyOriginal]["latitud"] != data2[listKeyModified]["latitud"] or data1[listKeyOriginal]["longitud"] != data2[listKeyModified]["longitud"]:
            #print(" "*1,"Coordinate diverse nell'evento: " + data1[listKeyOriginal]["title"])
            #print(" "*2,"Originale:")
            #print(" "*3,data1[listKeyOriginal]["latitud"])
            #print(" "*3,data1[listKeyOriginal]["longitud"])
            #print(" "*2,"Modificato:")
            #print(" "*3,data2[listKeyModified]["latitud"])
            #print(" "*3,data2[listKeyModified]["longitud"])
            contaCoordinateCambiate= contaCoordinateCambiate + 1
            TotcontaCoordinateCambiate= TotcontaCoordinateCambiate + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
            
        if data1[listKeyOriginal]["title"] != data2[listKeyModified]["title"]:
            #print(" "*1,"Titolo diverso nell'evento: " + data1[listKeyOriginal]["title"])
            #print(" "*2,"Originale:")
            #print(" "*3,data1[listKeyOriginal]["title"])
            #print(" "*2,"Modificato:")
            #print(" "*3,data2[listKeyModified]["title"])
            contaTitoliCambiati= contaTitoliCambiati + 1
            TotcontaTitoliCambiati= TotcontaTitoliCambiati + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
            
        if set(data1[listKeyOriginal]["props"].keys()) != set(data2[listKeyModified]["props"].keys()):
            #print(" "*1,"Entità diverse nell'evento: " + data1[listKeyOriginal]["title"])
            #print(" "*2,"Originale:")
            #print(" "*3,str(data1[listKeyOriginal]["props"].keys()))
            #print(" "*2,"Modificato:")
            #print(" "*3,str(data2[listKeyModified]["props"].keys()))
            contaEntitaCambiate= contaEntitaCambiate+ 1
            TotcontaEntitaCambiate= TotcontaEntitaCambiate + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
            
        if data1[listKeyOriginal]["objurl"] != data2[listKeyModified]["objurl"]:
            #print(" "*1,"Digital objects diversi nell'evento: " + data1[listKeyOriginal]["title"])
            #print(" "*2,"Originale:")
            #print(" "*3,str(data1[listKeyOriginal]["objurl"]))
            #print(" "*2,"Modificato:")
            #print(" "*3,str(data2[listKeyModified]["objurl"]))
            contaDgObjCambiate= contaDgObjCambiate+ 1 
            TotcontaDgObjCambiate= TotcontaDgObjCambiate + 1
            totEventiModificati= totEventiModificati+1

            
            #print()
            
        
        
        
            
            
        
            
        

    
  
    # Closing files
    originalJson.close()
    modifiedJson.close()
    
    print("TOT TITOLI CAMBIATI")
    print(str(contaTitoliCambiati) + '/' + str(totOriginalEvents))
    
    print("TOT IMMAGINI CAMBIATE")
    print(str(contaImmaginiCambiate) + '/' + str(totOriginalEvents))
    
    print("TOT DESCRIZIONI CAMBIATE")
    print(str(contaDescrizioneCambiata) + '/' + str(totOriginalEvents))
    
    print("TOT COORDINATE CAMBIATE")
    print(str(contaCoordinateCambiate) + '/' + str(totOriginalEvents))
    
    print("TOT ENTITA CAMBIATE")
    print(str(contaEntitaCambiate) + '/' + str(totOriginalEvents))
    
    print("TOT Dg Objects CAMBIATi")
    print(str(contaDgObjCambiate) + '/' + str(totOriginalEvents))
    

    
    #grafico for each stories
    
    
    
    X = ['Titles','Descriptions','Images','Coordinates',"Entities","DgObjects"]
    Ygirls = [contaTitoliCambiati,contaDescrizioneCambiata,contaImmaginiCambiate,contaCoordinateCambiate,contaEntitaCambiate,contaDgObjCambiate]
    Zboys = [totOriginalEvents,totOriginalEvents,totOriginalEvents,totOriginalEvents,totOriginalEvents,totOriginalEvents]

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Modified data')
    plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Original data')

    plt.xticks(X_axis, X)

    plt.title(dataA["narra"]["name"])
    plt.legend()
    plt.show()
    
    print()
    print()
 


    
#grafico

print("///////////////////////")
print("///////////////////////")
print("Grafici dati aggrgati")
print("///////////////////////")
print("///////////////////////")
print()
print("Totale eventi: " + str(totEvents))
print()

print("TOT TITOLI CAMBIATI")
print(str(TotcontaTitoliCambiati) + '/' + str(totEvents))
    
print("TOT IMMAGINI CAMBIATE")
print(str(TotcontaImmaginiCambiate) + '/' + str(totEvents))
    
print("TOT DESCRIZIONI CAMBIATE")
print(str(TotcontaDescrizioneCambiata) + '/' + str(totEvents))
    
print("TOT COORDINATE CAMBIATE")
print(str(TotcontaCoordinateCambiate) + '/' + str(totEvents))
    
print("TOT ENTITA CAMBIATE")
print(str(TotcontaEntitaCambiate) + '/' + str(totEvents))
    
print("TOT Dg Objects CAMBIATi")
print(str(TotcontaDgObjCambiate) + '/' + str(totEvents))

print()
print()


    
X = ['Titles','Descriptions','Images','Coordinates',"Entities","Digital objects"]
Ygirls = [TotcontaTitoliCambiati,TotcontaDescrizioneCambiata,TotcontaImmaginiCambiate,TotcontaCoordinateCambiate,TotcontaEntitaCambiate,TotcontaDgObjCambiate]
Zboys = [totEvents,totEvents,totEvents,totEvents,totEvents,totEvents]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Modified events')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Original events')

plt.xticks(X_axis, X)

plt.title("Changes for each event in all revisited stories")
plt.legend()
plt.show()


#grafico torta
y = np.array([TotcontaTitoliCambiati,TotcontaDescrizioneCambiata,TotcontaImmaginiCambiate,TotcontaCoordinateCambiate,TotcontaEntitaCambiate,TotcontaDgObjCambiate,totEvents-totEventiModificati ])
mylabels = ["Titles", "Descriptions", "Images", "Coordinates", "Entities", "Digital objects","No changes"]

plt.pie(y, labels = mylabels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.show()
    
print(totEventiModificati)