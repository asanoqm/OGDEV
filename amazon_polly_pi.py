from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import pygame.mixer

session = Session("default")
polly = session.client("polly")
try:
    response = polly.synthesize_speech(Text="ひとっ走り付き合えよ", OutputFormat="mp3", VoiceId="Mizuki")
except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)
if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = "speech.mp3"
        try:
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            print(error)
            sys.exit(-1)
        print("synthesize_speech OK ->>" + output)
else:
    print("Could not stream audio")
    sys.exit(-1)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("speech.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
