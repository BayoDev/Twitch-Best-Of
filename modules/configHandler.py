#!/usr/bin/env python
from configparser import ConfigParser
import os
from .cmd_logs import *

PATH = "./res/config.ini"

def config_init(bypass: bool=False,verbose: bool=False) -> None:
    # Initialize Config file
    # If bypass=True set config file to default values
    global PATH
    if os.path.isfile(PATH) and not bypass:
        if verbose:
            info("Config file already exists, add argument bypass=True to overwrite it")
        return
    config_object = ConfigParser()
    config_object['OUTPUT'] = {
        "title":"clipsMontage",
        "cmdOnly":"False",
        "outPath":".",
        "autoRes": True,
        "widthRes": 1920,
        "heightRes": 1080
    }
    config_object['INTRO']={
        "activate":"False",
        "time":"5",
        "font":"font",
        "textToImageRatio":"0.7",
        "customBg":"False",
        "customBgFileName":"test.jpg"
    }
    config_object['RANKING']={
        "activate":"True",
        "time":"4",
        "font":"font",
        "textToImageRatio":"0.4",
        "customBg":"False",
        "customBgFileName":"test.jpg"
    }
    config_object['OUTRO']={
        "activate":"False",
        "text":"Thanks for watching, subscribe!",
        "time":"6",
        "font":"font",
        "textToImageRatio":"0.7",
        "customBg":"False",
        "customBgFileName":"test.jpg"
    }
    with open(PATH, 'w') as conf:
        config_object.write(conf)


#---OUTPUT---

def get_output_title():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["title"]
    except:
        raise Exception("Field does not exists!")
    return response

def get_cmd_only():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["cmdOnly"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_out_path():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["outPath"]
    except:
        raise Exception("Field does not exists!")
    return response

def get_auto_res():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["autoRes"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_width_res():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["widthRes"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def get_height_res():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["heightRes"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

#---INTRO---

def get_intro_slide():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["activate"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_intro_time():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def get_intro_font_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["font"]
    except:
        raise Exception("Field does not exists!")
    return response

def get_intro_text_ratio():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["textToImageRatio"]
    except:
        raise Exception("Field does not exists!")
    return float(response)

def get_intro_custom_bg():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["customBg"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_intro_bg_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["customBgFileName"]
    except:
        raise Exception("Field does not exists!")
    return response

#---RANKING---

def get_ranking_slide():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["activate"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_ranking_time():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def get_ranking_font_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["font"]
    except:
        raise Exception("Field does not exists!")
    return response

def get_ranking_text_ratio():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["textToImageRatio"]
    except:
        raise Exception("Field does not exists!")
    return float(response)

def get_ranking_custom_bg():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["customBg"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_ranking_bg_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["customBgFileName"]
    except:
        raise Exception("Field does not exists!")
    return response

#---OUTRO---

def get_outro_slide():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["activate"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_outro_text():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["text"]
    except:
        raise Exception("Field does not exists!")
    return response

def get_outro_time():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def get_outro_font_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["font"]
    except:
        raise Exception("Field does not exists!")
    return response
  
def get_outro_text_ratio():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["textToImageRatio"]
    except:
        raise Exception("Field does not exists!")
    return float(response)

def get_outro_custom_bg():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["customBg"]
    except:
        raise Exception("Field does not exists!")
    if response == "False":
        response=False
        return response
    if response == "True":
        response=True
        return response
    raise Exception("Error in config file")

def get_outro_bg_name():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["customBgFileName"]
    except:
        raise Exception("Field does not exists!")
    return response

