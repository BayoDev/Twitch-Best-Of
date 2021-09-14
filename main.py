#!/usr/bin/env python
from modules.twitchClips import *
from modules.clipEditor import *
from modules.configHandler import *
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory



def getInputs():
    # Start the GUI and get the following inputs:
    #
    #   channel: the name of the channel
    #   nclips: number of clips that will be used in the video
    #   ranged: get the range of time of the clip {24h|7d|30d|all}
    #   iPath : directory to store where the output video will be stored
    #

    option = 0
    channel = ""
    while option <= 0 or option >= 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("██████╗ ███████╗███████╗████████╗    ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗")
        print("██╔══██╗██╔════╝██╔════╝╚══██╔══╝   ██╔═══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
        print("██████╔╝█████╗  ███████╗   ██║█████╗██║   ██║█████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║")
        print("██╔══██╗██╔══╝  ╚════██║   ██║╚════╝██║   ██║██╔══╝╚════╝██║   ██║██╔══╝  ██║╚██╗██║")
        print("██████╔╝███████╗███████║   ██║      ╚██████╔╝██║         ╚██████╔╝███████╗██║ ╚████║")
        print("╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═════╝ ╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
        print("\n\t\tCreated by Giulio Venturini\tReleased under GPLv3.0 license\n\nWelcome to Best-Of-Gen, an auto Best-of Generator of the top clip of a channel!\n")
        print("1)Generate video")
        print("2)Credits and info")
        print("3)Exit")
        option = int(input("\n>>"))
        if option == 3:
            # Quit Option
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        if option == 2:
            # Credits Option
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\tBest-Of-Gen")
            print("\n\tCreated by Giulio Venturini")
            print("\n\tReleased under GPLv3.0 license")
            print("\n\tGo to https://github.com/BayoDev/Twitch-Best-Of-Gen for more info")
            input("\n Press any key to continue...")
    if option == 1:
        # Generate Video option

        #---channel---

        resp = False
        ft = 0
        while not resp:
            os.system('cls' if os.name == 'nt' else 'clear')
            if ft!=0:
                print("\n\nChannel not available :/")
            ft = 1
            ch = input("\n\nName of the channel:")
            print("\nChecking if the channel is available...")
            if not ch.__contains__("@"):
                resp = isChannel(ch)
        channel = ch

        #---ranged---

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

        #---nclips---

        option = 0
        while option <=0 or option >19:
            os.system('cls' if os.name == 'nt' else 'clear')
            option = int(input("\nHow many clip do you want to use(1-19):"))
        nclips = option

        #---iPath---

        iPath = "./sas"
        i=0
        while not os.path.isdir(iPath) or i == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            if i==1:
                print("\nInvalid Directory!")
            i=1
            print("\nSelect a path to save the montage:")
            if not getCmdOnly():
                root = Tk()
                root.withdraw()
                iPath=askdirectory()
            else:
                iPath=getOutPath()

    return channel,nclips,ranged,iPath

def removeOldFiles():
    # Delete temporary file that may still exist if the program was
    # interrupted during the editing of the clips
    try:
        if os.path.isfile(getOutputTitle()+"TEMP_MPY_wvf_snd.mp3"):
            os.remove(getOutputTitle()+"TEMP_MPY_wvf_snd.mp3")
        removeAllClips()
    except:
        return


def main():

    removeOldFiles()

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
        return
    
    print("\nClips Downloaded!\n\nCreating the video...\n\n")

    createVideo(save_path=iPath,channel=channel,time=range)

    print("\n\n Video created!")

    return

if __name__ == '__main__':
    main()