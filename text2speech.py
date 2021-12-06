from gtts import gTTS

mytext = "  Zero   Zero    Zero    Zero"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("ZERO.mp3")
