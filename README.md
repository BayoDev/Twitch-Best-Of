# <p align="center">Twitch-Best-Of-Gen</p>

![GitHub](https://img.shields.io/github/license/BayoDev/Twitch-Best-Of-Gen)
![GitHub top language](https://img.shields.io/github/languages/top/BayoDev/Twitch-Best-Of-Gen)
![GitHub issues](https://img.shields.io/github/issues/BayoDev/Twitch-Best-Of-Gen)

>This program create a video scraping the best clips of a channel or category **ready to be posted** without using a token!

![Download repository](/Images/usage.gif)

## Content:
1. [Installation](#inst)
2. [Usage](#usage)
3. [Customization](#custom)
4. [:warning:DISCLAIMER:warning:](#disclaimer)
5. [CREDITS](#credits)

<a name="inst"></a>
## Installation

### 0. *Make sure to have chrome installed and a compatible webdriver installed and added to PATH*, a guide can be found <a href='https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/'>here</a>
<br>

### 1. Clone the directory
  ```git
  git clone https://github.com/BayoDev/Twitch-Best-Of-Gen.git
  ```
  __Or__
  
  ![Download repository](/Images/install.gif)
  

### 2. Unzip the file if compressed


### 3. Install requirements
  ```git
  cd Twitch-Best-Of-main
  ```
  > If installed via git the name of the folder may vary
  ```pip
  pip install -r requirements.txt
  ```
  
  

<a name="usage"></a>
## Usage

> **You must be in the directory to run the program!**

```python
python main.py
```

Follow the steps of the program to create your video!

<a name="custom"></a>
## Customize

You can customize some part of the video by modifying the config.ini file in the /res folder
> The file is created the first time that you run the program

OUTPUT | DESCRIPTION
------ | -----------
title  | Name of the output video
cmdOnly| Set this to true if can use only a cmd interface
outPath | This is used only if cmdOnly is True and set the directory where the final video will be saved
autoRes | False to disable
widthEes | Width resolution of the video if autoRes is disabled
heightRes | Height resolution of the video if autoRes is disabled

INTRO | DESCRIPTION
--------|------------
activate | True to enable
time | Duration in seconds 
font | Name of the font file without the extension(must be .ttf),must be positioned in /res
textRatio | The ratio of the width of the text compared to the width of the frame
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

RANKING | DESCRIPTION
--------|------------
activate | True to enable
time | Duration in seconds 
font | Name of the font file without the extension(must be .ttf),must be positioned in /res
textRatio | The ratio of the width of the text compared to the width of the frame
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

OUTRO | DESCRIPTION
--------|------------
activate | True to enable
text | Text displayed
time | Duration in seconds 
font | Name of the font file without the extension(must be .ttf),must be positioned in /res
textRatio | The ratio of the width of the text compared to the width of the frame
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

You can test how the font size of the config file will be displayed on the slides by using the testFont.py

While in the directory:
```cmd
python testFont.py
```

<a name="disclaimer"></a>
## :warning: DISCLAIMER :warning:

* Your IP could be banned by Twitch, use the program **at your own risk!**
* We aren't connected in any way with the twitch company
* We do not take any responsability for any improper/illegal use of this program


<a name="credits"></a>
## CREDITS

* Created by **Giulio Venturini**
