#!/usr/bin/env python
from configparser import ConfigParser
import os
import logging

PATH = "./res/config.ini"

def initConf(bypass=False,verbose=False):
    # Initialize Config file
    # If bypass=True set config file to default values
    global PATH
    if os.path.isfile(PATH) and not bypass:
        if verbose:
            print("Config file already exists, add argument bypass=True to overwrite it")
        return
    config_object = ConfigParser()
    config_object['OUTPUT'] = {
        "title":"clipsMontage",
        "cmdOnly":"False",
        "outPath":"." 
    }
    config_object['INTRO']={
        "activate":"False",
        "time":"5",
        "font":"font",
        "fontSize":"90",
        "customBg":"False",
        "customBgFileName":"test.jpg"
    }
    config_object['RANKING']={
        "activate":"True",
        "time":"4",
        "font":"font",
        "fontSize":"120",
        "customBg":"False",
        "customBgFileName":"test.jpg"
    }
    config_object['OUTRO']={
        "activate":"False",
        "text":"Thanks for watching, subscribe!",
        "time":"6",
        "font":"font",
        "fontSize":"120",
        "customBg":"False",
        "customBgFileName":"test.jpg"
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

def getCmdOnly():
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

def getOutPath():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTPUT"]["outPath"]
    except:
        raise Exception("Field does not exists!")
    return response


#---INTRO---

def getIntro():
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

def getIntroTime():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["time"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getIntroFontName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["font"]
    except:
        raise Exception("Field does not exists!")
    return response

def getIntroFontSize():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["fontSize"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getIntroCustomBg():
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

def getIntroBgName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["INTRO"]["customBgFileName"]
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

def getRankingTime():
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
    return response

def getRankingFontSize():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["fontSize"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getRankingCustomBg():
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

def getRankingBgName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["RANKING"]["customBgFileName"]
    except:
        raise Exception("Field does not exists!")
    return response

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
    return response
  
def getOutroFontSize():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["fontSize"]
    except:
        raise Exception("Field does not exists!")
    return int(response)

def getOutroCustomBg():
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

def getOutroBgName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OUTRO"]["customBgFileName"]
    except:
        raise Exception("Field does not exists!")
    return response

