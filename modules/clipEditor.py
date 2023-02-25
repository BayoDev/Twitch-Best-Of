#!/usr/bin/env python
from moviepy.editor import *
from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *
from .configHandler import *
import random

class Slide:

    text: str           # Text Displayed in the Slide
    size: tuple         # Size of the Slide as as a tuple (width,height)
    bgColor: tuple      # Color of the background  as a tuple (R,G,B)
    txtColor: tuple     # Color of the text as a tuple (R,G,B) 
    fileName: str       # File name of the Slide file , without extension
    fontName: str       # Name of the Font file used for the text without the extension,
                        #   must be in the /res folder and be a ttf file
    textRatio: float    # Font size of the text in the Slide
    customBg = bool     # {True|False} Use Custom Background
    bgName: str         # Name of the image file used as background with the extension, must be in /res folder

    def __init__(self,
                text: str="Test",
                size: tuple=(1920,1080),
                bgColor: tuple=(0,0,0),
                txtColor: tuple=(255,255,255),
                fileName :str=f"slide{random.randrange(1000)}",
                fontName :str="font",
                textRatio :float=0.5,
                customBg=False,
                bgName=None
    ):
        self.text=text                  
        self.size=size                    
        self.bgColor=bgColor            
        self.txtColor=txtColor          
        self.fileName=fileName        
        self.fontName = fontName      
        self.textRatio = textRatio      
        self.customBg=customBg          
        self.bgName=bgName              
        


def get_max_dimensions(filePath: str) -> tuple:
    # Return the max dimension among the video file 
    # in the filePath folder as a tuplet (width,height)
    if not get_auto_res():
        return (get_width_res(),get_height_res())
    import cv2
    heights = []
    widths = []
    for name in os.listdir(filePath):
        try:
            vid = cv2.VideoCapture(filePath+"/"+name)
            heights.append(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            widths.append(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        except:
            continue
    return (int(max(widths)),int(max(heights)))

def get_video_dimension(fileName: str) -> int:
    # Return Width of a video file named fileName contained in the ./Clips folder
    import cv2
    vid = cv2.VideoCapture("./Clips/"+fileName)
    return (vid.get(cv2.CAP_PROP_FRAME_WIDTH),vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

def get_max_fps(filePath: str) -> int:
    # Return the highest fps among the video file contained in the filePath folder
    import cv2
    fps = []
    for name in os.listdir(filePath):
        try:
            vid = cv2.VideoCapture(filePath+"/"+name)
            fps.append(vid.get(cv2.CAP_PROP_FPS))
        except:
            continue
    return int(max(fps))
    
def create_text_slide(slide: Slide) -> None:
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
    image.save(f"./Clips/{slide.fileName}.png")
    
def create_intro(size: tuple,video_fps: int,numberOfClips: int,channel: str,time: str) -> ImageSequenceClip:
    # Return an intro slide as an ImageSequenceClip  object
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
    imgList = []
    for i in range(video_fps*get_intro_time()):
        imgList.append('./Clips/intro.png')
    return ImageSequenceClip(imgList,fps=video_fps)

def create_transition(size: tuple,video_fps: int,number: int) -> ImageSequenceClip:
    # Return an in-clip-transition as an ImageSequenceClip object
    create_text_slide(Slide(text=f"Clip #{number}",
                        size=size,
                        fileName=f"transition{number}",
                        fontName=get_ranking_font_name(),
                        textRatio=get_ranking_text_ratio(),
                        customBg=get_ranking_custom_bg(),
                        bgName=get_ranking_bg_name()))
    imgList = []
    for s in range(video_fps*get_ranking_time()):
        imgList.append(f'./Clips/transition{number}.png')
    return ImageSequenceClip(imgList,fps=video_fps)

def create_outro(size: tuple,video_fps: int) -> ImageSequenceClip:
    # Return an outro as an ImageSequenceClip object
    create_text_slide(Slide(text=get_outro_text(),
                        size=size,
                        fileName="outro",
                        fontName=get_outro_font_name(),
                        textRatio=get_outro_text_ratio(),
                        customBg=get_outro_custom_bg(),
                        bgName=get_outro_bg_name()))
    imgList = []
    for s in range(video_fps*get_outro_time()):
        imgList.append('./Clips/outro.png')
    return ImageSequenceClip(imgList,fps=video_fps)
    

def create_video(save_path: str=".",channel: str=None,time: str="7d") -> None:

    # Create and save the final video 

    file_name = get_output_title()
    numberOfClips = sum([len(files) for r, d, files in os.walk("./Clips")])
    video_size = get_max_dimensions("./Clips")
    video_fps = get_max_fps("./Clips")
    clipList =[]
    #---INTRO---
    if get_intro_slide():
        clipList.append(create_intro(video_size,video_fps,numberOfClips,channel,time))

    #---Clips and transitions---
    for i in range(numberOfClips,0,-1):
        if get_ranking_slide():
            clipList.append(create_transition(video_size,video_fps,i))
        vid = VideoFileClip(f"./Clips/clip{i}.mp4",fps_source='fps')
        if get_video_dimension(f"clip{i}.mp4") != video_size:
                vid = vid.resize(video_size)
        clipList.append(vid)
    
    #---Outro---
    if get_outro_slide():
        clipList.append(create_outro(video_size,video_fps))
    #   Concatenate clips
    final_clip = concatenate_videoclips(clipList)
    final_clip.write_videofile(f"{save_path}/{file_name}.mp4",fps=video_fps)