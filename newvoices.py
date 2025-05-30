import os
import pygame

def speak(text):
#        in cmd type: python -m edge_tts --list-voices
        voice = 'en-US-AriaNeural'
#        en-US-AnaNeural
#        en-US-AndrewMultilingualNeural
#        en-US-AndrewNeural
#        en-US-AriaNeural
#        en-US-AvaMultilingualNeural
#        en-US-AvaNeural
#        en-US-BrianMultilingualNeural
#        en-US-BrianNeural
#        en-US-ChristopherNeural
#        en-US-EmmaMultilingualNeural
#        en-US-EmmaNeural
#        en-US-EricNeural
#        en-US-GuyNeural
#        en-US-JennyNeural
#        en-US-MichelleNeural
#        en-US-RogerNeural
#        en-US-SteffanNeural
        data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
        os.system(data)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)

        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            
