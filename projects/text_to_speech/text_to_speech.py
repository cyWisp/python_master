from gtts import gTTS

FILE = 'hi_there.mp3'
LANG = 'en'

if __name__ == '__main__':
    text = "I am having too much fun with this."
    speech = gTTS(
        text=text,
        lang=LANG,
        tld='co.uk',
        slow=False
    )

    speech.save(FILE)
