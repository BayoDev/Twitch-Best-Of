#!/usr/bin/env python
from moviepy.editor import *
import requests as rs
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import urllib.request 
import os
import logging

class Clip:
    def __init__(self,url):
        self.url = url

def isChannel(name):
    # Return the availability of a channel
    data = getLoadedPageContent("https://twitch.tv/"+name,delay=15)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False

def isCategory(name):
    # Return the availability of a channel
    data = getLoadedPageContent("https://www.twitch.tv/directory/game/"+name,delay=15)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False

def getLoadedPageContent(url,delay=10,clicks=[]):
    # Return the page source of the given {url} 
    # after waiting {delay} seconds for the page to load load
    try:
        options = webdriver.ChromeOptions()
    except Exception as exc:
        logging.error(exc)
        raise Exception("An error occurred while loading the selenium webdriver")
    options.add_argument('headless')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(delay)
    if len(clicks)!=0:
        for el in clicks:
            div = driver.find_element_by_xpath(el)
            div.click()
    time.sleep(delay)
    response = driver.page_source
    driver.quit()
    return response

def fetchClipsCategory(cat_name,range="7d",max=None,languages=[]):
    # Return an array of Clip object fetched on the channel 
    assert max==None or max > 0
    #Test internet connection
    test = rs.get("https://google.com")
    if not test.ok:
        raise Exception("Unable to connect to the internet")
    
    if range != "24h" and range != "7d" and range != "30d" and range != "all":
        raise Exception("Range not valid, allowed ranges: 24h, 7d, 30d, all")
    language_codes = ["//button[@data-test-selector='language-select-menu__toggle-button']"]
    for lg in languages:
        language_codes.append(f'//div[@data-language-code="{lg}"]')
    data = bs(getLoadedPageContent(f"https://www.twitch.tv/directory/game/{cat_name}/clips?range={range}",clicks=language_codes),'html.parser')
    clips = data.findAll("article")
    response = []
    for element in clips:
        response.append(Clip(f"https://www.twitch.tv"+element.find("a",{"data-a-target": "preview-card-image-link"})["href"]))
    if max == None:
        return response
    else:
        if max > len(response):
            return response[:len(response)]
        else:
            return response[:max]

def fetchClipsChannel(channel_name,range="7d",max=None):
    # Return an array of Clip object fetched on the channel 
    assert max==None or max > 0
    #Test internet connection
    test = rs.get("https://google.com")
    if not test.ok:
        raise Exception("Unable to connect to the internet")
    
    if range != "24h" and range != "7d" and range != "30d" and range != "all":
        raise Exception("Range not valid, allowed ranges: 24h, 7d, 30d, all")
    data = bs(getLoadedPageContent(f"https://www.twitch.tv/{channel_name}/clips?filter=clips&range={range}"),'html.parser')
    clips = data.findAll("article")
    response = []
    for element in clips:
        response.append(Clip(f"https://www.twitch.tv"+element.find("a",{"data-a-target": "preview-card-image-link"})["href"]))
    if max == None:
        return response
    else:
        if max > len(response):
            return response[:len(response)]
        else:
            return response[:max]
        
def removeAllClips():
    # Remove all the clips and file contained in the "Clips" folder
    if os.path.isdir("./Clips"):
        for name in os.listdir('./Clips'):
            if os.path.isfile('./Clips/'+name):
                os.remove('./Clips/'+name)

def downloadClip(clip,fileName):
    # Download clip and save it in the ./Clips folder with the given fileName with mp4 extension
    assert type(clip) == Clip
    data = bs(getLoadedPageContent(clip.url),'html.parser')
    videoLink = data.find("video")["src"]
    if not os.path.isdir("./Clips"):
        os.mkdir("Clips")
    urllib.request.urlretrieve(videoLink, f'./Clips/{fileName}.mp4') 
    time.sleep(5)