#!/usr/bin/env python
from modules.twitchClips import *
from modules.clipEditor import *
from modules.configHandler import *
from modules.input_handler import *
import os
import logging



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

    initConf(verbose=False)

    logging.basicConfig(level=10,filename="log.txt",filemode='w')

    removeOldFiles()

    name,nclips,range,iPath,type,langs = getInputs()

    print("\nFetching data...")

    if type == 1:
        data = fetchClipsChannel(name,max=nclips,range=range)
    elif type == 2:
        data = fetchClipsCategory(name,max=nclips,range=range,languages=langs)

    i = 1
    print("\nData Fetched!\n\nDownloading clips...")
    
    try:
        for idx,clip in enumerate(data):
            print(f"\nDownloading clip {idx}")
            downloadClip(clip,f"clip{i}")
            print("\nClip downloaded!")
            i+=1
    except Exception as exc:
        logging.error(exc)
        print("An error occured while downloading the clips,stopping the execution")
        return
    
    print("\nAll clips Downloaded!\n\nCreating the video...\n\n")

    createVideo(save_path=iPath,channel=name,time=range)

    print("\n\n Video created!")

    return

if __name__ == '__main__':
    main()