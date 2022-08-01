from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
from modules.clipEditor import Slide
from modules.cmd_logs import cls
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
    font = ImageFont.truetype(f'./res/{slide.fontName}.ttf', fontsize)
    while True:
        if font.getsize(slide.text)[0] < breakpoint:
            fontsize += jumpsize
        else:
            jumpsize = jumpsize // 2
            fontsize -= jumpsize
        font = ImageFont.truetype(f'./res/{slide.fontName}.ttf', fontsize)
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
                        fileName=f"intro",
                        fontName=get_intro_font_name(),
                        textRatio=get_intro_text_ratio(),
                        customBg=get_intro_custom_bg(),
                        bgName=get_intro_bg_name()))
    return

def create_transition(size,number):
    create_text_slide(Slide(text=f"Clip #{number}",
                        size=size,
                        fileName=f"transition{number}",
                        fontName=get_ranking_font_name(),
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

def main():
    slideSize = (1920,1080)
    selection = None
    while selection not in range(1,5):
        cls()
        print(f"\n\t FONT TESTER\n\n 1) Test INTRO\n 2) Test RANKING\n 3) Test OUTRO\n 4) Set size (current: {slideSize})\n 5) Quit\n")
        try:
            selection = int(input("Your choice: "))
        except:
            continue
        if selection == 1:
            create_intro(slideSize)
            selection = None
        if selection == 2:
            create_transition(slideSize,10)
            selection = None
        if selection == 3:
            create_outro(slideSize)
            selection = None
        if selection == 4:
            while True:
                old = slideSize
                try:
                    cls()
                    print("\n\t Enter slide size\n")
                    slideSize = (int(input(" Width: ")),int(input("\n Height: ")))
                    selection = None
                    break
                except:
                    slideSize = old

        if selection == 5:
            exit()



if __name__ == '__main__':
    main()