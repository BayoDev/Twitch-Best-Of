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
    config_object['OPTIONS'] = {
        "title":"clipsMontage",
        "ranking_slide":"True",
        "ranking_slide_time" : "4",
        "outro":"True",
        "outro_text":"Thanks for watching, subscribe!",
        "outro_time" : "6",
        "customFont" : "False"
    }
    with open(PATH, 'w') as conf:
        config_object.write(conf)


def getOutputName():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["title"]
    except:
        raise Exception("Field does not exists!")
    return response

def getRankingSlide():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["ranking_slide"]
    except:
        raise Exception("Field does not exists!")
    return response

def getRankingSlideTime():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["ranking_slide_time"]
    except:
        raise Exception("Field does not exists!")
    return response

def getOutro():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["outro"]
    except:
        raise Exception("Field does not exists!")
    return response

def getOutroText():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["outro_text"]
    except:
        raise Exception("Field does not exists!")
    return response

def getOutroTime():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["outro_time"]
    except:
        raise Exception("Field does not exists!")
    return response

def getCustomFont():
    global PATH
    config_object = ConfigParser()
    config_object.read(PATH)
    try:
        response = config_object["OPTIONS"]["customFont"]
    except:
        raise Exception("Field does not exists!")
    return response
