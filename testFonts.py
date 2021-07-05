from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
import sys

def createTextSlide(text,size,bgcolor=(0,0,0),txtcolor=(255,255,255),file_name="slide",fontSize=100):
    fontSize=int((getFontSize()/1920)*size[0])
    if getCustomFont():
        fnt = ImageFont.truetype('./res/font.ttf', fontSize)
    else:
        fnt = None
    slide = Image.new("RGB",size,color=bgcolor)
    d = ImageDraw.Draw(slide)
    w,h = d.textsize(text,font=fnt)
    h+= int(h*0.21)
    d.text(((size[0]-w)/2, (size[1]-h)/2),text=text,fill=txtcolor,font=fnt)
    slide.show()


def createTransition(number,size,fontSize):
    fontSize=int((getFontSize()/1920)*size[0])
    if getCustomFont():
        fnt = ImageFont.truetype('./res/font.ttf', fontSize)
    else:
        fnt = None
    transition = Image.new('RGB', size, color = (0, 0, 0))
    d = ImageDraw.Draw(transition)
    w, h = d.textsize(f"Clip #{number}",font=fnt)
    h += int(h*0.21)    
    d.text(((size[0]-w)/2, (size[1]-h)/2), text=f"Clip #{number}", fill=(255,255,255), font=fnt)
    transition.show()


createTransition(1,(1920,1080),getFontSize())

createTextSlide(getOutroText(),(1920,1080),getFontSize())