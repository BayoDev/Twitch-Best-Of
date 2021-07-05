# <p align="center">Twitch-Best-Of-Gen</p>

![GitHub](https://img.shields.io/github/license/BayoDev/Twitch-Best-Of-Gen)
![GitHub top language](https://img.shields.io/github/languages/top/BayoDev/Twitch-Best-Of-Gen)
![GitHub issues](https://img.shields.io/github/issues/BayoDev/Twitch-Best-Of-Gen)

>This program create a video with best clips of a channel, **ready to be posted!**

![Download repository](/Images/usage.gif)

## RIGHT NOW YOU MUST HAVE CHROME INSTALLED AND A COMPATIBLE WEB DRIVER
## WE ARE WORKING ON A COMPATIBILITY PATCH AND AN INSTALLATION GUIDE

## Content:
1. [Installation](#inst)
2. [Usage](#usage)
3. [Customization](#custom)
4. [DISCLAIMER](#disclaimer)
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

You can customize some part of the code by modifying the config.ini file in /res

OPTION | DESCRIPTION
------ | -----------
title  | Name of the output video
ranking_slide | Abilitate[True]/Disabilitate[False] the ranked slides in beetwen clips
ranking_slide_time | Duration of ranked slides in seconds
outro | Abilitate[True]/Disabilitate[False] the outro slide
outro_text | The text displayed in the outro slide
outro_time | Duration of the outro slide
customFont | Abilitate[True]/Disabilitate[False] the usage of a custom font(more details in the config file)

<a name="disclaimer"></a>
## DISCLAIMER

* We aren't connected in any way with the twitch company
* We do not take any responsability for any improper/illegal use of this program

<a name="credits"></a>
## CREDITS

* Created by **Giulio Venturini**
