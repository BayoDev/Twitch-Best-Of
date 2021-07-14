#!/usr/bin/env python
from moviepy.editor import *
import requests as rs
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import urllib.request 
import os 

class Clip:
    def __init__(self,url,title):
        self.url = url
        self.title = title

def isChannel(name):
    # Return the availability of a channel
    data = getLoadedPageContent("https://twitch.tv/"+name,delay=15)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False

def getLoadedPageContent(url,delay=10):
    # Return the page source of the given {url} 
    # after waiting {delay} seconds for the page to load load
    try:
        options = webdriver.ChromeOptions()
    except:
        try:
            options=webdriver.Firefox()
        except:
            try:
                options= webdriver.Edge()
            except:
                raise Exception("An error occurred while loading the selenium webdriver")
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(delay)
    response = driver.page_source
    driver.quit()
    return response

def fetchClips(channel_name,range="7d",max=None):
    # Return an array of Clip object fetched on the channel 
    assert max==None or max > 0
    #Test internet connection
    test = rs.get("https://google.com")
    if not test.ok:
        raise Exception("Unable to connect to the internet")
    
    if range != "24h" and range != "7d" and range != "30d" and range != "all":
        raise Exception("Range not valid, allowed ranges: 24h, 7d, 30d, all")
    data = bs(getLoadedPageContent(f"https://www.twitch.tv/{channel_name}/clips?filter=clips&range={range}"),'html.parser')
    clips = data.findAll("article",{"class": "sc-AxjAm dBWNsP"})
    response = []
    for element in clips:
        response.append(Clip(f"https://www.twitch.tv"+element.find("a",{"data-a-target": "preview-card-image-link"})["href"],element.find("h3",{"class": "sc-AxirZ dqHsmV"})["title"]))
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

    
