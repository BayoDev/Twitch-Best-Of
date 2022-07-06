#!/usr/bin/env python
from modules.twitchClips import *
from modules.clipEditor import *
from modules.configHandler import *
from modules.input_handler import *
from modules.cmd_logs import *
import threading
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


def main(automated=False,name=None,nclips=None,range_in=None,iPath=None,type=None,langs=None):
    if automated:
        right,iPath = checkInputs(name,nclips,range_in,iPath,type,langs)
        if not right:
            return False

    initConf(verbose=False)

    initLog()

    logging.basicConfig(level=10,filename="log.txt",filemode='w')

    removeOldFiles()

    if not automated:
        name,nclips,range_in,iPath,type,langs = getInputs()

    cls()

    info("Fetching data")

    if type == 1:
        data = fetchClipsChannel(name,max=nclips,range=range_in)
    elif type == 2:
        data = fetchClipsCategory(name,max=nclips,range=range_in,languages=langs)

    i = 1
    log("Data fetched")
    info("Downloading clips")
    
    try:
        threads = []
        for clip in data:
            threads.append(threading.Thread(target=downloadClip,args=(clip,f"clip{i}")))
            i+=1
        for tr in threads:
            tr.start()
        for i in tqdm(range(len(data))):
            condition = True
            while condition:
                for tr in threads:
                    if not tr.is_alive():
                        threads.remove(tr)
                        condition = False
                        continue
    except Exception as exc:
        logging.error(exc)
        log("Error while downloading the clips",success=False)
        return False
    
    log("All clips downloaded")
    info("Creating the video")

    createVideo(save_path=iPath,channel=name,time=range_in)

    log("Video created")
    info("Interrupting the execution")

    return True

if __name__ == '__main__':
    main()