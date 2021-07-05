#!/usr/bin/env python
from moviepy.editor import *
from PIL import Image,ImageDraw,ImageFont
from modules.configHandler import *

def getMaxDimension(file_path):
    import cv2
    heights = []
    widths = []
    for name in os.listdir(file_path):
        try:
            vid = cv2.VideoCapture(file_path+"/"+name)
            heights.append(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            widths.append(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        except:
            continue
    return (int(max(widths)),int(max(heights)))

def getDimension(file_name):
    import cv2
    vid = cv2.VideoCapture("./Clip/"+file_name)
    return vid.get(cv2.CAP_PROP_FRAME_WIDTH)

def getMaxFps(file_path):
    import cv2
    fps = []
    for name in os.listdir(file_path):
        try:
            vid = cv2.VideoCapture(file_path+"/"+name)
            fps.append(vid.get(cv2.CAP_PROP_FPS))
        except:
            continue
    return int(max(fps))
    
def createTextSlide(text,size,bgcolor=(0,0,0),txtcolor=(255,255,255),file_name="slide"):
    fontSize=int((90/1920)*size[0])
    fnt = ImageFont.truetype("./res/font.ttf",fontSize)
    slide = Image.new("RGB",size,color=bgcolor)
    d = ImageDraw.Draw(slide)
    w,h = d.textsize(text,font=fnt)
    h+= int(h*0.21)
    d.text(((size[0]-w)/2, (size[1]-h)/2),text=text,fill=txtcolor,font=fnt)
    slide.save(f"./Clips/{file_name}.png")


def createTransition(number,size):
    fontSize=int((120/1920)*size[0])
    if getCustomFont():
        fnt = ImageFont.truetype('./res/font.ttf', fontSize)
    else:
        fnt = None
    transition = Image.new('RGB', size, color = (0, 0, 0))
    d = ImageDraw.Draw(transition)
    w, h = d.textsize(f"Clip #{number}",font=fnt)
    h += int(h*0.21)    
    d.text(((size[0]-w)/2, (size[1]-h)/2), text=f"Clip #{number}", fill=(255,255,255), font=fnt)
    transition.save(f"./Clips/transition{number}.png")

def editClips(save_path="."):
    file_name = getOutputName()
    numberOfClips = sum([len(files) for r, d, files in os.walk("./Clips")])
    video_size = getMaxDimension("./Clips")
    video_fps = getMaxFps("./Clips")
    clipList =[]
    for i in range(numberOfClips,0,-1):
        if getRankingSlide():
            createTransition(i,video_size)
            imgList = []
            for s in range(video_fps*getRankingSlideTime()):
                imgList.append(f'./Clips/transition{i}.png')
            imgSequence = ImageSequenceClip(imgList,fps=video_fps)
            clipList.append(imgSequence)
        vid = VideoFileClip(f"./Clips/clip{i}.mp4")
        if getDimension(f"clip{i}.mp4") != video_size[0]:
                vid = vid.resize(width=video_size[0])
        clipList.append(vid)
    #   Create Outro
    if getOutro():
        createTextSlide(getOutroText(),video_size)
        imgList = []
        for s in range(video_fps*getOutroTime()):
            imgList.append(f'./Clips/slide.png')
        imgSequence = ImageSequenceClip(imgList,fps=video_fps)
        clipList.append(imgSequence)
    #   Concatenate clips
    final_clip = concatenate_videoclips(clipList)
    final_clip.write_videofile(f"{save_path}/{file_name}.mp4",fps=video_fps)
    
    
