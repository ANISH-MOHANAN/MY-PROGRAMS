#converting file data to audio
from gtts import gTTS
import os
text=open('demo1.txt','r',encoding='utf-8').read()
output=gTTS(text=text,lang='en',slow=False)
output.save('myfile.mp3')
os.system('start myfile.mp3')
