import matplotlib.pyplot as plt
import numpy as np

def analysis(data):
    df =np.array(data)
    meanTo = np.mean(df[:,6])
    std_dev = np.std(df[:,6])
    UCL = meanTo + 3 * std_dev
    LCL = meanTo - 3 * std_dev

    dfT = df[df[:,7]=="True"]
    meanT = np.mean(df[:,6])
    std_devT = np.std(df[:,6])
    UCLt = meanT + 3 * std_devT
    LCLt = meanT - 3 * std_devT

    dfF = df[df[:,7]=="False"]
    meanF = np.mean(df[:,6])
    std_devF = np.std(df[:,6])
    UCLf = meanF + 3 * std_devF
    LCLf = meanF - 3 * std_devF

    fig = plt.figure(figsize=(15,10), layout='constrained')
    axs = fig.subplot_mosaic([["total", "total"],
                            ["true", "false"]])
    
    
    axs["total"].plot(df[:,0], df[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["total"].axhline(meanTo, color='green', linestyle='--', label='Average')
    axs["total"].axhline(UCL, color='red', linestyle='--', label='UCL (3σ)')
    axs["total"].axhline(LCL, color='red', linestyle='--', label='LCL (3σ)')

    axs["total"].set_xlabel('ID')
    axs["total"].set_ylabel('Time_Product')
    axs["total"].set_title('Lean Control Paper ')
    axs["total"].legend()
    

    axs["true"].plot(dfT[:,0], dfT[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["true"].axhline(meanT, color='green', linestyle='--', label='Average')
    axs["true"].axhline(UCLt, color='red', linestyle='--', label='UCL (3σ)')
    axs["true"].axhline(LCLt, color='red', linestyle='--', label='LCL (3σ)')
    axs["true"].set_xlabel('ID')
    axs["true"].set_ylabel('Time_Product')
    axs["true"].set_title('Lean Control Paper Bike Defect True')
    axs["true"].legend()

    axs["false"].plot(dfF[:,0], dfF[:,6], marker='o', linestyle='-', color='b', label='Time_Product')
    axs["false"].axhline(meanF, color='green', linestyle='--', label='Average')
    axs["false"].axhline(UCLf, color='red', linestyle='--', label='UCL (3σ)')
    axs["false"].axhline(LCLf, color='red', linestyle='--', label='LCL (3σ)')
    axs["false"].set_xlabel('ID')
    axs["false"].set_ylabel('Time_Product')
    axs["false"].set_title('Lean Control Paper Bike Defect False')
    axs["false"].legend()

    
    path = f"graph/graph.png"
    plt.savefig(path) 
    return path

    
