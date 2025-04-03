#Importazione matplotlib per la creazione del grafico di Carta di controllo
import matplotlib.pyplot as plt
#Importazione numpy per la gestione dei dati
import numpy as np

#Funzione che riceve come argomento i dati e crea la Carta di Controllo
def analysis(data):
    
    #Trasformo in dati in array numpy
    df =np.array(data)
    
    #Calcolo media e deviazione standard
    meanTo = np.mean(df[:,6])
    std_dev = np.std(df[:,6])
    
    #Limite di Controllo Superiore (UCL - Upper Control Limit)
    UCL = meanTo + 3 * std_dev
    #Limite di Controllo Inferiore (LCL - Lower Control Limit)
    LCL = meanTo - 3 * std_dev

    #Filtro delle bici che hanno difetti e calcolo delle statistiche
    dfT = df[df[:,7]=="True"]
    meanT = np.mean(dfT[:,6])
    std_devT = np.std(dfT[:,6])
    UCLt = meanT + 3 * std_devT
    LCLt = meanT - 3 * std_devT

    #Filtro delle bici che NON hanno difetti e calcolo delle statistiche
    dfF = df[df[:,7]=="False"]
    meanF = np.mean(dfF[:,6])
    std_devF = np.std(dfF[:,6])
    UCLf = meanF + 3 * std_devF
    LCLf = meanF - 3 * std_devF

    #Creazione della Figure del grafico
    fig = plt.figure(figsize=(15,10), layout='constrained')

    #Scelta della griglia dei subplot
    axs = fig.subplot_mosaic([["total", "total"],
                            ["true", "false"]])
    
    #Impostazione primo subplot con dati totali
    axs["total"].plot(df[:,0], df[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["total"].axhline(meanTo, color='green', linestyle='--', label='Average')
    axs["total"].axhline(UCL, color='red', linestyle='--', label='UCL (3σ)')
    axs["total"].axhline(LCL, color='red', linestyle='--', label='LCL (3σ)')
    axs["total"].set_xlabel('ID')
    axs["total"].set_ylabel('Time_Product')
    axs["total"].set_title('Control Paper ')
    axs["total"].legend()
    
    #Impostazione subplot con bici che hanno difetti
    axs["true"].plot(dfT[:,0], dfT[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["true"].axhline(meanT, color='green', linestyle='--', label='Average')
    axs["true"].axhline(UCLt, color='red', linestyle='--', label='UCL (3σ)')
    axs["true"].axhline(LCLt, color='red', linestyle='--', label='LCL (3σ)')
    axs["true"].set_xlabel('ID')
    axs["true"].set_ylabel('Time_Product')
    axs["true"].set_title('Control Paper Bike Defect True')
    axs["true"].legend()

    #Impostazione subplot con bici che NON hanno difetti
    axs["false"].plot(dfF[:,0], dfF[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["false"].axhline(meanF, color='green', linestyle='--', label='Average')
    axs["false"].axhline(UCLf, color='red', linestyle='--', label='UCL (3σ)')
    axs["false"].axhline(LCLf, color='red', linestyle='--', label='LCL (3σ)')
    axs["false"].set_xlabel('ID')
    axs["false"].set_ylabel('Time_Product')
    axs["false"].set_title('Control Paper Bike Defect False')
    axs["false"].legend()

    path = "graph/graph.png"

    #Salvataggio Carta di controllo
    plt.savefig(path)

    #Quando il grafico è salvato restituisce il percorso
    return path

    
