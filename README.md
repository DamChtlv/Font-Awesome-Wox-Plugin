Wox.Plugin.FontAwesome
=====================

**Getting Font Awesome icons class made easy.**  
Finding icons is very fast because it searches in local JSON files (instead of an online API).

[![Screen 1](https://github.com/DamChtlv/Font-Awesome-Wox-Plugin/blob/assets/Screenshots/screen1.png)](#screen1)   

Features
---------
You can search through all icons styles and click to copy icon class : `fa close`  
*(if you click on *times*, you will have `fa-times` in your clipboard)*

Installation
---------
To install the plugin :
- Download the latest release of the plugin : https://github.com/DamChtlv/Font-Awesome-Wox-Plugin/releases/latest/download/Font.Awesome.zip
- Go to your folder `C:/Users/%USER%/AppData/Roaming/Wox/Plugins` then simply unzip the archive and you should have a folder named **Font Awesome**  
*Should be something like: `C:/Users/%USER%/AppData/Roaming/Wox/Plugins/Font Awesome/`*
- Restart **Wox** and type `Settings`
- Verify that you have correctly set the **Python** Path in **General** tab *(Python 3.5+ required)*  
*Should be something like: `C:/Users/%user%/AppData/Local/Programs/Python/Python37/`*  
- Go to the **Plugin** tab and look for **Font Awesome** plugin  
*If it doesn't show, either you put the plugin folder in the wrong directory or Wox can't find your python*
- You will need to install python module **pyperclip** *(for copying to clipboard)*  
*Type in your terminal:*  `pip3 install pyperclip`
- Type `fa` in **Wox** & wait few secs *(you will see the loading occuring while it's checking json file)*
- Enjoy ✌ 

Version
-------
*It's all based on **Font Awesome Pro 5.14 version** (2299 icons)* at the moment  

Credits
---------
This is inspired by / fork of [Font Awesome Workflow for Alfred](https://github.com/ruedap/alfred-font-awesome-workflow) (by [@ruedap](https://github.com/ruedap/)) **for Wox (Windows)** written in Python
