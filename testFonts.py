from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
from modules.clipEditor import Slide
import sys

def createTextSlide(slide):
    fontSize=int((slide.fontSize/1920)*slide.size[0])
    fnt = ImageFont.truetype(f'./res/{slide.font_name}.ttf', slide.fontSize)
    if slide.customBg:
        tr = Image.open(f"./res/{slide.bgName}")
        if tr.size != slide.size:
            tr = tr.resize(slide.size)
    else:
        tr = Image.new("RGB",slide.size,color=slide.bgColor)
    d = ImageDraw.Draw(tr)
    w,h = d.textsize(slide.text,font=fnt)
    h+= int(h*0.21)
    d.text(((slide.size[0]-w)/2, (slide.size[1]-h)/2),text=slide.text,fill=slide.txtColor,font=fnt)
    tr.show()
    
def createIntro(size,numberOfClips=10,channel="channel",time="all"):
    if time == "24h":
        time_period="the day"
    if time == "7d":
        time_period="the week"
    if time=="30d":
        time_period="the month"
    if time == "all":
        time_period="all time"
    createTextSlide(Slide(text=f"Top {numberOfClips} best {channel}'s clips of {time_period}",
                        size=size,
                        file_name=f"intro",
                        font_name=getIntroFontName(),
                        fontSize=getIntroFontSize(),
                        customBg=getIntroCustomBg(),
                        bgName=getIntroBgName()))
    return

def createTransition(size,number):
    createTextSlide(Slide(text=f"Clip #{number}",
                        size=size,
                        file_name=f"transition{number}",
                        font_name=getRankingFontName(),
                        fontSize=getRankingFontSize(),
                        customBg=getRankingCustomBg(),
                        bgName=getRankingBgName()))
    return

def createOutro(size):
    createTextSlide(Slide(text=getOutroText(),
                        size=size,
                        file_name="outro",
                        font_name=getOutroFontName(),
                        fontSize=getOutroFontSize(),
                        customBg=getOutroCustomBg(),
                        bgName=getOutroBgName()))
    return

size = (1920,1080)    

createIntro(size)
createTransition(size,0)
createOutro(size)