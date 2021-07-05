from modules.twitchClips import *
from modules.clipEditor import *
from modules.configHandler import *
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory



def getInputs():
    option = 0
    channel = ""
    while option <= 0 or option > 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("██████╗ ███████╗███████╗████████╗    ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗")
        print("██╔══██╗██╔════╝██╔════╝╚══██╔══╝   ██╔═══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
        print("██████╔╝█████╗  ███████╗   ██║█████╗██║   ██║█████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║")
        print("██╔══██╗██╔══╝  ╚════██║   ██║╚════╝██║   ██║██╔══╝╚════╝██║   ██║██╔══╝  ██║╚██╗██║")
        print("██████╔╝███████╗███████║   ██║      ╚██████╔╝██║         ╚██████╔╝███████╗██║ ╚████║")
        print("╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═════╝ ╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
        print("\n\t\tCreated by Giulio Venturini\tReleased under GNUv3.0 license\n\nWelcome to Best-Of-Gen, an auto Best-of Generator of the top clip of a channel!\n")
        print("1)Generate video")
        print("2)Credits and info")
        option = int(input("\n>>"))
    if option == 1:
        resp = False
        ft = 0
        while not resp:
            os.system('cls' if os.name == 'nt' else 'clear')
            if ft!=0:
                print("\n\nChannel not available :/")
            ft = 1
            ch = input("\n\nName of the channel:")
            print("\nChecking if the channel is available...")
            resp = isChannel(ch)
        channel = ch
        option = 0
        while option <= 0 or option > 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\n\tChoose the range of the clip")
            print("\n1)24 hours")
            print("2)7 days")
            print("3)30 days")
            print("4)All time")
            option = int(input("\n\n>>"))
        if option == 1:
            ranged = "24h"
        if option == 2:
            ranged = "7d"
        if option == 3:
            ranged = "30d"
        if option == 4:
            ranged = "all"
        option = 0
        while option <=0 or option >19:
            os.system('cls' if os.name == 'nt' else 'clear')
            option = int(input("\nHow many clip do you want to use(1-19):"))
        nclips = option
        iPath = "./sas"
        i=0
        while not os.path.isdir(iPath) or i == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            if i==1:
                print("\nInvalid Directory!")
            i=1
            print("\nSelect a path to save the montage:")
            root = Tk()
            root.withdraw()
            iPath=askdirectory()
    return channel,nclips,ranged,iPath

def main():
    if os.path.isfile(getOutputName()+"TEMP_MPY_wvf_snd.mp3"):
        os.remove(getOutputName()+"TEMP_MPY_wvf_snd.mp3")
    removeAllClips()
    initConf(verbose=False)
    channel,nclips,range,iPath = getInputs()
    print("\nFetching data...")
    data = fetchClips(channel,max=nclips,range=range)
    i = 1
    print("\nData Fetched!\n\nDownloading clips...")
    try:
        for clip in data:
            downloadClip(clip,f"clip{i}")
            i+=1
    except:
        print("An error occured while downloading the clips,stopping the execution")
        quit()
    print("\nClips Downloaded!\n\nCreating the video...\n\n")
    editClips(save_path=iPath)
    try:
        removeAllClips()
    except:
        print("\nError while deleting the clips\nthe clips will be deleted the next time you run the program!")
    print("\n\n Video created!")

if __name__ == '__main__':
    main()