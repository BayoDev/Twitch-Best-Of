from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
from modules.clipEditor import Slide
import sys

def createTextSlide(slide):
    # Create and save a text slide based on the Slide object that is passed
    assert type(slide) == Slide
    # fontSize = int((slide.fontSize/1920)*slide.size[0])
    # font = ImageFont.truetype(f'./res/{slide.font_name}.ttf', slide.fontSize)
    if slide.customBg:
        image = Image.open(f"./res/{slide.bgName}")
        if image.size != slide.size:
            image = image.resize(slide.size)
    else:
        image = Image.new("RGB",slide.size,color=slide.bgColor)
    drawImage = ImageDraw.Draw(image)
    # w,h = drawImage.textsize(slide.text,font=font)
    # h+= int(h*0.21)

    # Taken from https://stackoverflow.com/a/61891053

    img_fraction = 0.7
    breakpoint = img_fraction * slide.size[0]
    jumpsize = 75
    fontsize = 1
    font = ImageFont.truetype(f'./res/{slide.font_name}.ttf', fontsize)
    while True:
        if font.getsize(slide.text)[0] < breakpoint:
            fontsize += jumpsize
        else:
            jumpsize = jumpsize // 2
            fontsize -= jumpsize
        font = ImageFont.truetype(f'./res/{slide.font_name}.ttf', fontsize)
        if jumpsize <= 1:
            break

    textWidth, textHeight = font.getsize(slide.text)

    drawImage.text(((slide.size[0]-textWidth)/2, (slide.size[1]-textHeight)/2),text=slide.text,fill=slide.txtColor,font=font)
    image.show()
    
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

size = (1280,720)    

createIntro(size)
createTransition(size,0)
createOutro(size)