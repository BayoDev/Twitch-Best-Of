# <p align="center">Twitch-Best-Of-Gen</p>

![GitHub](https://img.shields.io/github/license/BayoDev/Twitch-Best-Of-Gen)
![GitHub top language](https://img.shields.io/github/languages/top/BayoDev/Twitch-Best-Of-Gen)
![GitHub issues](https://img.shields.io/github/issues/BayoDev/Twitch-Best-Of-Gen)

>This program create a video with best clips of a channel, **ready to be posted!**

![Download repository](/Images/usage.gif)

## RIGHT NOW YOU MUST HAVE CHROME INSTALLED AND A COMPATIBLE WEB DRIVER, WE ARE WORKING ON A COMPATIBILITY PATCH AND AN INSTALLATION GUIDE

## Content:
1. [Installation](#inst)
2. [Usage](#usage)
3. [Customization](#custom)
4. [:warning:DISCLAIMER:warning:](#disclaimer)
5. [CREDITS](#credits)

<a name="inst"></a>
## Installation

1. Clone the directory
  ```git
  git clone https://github.com/BayoDev/Twitch-Best-Of-Gen.git
  ```
  __Or__
  
  ![Download repository](/Images/install.gif)
  
2. Unzip the file if compressed

3. Install requirements
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

You can customize some part of the code by modifying the config.ini file in the /res folder

OUTPUT | DESCRIPTION
------ | -----------
title  | Name of the output video
cmdOnly| Set this to true if can use only a cmd interface
oupath | This is used only if cmdOnly is True and set the directory where the final video will be saved

INTRO | DESCRIPTION
--------|------------
activate | True to enable
time | Duration in seconds 
font | Name of the font file without the extension(must be .ftt),must be positioned in /res
fontSize | The font-size of the text
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

RANKING | DESCRIPTION
--------|------------
activate | True to enable
time | Duration in seconds 
font | Name of the font file without the extension(must be .ftt),must be positioned in /res
fontSize | The font-size of the text
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

OUTRO | DESCRIPTION
--------|------------
activate | True to enable
text | Text displayed
time | Duration in seconds 
font | Name of the font file without the extension(must be .ftt),must be positioned in /res
fontSize | The font-size of the text
customBg | True to use a custom background image in the ranking slides
customBgFileName | Name of the file of the custom background image(must be in /res)

You can test how the font size of the config file will be displayed on the slides by using the testFont.py

While in the directory:
```cmd
python testFont.py
```

<a name="disclaimer"></a>
## :warning: DISCLAIMER :warning:

* We aren't connected in any way with the twitch company
* We do not take any responsability for any improper/illegal use of this program

<a name="credits"></a>
## CREDITS

* Created by **Giulio Venturini**
