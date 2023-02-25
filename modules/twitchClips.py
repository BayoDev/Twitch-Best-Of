#!/usr/bin/env python
from moviepy.editor import *
import requests as rs
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import urllib.request 
import os
import logging


class Clip:
    url: str            # Url of the clip
    title: str          # Title of the clip
    channelName: str    # Name of the channel
    duration: str       # Duration in seconds of the clip

    def __init__(self,url: str,title: str,channelName: str,duration: str):
        self.url = url
        self.title = title
        self.channelName = channelName
        self.duration = duration

    def print_info(self) -> None:
        print(f"\nTitle: {self.title}\nUrl: {self.url}\nChannel Name: {self.channelName}\nDuration: {self.duration}\n")

def is_channel(name: str) -> bool:
    # Return the availability of a channel
    data = get_loaded_page_content("https://twitch.tv/"+name+"/clips?filter=clips&range=all",type=None,delay=20)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False

def is_category(name: str) -> bool:
    # Return the availability of a channel
    data = get_loaded_page_content("https://www.twitch.tv/directory/game/"+name,type=None,delay=20)
    data = bs(data,'html.parser')
    doesExist = data.findAll("p",{"data-a-target":"core-error-message"})
    if len(doesExist)==0:
        return True
    else:
        return False


def get_loaded_page_content(url: str,type:str,clicks:list[str]=[],delay: int=None) -> str:
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
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements(By.TAG_NAME,'article'))!=0)
    if type=='clip':
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements(By.TAG_NAME,'video'))!=0)
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
            div = driver.find_element(By.XPATH,el)
            div.click()
    else:
        response = driver.page_source
        driver.quit()
        return response

    if type=='category':
        WebDriverWait(driver,60).until(lambda test : len(driver.find_elements(By.TAG_NAME,'article'))!=0)
    if type==None:
        time.sleep(delay)
            
    response = driver.page_source
    driver.quit()
    return response

def fetch_clips_category(cat_name: str,range: str="7d",max: int=None,languages: list[str]=[]) -> list[Clip]:
    # Return an array of Clip object fetched on the channel 
    assert max==None or max > 0
    #Test internet connection
    test = rs.get("https://google.com")
    if not test.ok:
        raise Exception("Unable to connect to the internet")
    
    if range != "24h" and range != "7d" and range != "30d" and range != "all":
        raise Exception("Range not valid, allowed ranges: 24h, 7d, 30d, all")
    language_codes = ['//*[@id="browse-root-filter-sort-options"]/div/div[2]/div[1]/div[1]/div/div/div[1]/button/div/div[2]/div']
    for lg in languages:
        language_codes.append(f'//div[@data-language-code="{lg}"]')
    data = bs(get_loaded_page_content(f"https://www.twitch.tv/directory/game/{cat_name}/clips?range={range}",type='category',clicks=language_codes),'html.parser')
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

def fetch_clips_channel(channel_name: str,range: str="7d",max: int=None) -> list[Clip]:
    # Return an array of Clip object fetched on the channel 
    assert max==None or max > 0
    #Test internet connection
    test = rs.get("https://google.com")
    if not test.ok:
        raise Exception("Unable to connect to the internet")
    
    if range != "24h" and range != "7d" and range != "30d" and range != "all":
        raise Exception("Range not valid, allowed ranges: 24h, 7d, 30d, all")
    data = bs(get_loaded_page_content(f"https://www.twitch.tv/{channel_name}/clips?filter=clips&range={range}",type='channel'),'html.parser')
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
        
def remove_all_clips() -> None:
    # Remove all the clips and file contained in the "Clips" folder
    if os.path.isdir("./Clips"):
        for name in os.listdir('./Clips'):
            if os.path.isfile('./Clips/'+name):
                os.remove('./Clips/'+name)

def download_clip(clip,fileName) -> None:
    # Download clip and save it in the ./Clips folder with the given fileName with mp4 extension
    assert type(clip) == Clip

    data = bs(get_loaded_page_content(clip.url,type='clip'),'html.parser')
    videoLink = data.find("video")["src"]
    if not os.path.isdir("./Clips"):
        os.mkdir("Clips")

    urllib.request.urlretrieve(videoLink, f'./Clips/{fileName}.mp4')