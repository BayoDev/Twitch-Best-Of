#!/usr/bin/env python
from moviepy.editor import *
import requests as rs
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import urllib.request 
import os
import logging

class Clip:
    url: str
    title: str
    channelName: str
    duration: str

    def __init__(self,url: str,title: str,channelName: str,duration: str):
        self.url = url
        self.title = title
        self.channelName = channelName
        self.duration = duration

    def print_info(self) -> None:
        print(f"\nTitle: {self.title}\nUrl: {self.url}\nChannel Name: {self.channelName}\nDuration: {self.duration}\n")

def isChannel(name):
    # Return the availability of a channel
    data = getLoadedPageContent("https://twitch.tv/"+name+"/clips?filter=clips&range=all",type=None,delay=20)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False

def isCategory(name):
    # Return the availability of a channel
    data = getLoadedPageContent("https://www.twitch.tv/directory/game/"+name,type=None,delay=20)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False


def getLoadedPageContent(url: str,type:str,clicks:list=[],delay: int=None):
    # Return the page source of the given {url} 
    # after waiting {delay} seconds for the page to load load
    # type = channel | clip | category | None
    
    try:
        options = webdriver.ChromeOptions()
    except Exception as exc:
        logging.error(exc)
        raise Exception("An error occurred while loading the selenium webdriver")
    options.add_argument('headless')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    if type=='channel' or type=='category':
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements_by_tag_name('article'))!=0)
    if type=='clip':
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements_by_tag_name('video'))!=0)
        ready = False
        while not ready:
            html_data = bs(driver.page_source,'html.parser')
            ready = True
            try:
                html_data.find("video")["src"]
            except:
                ready = False
    if type==None:
        time.sleep(delay)
        
    if len(clicks)!=0:
        for el in clicks:
            div = driver.find_element_by_xpath(el)
            div.click()
    else:
        response = driver.page_source
        driver.quit()
        return response

    if type=='category':
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements_by_tag_name('article'))!=0)
    if type==None:
        time.sleep(delay)
            
    response = driver.page_source
    driver.quit()
    return response
'''

def getLoadedPageContent(url,clicks=[],delay:int=None, type: str=None):
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
    if delay != None:
        time.sleep(delay)
    else:
        WebDriverWait(driver,20).until(lambda test : len(driver.find_elements_by_tag_name('article'))!=0)
    if len(clicks)!=0:
        for el in clicks:
            div = driver.find_element_by_xpath(el)
            div.click()
    if delay != None:
        time.sleep(delay)
    else:
        if len(clicks)!=0 and not type=='category':
            WebDriverWait(driver,20).until(lambda test : len(driver.find_elements_by_tag_name('video'))!=0)
        if type =='category':
            WebDriverWait(driver,20).until(lambda test : len(driver.find_elements_by_tag_name('article'))!=0)
    response = driver.page_source
    driver.quit()
    return response
''' 

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
    data = bs(getLoadedPageContent(f"https://www.twitch.tv/directory/game/{cat_name}/clips?range={range}",type='category',clicks=language_codes),'html.parser')
    clips = data.findAll("article")
    response = []
    for element in clips:
        response.append(Clip(f"https://www.twitch.tv"+element.find("a",{"data-a-target": "preview-card-image-link"})["href"],element.find("h3").text,element.find("a",{"data-a-target": "preview-card-channel-link"}).text,element.find("a",{"data-a-target": "preview-card-image-link"}).find("div").findAll("div")[2].find("div").text))
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
    data = bs(getLoadedPageContent(f"https://www.twitch.tv/{channel_name}/clips?filter=clips&range={range}",type='channel'),'html.parser')
    clips = data.findAll("article")
    response = []
    for element in clips:
        response.append(Clip(f"https://www.twitch.tv"+element.find("a",{"data-a-target": "preview-card-image-link"})["href"],element.find("h3").text,element.find("a",{"data-a-target": "preview-card-channel-link"}).text,element.find("a",{"data-a-target": "preview-card-image-link"}).find("div").findAll("div")[2].find("div").text))
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

    data = bs(getLoadedPageContent(clip.url,type='clip'),'html.parser')
    videoLink = data.find("video")["src"]
    if not os.path.isdir("./Clips"):
        os.mkdir("Clips")

    urllib.request.urlretrieve(videoLink, f'./Clips/{fileName}.mp4')