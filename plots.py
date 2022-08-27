# import necessary libraries
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

import os.path
  

def finalPlotting(stepsize):  
    # use glob to get all the csv files 
    # in the folder
    scenario = "_lake2_ep_"
    path = os.path.join(os.getcwd(),'output/smaller_timestep/')
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    secondsPerDay=24*60*60
    finalDF=pd.DataFrame()
    data_day_list = []
    
    # loop over the list of csv files
    for f in csv_files:
          
        # read the csv file
        df = pd.read_csv(f)
          
        # print the location and filename
        print('Location:', f)
        print('File Name:', f.split("\\")[-1])
        data_day_list.append(df)
        
    finalDF = pd.concat(data_day_list)
    finalDF = finalDF.rename(columns={"Unnamed: 0": "realtime"})
 
    
#plot each microplastic form  
    thingsToPlot1=['C_A1','C_A2', 'C_A3', 'C_A4']
    for p in thingsToPlot1:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)
    
    #plt.legend(loc='best')
    #plt.yscale("log")
    plt.title("pristine")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path,scenario + 'fig-prist.png'),dpi=200)
    plt.show()
    print("pristine plotted...")

    thingsToPlot2=['C_B1','C_B2', 'C_B3', 'C_B4']
    for p in thingsToPlot2:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("heteroaggregated")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-het.png'),dpi=200)
    plt.show()
    print("heteroaggregated plotted...")
    
    thingsToPlot3=['C_C1','C_C2', 'C_C3', 'C_C4']
    for p in thingsToPlot3:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("biofouled")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-bf.png'),dpi=200)
    plt.show()
    print("biofouled plotted...")
    
    thingsToPlot4=['C_D1','C_D2', 'C_D3', 'C_D4']
    for p in thingsToPlot4:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("biofouled-heteroaggregated")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-bf-het.png'),dpi=200)
    plt.show()
    print("biofouled heteroaggregated plotted...")

#plot each lake compartment  
    thingsToPlot5=['C_A1','C_B1', 'C_C1', 'C_D1']
    for p in thingsToPlot5:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)
    
    #plt.legend(loc='best')
    #plt.yscale("log")
    plt.title("surface")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path,scenario + 'fig-surf.png'),dpi=200)
    plt.show()
    print("surface plotted...")

    thingsToPlot6=['C_A2','C_B2', 'C_C2', 'C_D2']
    for p in thingsToPlot6:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("epilimnion")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-epi.png'),dpi=200)
    plt.show()
    print("epilimnion plotted...")
    
    thingsToPlot7=['C_A3','C_B3', 'C_C3', 'C_D3']
    for p in thingsToPlot7:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("hypolimnion")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-hypo.png'),dpi=200)
    plt.show()
    print("hypolimnion plotted...")
    
    thingsToPlot8=['C_A4','C_B4', 'C_C4', 'C_D4']
    for p in thingsToPlot8:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.title("sediment")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-sed.png'),dpi=200)
    plt.show()
    print("sediment plotted...")
    

    return

def finalPlottingLOG(stepsize):  
    # use glob to get all the csv files 
    # in the folder
    path = os.path.join(os.getcwd(),'output/equal_properties/L2/PA')
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    secondsPerDay=24*60*60

    finalDF=pd.DataFrame()
    data_day_list = []
    scenario = "_lake2_ep_"
    # loop over the list of csv files
    for f in csv_files:
          
        # read the csv file
        df = pd.read_csv(f)
          
        # print the location and filename
        print('Location:', f)
        print('File Name:', f.split("\\")[-1])
        data_day_list.append(df)
        
    finalDF = pd.concat(data_day_list)
    finalDF = finalDF.rename(columns={"Unnamed: 0": "realtime"})
 
    
#plot each microplastic form  
    thingsToPlot1=['C_A1','C_A2', 'C_A3', 'C_A4']
    for p in thingsToPlot1:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)
    
    #plt.legend(loc='best')
    plt.yscale("log")
    plt.title("pristine")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-prist-log.png'),dpi=200)
    plt.show()
    print("pristine plotted...")

    thingsToPlot2=['C_B1','C_B2', 'C_B3', 'C_B4']
    for p in thingsToPlot2:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)
    
    plt.yscale("log")
    plt.title("heteroaggregated")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, 'fig-het-log.png'),dpi=200)
    plt.show()
    print("heteroaggregated plotted...")
    
    thingsToPlot3=['C_C1','C_C2', 'C_C3', 'C_C4']
    for p in thingsToPlot3:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.yscale("log")
    plt.title("biofouled")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-bf-log.png'),dpi=200)
    plt.show()
    print("biofouled plotted...")
    
    thingsToPlot4=['C_D1','C_D2', 'C_D3', 'C_D4']
    for p in thingsToPlot4:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.yscale("log")
    plt.title("biofouled-heteroaggregated")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-bf-het-log.png'),dpi=200)
    plt.show()
    print("biofouled heteroaggregated plotted...")

#plot each lake compartment  
    thingsToPlot5=['C_A1','C_B1', 'C_C1', 'C_D1']
    for p in thingsToPlot5:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)
    
    #plt.legend(loc='best')
    plt.yscale("log")
    plt.title("surface")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-surf-log.png'),dpi=200)
    plt.show()
    print("surface plotted...")

    thingsToPlot6=['C_A2','C_B2', 'C_C2', 'C_D2']
    for p in thingsToPlot6:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.yscale("log")    
    plt.title("epilimnion")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-epi-log.png'),dpi=200)
    plt.show()
    print("epilimnion plotted...")
    
    thingsToPlot7=['C_A3','C_B3', 'C_C3', 'C_D3']
    for p in thingsToPlot7:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.yscale("log")
    plt.title("hypolimnion")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-hypo-log.png'),dpi=200)
    plt.show()
    print("hypolimnion plotted...")
    
    thingsToPlot8=['C_A4','C_B4', 'C_C4', 'C_D4']
    for p in thingsToPlot8:
        plt.plot(finalDF.realtime/(secondsPerDay),finalDF[p], label=p)

    plt.yscale("log")
    plt.title("sediment")
    plt.xlabel("Time (days)",fontsize=12)
    plt.ylabel("Conc [particles/m3]",fontsize=12)
    leg = plt.legend(loc='center right')
    plt.draw()
    plt.savefig(os.path.join(path, scenario + 'fig-sed-log.png'),dpi=200)
    plt.show()
    print("sediment plotted...")
    

    return

