# I.V.A

**I**ntegrated **V**oice **A**ssistant or **I.V.A** is a desktop assistant Developed in python. It uses Microsoft Speech API (SAPI5) precisely to perform speech recognition and speech synthesis within Windows. It's a console prototype.  

## Requirements

i) Python and it's libraries. <br/>
ii) Source Code editor (Since it's a console app) <br/>
ii) Windows 10 x64. <br/>

## Install Requirements
### Install Python
i) Go to "**https://www.python.org/**". Hover over "Downloads" Then Click "Python 3.8.0". (Note: Always download the executable installer) <br/> <br/>
ii) After Downloading Installer. Open it. <br/> <br/>
iii) While installing check on **Add Python 3.8 to path** <br/> <br/>
iv) Also adjust system variables. <br/><br/>

### Install Python Libraries
i) Upgrade pip by "**python -m pip install --upgrade pip --user**". <br/><br/>
ii)  Install '**pyttsx3**'.<br/>
  - To install it go to cmd. (To open cmd use "**windows+r**" then type cmd then "**Enter**") <br/>
  - Then Type "**python -m pip install pyttsx3 --user**". <br/> <br/>

iii) Install '**SpeechRecognition**' by using command '**python -m pip install SpeechRecognition --user**' <br/><br/>
iv) Install '**wikipedia**' by using command '**python -m pip install wikipedia --user**' <br/><br/>
v) Install '**google**' by using command '**python -m pip install google --user**'<br/><br/>
vi) Solve '**pywin32**' error by copying '**pythoncom38.dll**' and '**pywintypes38.dll**' from "**C:\Python38\Lib\site-packages\pywin32_system32**" to "**C:\Python38\Lib\site-packages\win32**" <br/><br/>
vii) Install '**PyAudio**'. Go to **https://www.lfd.uci.edu/~gohlke/pythonlibs/** and download wheel file for PyAudio. Then go to download directory and open cmd in that folder. THen type '**python -m pip install (filename.whl) --user**' <br/>  <br/>

## Project Design

## Commands it can execute 
- "***Wikipedia***" command allows the system to read 3 lines from designated wikipedia page.Ex: "***wikipedia*** Alan turing" <br/>
- "***Tell***" command allows the system to describe basic info about the topic. Ex: "***Tell*** me about Alan Turing". <br/>
- "***open google***" command allows the system to open google in google chrome (if it's installed). <br/>
- "***open youtube***" command allows the system to open youtube in google chrome (if it's installed). <br/>
- "***open Project***" command allows the system to open github in google chrome (if it's installed). <br/>
- "***open trello***" command allows the system to open trello in google chrome (if it's installed). <br/>
- "***buy***" command allows the system to open daraz.com in google chrome (if it's installed) so you can buy stuff in online shop. Ex: "***buy*** headphone" <br/>








