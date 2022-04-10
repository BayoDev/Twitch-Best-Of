#!/usr/bin/env python
from modules.twitchClips import *
from modules.clipEditor import *
from modules.configHandler import *
from modules.input_handler import *
from modules.cmd_logs import *
import os
import logging
from tqdm import tqdm

def removeOldFiles():
    # Delete temporary file that may still exist if the program was
    # interrupted during the editing of the clips
    try:
        if os.path.isfile(getOutputTitle()+"TEMP_MPY_wvf_snd.mp3"):
            os.remove(getOutputTitle()+"TEMP_MPY_wvf_snd.mp3")
        removeAllClips()
    except:
        return


def main(automated=False,name=None,nclips=None,range=None,iPath=None,type=None,langs=None):
    if automated:
        right,iPath = checkInputs(name,nclips,range,iPath,type,langs)
        if not right:
            return False

    initConf(verbose=False)

    initLog()

    logging.basicConfig(level=10,filename="log.txt",filemode='w')

    removeOldFiles()

    if not automated:
        name,nclips,range,iPath,type,langs = getInputs()

    cls()

    info("Fetching data")

    if type == 1:
        data = fetchClipsChannel(name,max=nclips,range=range)
    elif type == 2:
        data = fetchClipsCategory(name,max=nclips,range=range,languages=langs)

    i = 1
    log("Data fetched")
    info("Downloading clips")
    
    try:
        for clip in tqdm(data):
            downloadClip(clip,f"clip{i}")
            i+=1
    except Exception as exc:
        logging.error(exc)
        log("Error while downloading the clips",success=False)
        return False
    
    log("All clips downloaded")
    info("Creating the video")

    createVideo(save_path=iPath,channel=name,time=range)

    log("Video created")
    info("Interrupting the execution")

    return True

if __name__ == '__main__':
    main()