#!/usr/bin/env python
from configparser import ConfigParser
import os

PATH = "./res/config.ini"

def initConf(bypass=False,verbose=False):
    global PATH
    if os.path.isfile(PATH) and not bypass:
        if verbose:
            print("Config file already exists, add argument bypass=True to overwrite it")
        return
    config_object = ConfigParser()
    config_object['OUTPUT'] = {
        "title":"clipsMontage"
    }
    config_object['RANKING']={
        "activate":"True",
        "time":"4",
        "font":"font",
        "fontSize":"120"
    }
    config_object['OUTRO']={
        "activate":"True",
        "text":"Thanks for watching, subscribe!",
        "time":"6",
        "font":"font",
        "fontSize":"120"
    }
    with open(PATH, 'w') as conf:
        config_object.write(conf)


#---OUTPUT---

def getOutputTitle():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["title"]
    except:
        raise Exception("Field does not exists!")
    return response

#---RANKING---

def getRankingSlide():
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

def getRankingSlideTime():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getRankingFontName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["font"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getRankingFontSize():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["fontSize"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

#---OUTRO---

def getOutro():
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

def getOutroText():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["text"]
    except:
        raise Exception("Field does not exists!")
    return response

def getOutroTime():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getOutroFontName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["font"]
    except:
        raise Exception("Field does not exists!")
    return int(response)
  
def getOutroFontSize():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["fontSize"]
    except:
        raise Exception("Field does not exists!")
    return int(response)