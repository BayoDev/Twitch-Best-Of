from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
from modules.clipEditor import Slide
import sys

def create_text_slide(slide):
    # Create and save a text slide based on the Slide object that is passed
    assert type(slide) == Slide

    if slide.customBg:
        image = Image.open(f"./res/{slide.bgName}")
        if image.size != slide.size:
            image = image.resize(slide.size)
    else:
        image = Image.new("RGB",slide.size,color=slide.bgColor)
    drawImage = ImageDraw.Draw(image)

    # Taken from https://stackoverflow.com/a/61891053

    img_fraction = slide.textRatio
    breakpoint = img_fraction * slide.size[0]
    jumpsize = 50
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
    
def create_intro(size,numberOfClips=10,channel="channel",time="all"):
    if time == "24h":
        time_period="the day"
    if time == "7d":
        time_period="the week"
    if time=="30d":
        time_period="the month"
    if time == "all":
        time_period="all time"
    create_text_slide(Slide(text=f"Top {numberOfClips} best {channel}'s clips of {time_period}",
                        size=size,
                        file_name=f"intro",
                        font_name=get_intro_font_name(),
                        textRatio=get_intro_text_ratio(),
                        customBg=get_intro_custom_bg(),
                        bgName=get_intro_bg_name()))
    return

def create_transition(size,number):
    create_text_slide(Slide(text=f"Clip #{number}",
                        size=size,
                        file_name=f"transition{number}",
                        font_name=get_ranking_font_name(),
                        textRatio=get_ranking_text_ratio(),
                        customBg=get_ranking_custom_bg(),
                        bgName=get_ranking_bg_name()))
    return

def create_outro(size):
    create_text_slide(Slide(text=get_outro_text(),
                        size=size,
                        fileName="outro",
                        fontName=get_outro_font_name(),
                        textRatio=get_outro_text_ratio(),
                        customBg=get_outro_custom_bg(),
                        bgName=get_outro_bg_name()))
    return

size = (1280,720)    

create_intro(size)
create_transition(size,0)
create_outro(size)