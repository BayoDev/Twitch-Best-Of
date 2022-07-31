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

def remove_old_files() -> None:
    # Delete temporary file that may still exist if the program was
    # interrupted during the editing of the clips
    try:
        if os.path.isfile(get_output_title()+"TEMP_MPY_wvf_snd.mp3"):
            os.remove(get_output_title()+"TEMP_MPY_wvf_snd.mp3")
        remove_all_clips()
    except:
        return


def main(
    automated: bool=False,
    name: str=None,
    nclips: int=None,
    range_in: str=None,
    iPath: str=None,
    type: str=None,
    langs: list=None
    ) -> None:
    if automated:
        right,iPath = check_inputs(name,nclips,range_in,iPath,type,langs)
        if not right:
            return False

    config_init(verbose=False)

    initLog()

    logging.basicConfig(level=10,filename="log.txt",filemode='w')

    remove_old_files()

    if not automated:
        name,nclips,range_in,iPath,type,langs = get_inputs()

    cls()

    info("Fetching data")

    if type == 1:
        data = fetch_clips_channel(name,max=nclips,range=range_in)
    elif type == 2:
        data = fetch_clips_category(name,max=nclips,range=range_in,languages=langs)

    i = 1
    log("Data fetched")
    info("Downloading clips")
    
    try:
        threads = []
        for clip in data:
            threads.append(threading.Thread(target=download_clip,args=(clip,f"clip{i}")))
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

    create_video(save_path=iPath,channel=name,time=range_in)

    log("Video created")
    info("Interrupting the execution")

    return True

if __name__ == '__main__':
    main()