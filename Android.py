import webbrowser
#import pyttsx3
import datetime
import time
import wolframalpha
import requests
import pyautogui
import wikipedia
import clipboard
import os
import pygame
import pyjokes
from translate import Translator
def mohsen():

    
    def load():
        print("Loading your AI personal assistant G-One")
        time.sleep(5)
    
    def wishMe():
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            print("Hello,Good Morning")
        elif hour>=12 and hour<18:
            print("Hello,Good Afternoon")
        else:
            print("Hello,Good Evening")
#    def wish():
#    	hour=datetime.datetime.now().hour
#    	if hour==19:
#    		print('وقت اذان مغرب است . به مسجد بروید.')
#    	if hour==11:
#    		print('وقت اذان ظهر است، به مسجد بروید.')
    def new():
        print("Tell me how can I help you now?")
    def opencv():
        import imgn.py
    def text2speech():
        text = clipboard.paste()
        print(text)
        #speak(text)

    def screenshot():
        name_img = (datetime.datetime.now())
        name_img = 'ss.png'
        img = pyautogui.screenshot(name_img)
        img.show()
    def date():
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        print("the current date is:")
        print(date)
        print(month)
        print(year)
    def welcome():
        #speak('welcome back msn')
        print('welcome back msn')
    #a = int(input("Enter ID:"))
    #getvoices(a)
    def AI():
        welcome()
        load()
        wishMe()
        #date()
        #wish()
        new()
    AI()
    def takeCommand():
        try:
            command = input('Enter:')
            print(f"user said:{command}\n")
        except Exception as e:
            print("Pardon me, please say that again")
            return "None"
        return command
    #############################################
    translateCommand = ['translate','ترجمه','ترجمه کن']
    translateEn = ['english', 'en','انگلیسی']
    translateFa = ['persian', 'fa','فارسی']
#############################################
    goodBye = ['good bye','خداحافظ','خدانگهدار']
#############################################
    opening = ['opening', 'open','باز کن','باز']
    openDigikala = ['digikala','دیجیکالا']
    openGoogle = ['google','گوگل','موتور جستجو']
    openYoutube = ['youtube','یوتیوب']
    openGmail = ['gmail', 'email','ایمیل','جیمیل']
    openStar_clicks = ['star-clicks']
    open_site = ['site','سایت', 'home', 'Home']
#############################################
    clock = ['time', 'clock','تایم','زمان','ساعت']
#############################################
    Question = ['Question','سوال','سوال دارم']
#############################################
    weather = ['weather','آب و هوا']
#############################################
    whoareyou = ['who are you','تو که هستی','تو چه کسی هستی']
#############################################
    ask = ['ask','محاسبه','محاسبه کن', 'Calculator', 'calculator']
#############################################
    search = ['search','سرچ','سرچ کن']
#############################################
    camera = ['camera']
#############################################
    whomadeyou = ['who made you','چه کسی تو را ساخته است']
#############################################
    upsounds = ['up', 'بالا']
    sounddown = ['down', 'پایین']
    soundmute = ['mute','قطع']
    prevtrack = ['prev']
    nexttrack = ['next']
    play = ['play']
    stop = ['stop']
    sound_command = ['sound', 'صدا', 'صوت']
#############################################
    brightcommand = ['bright']
    upbright = ['up']
    dnbright = ['down']
#############################################
    wakeUpCall = ['G-one','جی وان', 'جيوان', 'matilda', 'microsoft', 'Microsoft', 'mossi', 'Mossi', 'MOSSI', 'no limits']
#############################################
    cv2 = ['opencv']
    clipboard = ['بخوان', 'بخون', 'read', 'reading', 'book', 'clipboard']
    Scratch = ['Scratch', 'scratch']
    dnplayer = ['android', 'Android']
    Photoshop = ['photoshop', 'Photoshop']
    Flight = ['Flight', 'flight']
    filex = ['explorer', 'file explorer', 'file']
    code = ['vs code', 'code']
    joke = ['joke']
    screenshot = ['screenshot', 'shot', 'screen']
    date = ['تاریخ', 'date']
    music_command = ['music']
    quran = ['quran']
    Tohmat = ['tohmat']
    trackone = ['track one']
#############################################
    
    if __name__=='__main__':
        
        while True:
            command = takeCommand()
            if any(item in command for item in wakeUpCall):
                if any(item in command for item in clock):
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"the time is {strTime}")
                elif any(item in command for item in goodBye):
                    #speak('your personal assistant G-one is shutting down,Good bye')
                    print('your personal assistant G-one is shutting down,Good bye')
                    break
                elif any(item in command for item in music_command):
                    if any(item in command for item in Tohmat):
                        print('ok is playing music')
                        time.sleep(3)
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("musics\\Tohmat.mp3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif any(item in command for item in trackone):
                        print('ok is playing music')
                        time.sleep(3)
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("musics\\1.mp3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    else:
                        print('Pardon me please say again')
                elif any(item in command for item in quran):
                    print('ok is playing quran')
                    time.sleep(3)
                    if 'sore 1--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\001.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 2--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\002.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 3--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\003.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 4--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\004.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 5--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\005.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 6--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\006.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 7--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\007.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 8--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\008.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 9--' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\009.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 10-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\010.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 11-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\011.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 12-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\012.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 13-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\013.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 14-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\014.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 15-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\015.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 16-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\016.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 17-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\017.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 18-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\018.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 19-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\019.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 20-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\020.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 21-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\021.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 22-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\022.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 23-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\023.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 24-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\024.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()

                    elif 'sore 25-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\025.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 26-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\026.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 27-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\027.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 28-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\028.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 29-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\029.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 30-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\030.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 31-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\031.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 32-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\032.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 33-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\033.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 34-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\034.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 35-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\035.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 36-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\036.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 37-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\037.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 38-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\038.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 39-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\039.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 40-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\040.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 41-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\041.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 42-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\042.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 43-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\043.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 44-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\044.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 45-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\045.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 46-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\046.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 47-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\047.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 48-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\048.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 49-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\049.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 50-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\050.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()

                    elif 'sore 51-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\051.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 52-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\052.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 53-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\053.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 54-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\054.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 55-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\055.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 56-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\056.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 57-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\057.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 58-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\058.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 59-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\059.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 60-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\060.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 61-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\061.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 62-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\062.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 63-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\063.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 64-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\064.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 65-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\065.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 66-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\066.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 67-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\067.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 68-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\068.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 69-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\069.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 70' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\070.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 71-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\071.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 72-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\072.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 73-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\073.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 74-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\074.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 75-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\075.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 76-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\076.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()

                    elif 'sore 77-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\077.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 78-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\078.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 79-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\079.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 80-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\080.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 81-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\081.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 82-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\082.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 83-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\083.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 84-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\084.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 85-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\085.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 86-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\086.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 87-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\087.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 88-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\088.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 89-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\089.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 90-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\090.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 91-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\091.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 92-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\092.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 93-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\093.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 94-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\094.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 95-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\095.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 96-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\096.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 97-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\097.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 98-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\098.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 99-' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\099.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 100' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\100.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 101' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\101.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 102' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\102.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()

                    elif 'sore 103' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\103.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 104' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\104.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 105' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\105.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 106' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\106.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 107' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\107.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 108' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\108.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 109' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\109.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 110' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\110.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 111' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\111.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 112' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\112.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 113' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\113.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    elif 'sore 114' in command:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("quran\\114.MP3")

                        try:
                            pygame.mixer.music.play()

                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)

                        except Exception as e:
                            print(e)

                        finally:
                            pygame.mixer.music.stop()
                            pygame.mixer.quit()
                    else:
                        print('Pardon me please say again')
                        #speak('Pardon me please say again')
                elif any(item in command for item in date):
                    date()
                elif any(item in command for item in screenshot):
                    screenshot()
                elif any(item in command for item in joke):
                    #speak(pyjokes.get_joke())
                    print(pyjokes.get_joke())
                elif any(item in command for item in cv2):
                    opencv()
                elif any(item in command for item in brightcommand):
                    if any(item in command for item in dnbright):
                        sbc.set_brightness(50)
                        print('ok')
                    if any(item in command for item in upbright):
                        sbc.set_brightness(100)
                        print('ok')
                elif any(item in command for item in translateCommand):
                    if any(item in command for item in translateEn):
                        user = input('Enter Word:')
                        option = Translator(from_lang="en" , to_lang="persian")
                        print(option.translate(user))
                    elif any(item in command for item in translateFa):
                        user = input('Enter Word:')
                        option = Translator(from_lang="persian" , to_lang="en")
                        print(option.translate(user))
                        #speak(option.translate(user))
                    else:
                        print('pardon me please say thet again')
                        #speak('pardon me please say that again')
                elif any(item in command for item in opening):
                    if any(item in command for item in openDigikala):
                        webbrowser.open_new_tab("https://www.digikala.com")
                        print('opening digikala')
                        #speak('opening digikala')
                    elif any(item in command for item in openGoogle):
                        webbrowser.open_new_tab("https://www.google.com")
                        print('opening google')
                        #speak('opening google')
                    elif any(item in command for item in openYoutube):
                        webbrowser.open_new_tab("https://www.youtube.com")
                        print("youtube is open now")
                        time.sleep(5)
                    elif any(item in command for item in openGmail):
                        webbrowser.open_new_tab("gmail.com")
                        print("Google Mail open now")
                        time.sleep(5)
                    elif any(item in command for item in openStar_clicks):
                        webbrowser.open_new_tab("star-clicks.com")
                        print("star-clicks open now")
                        time.sleep(5)
                    elif any(item in command for item in open_site):
                        site = input('Enter location:')
                        webbrowser.open_new_tab(site)
                        print(site)
                        time.sleep(5)
                    elif any(item in command for item in filex):
                        os.system('explorer C://{}'.format(command.replace('Open', '')))
                        print('file explorer is open now.')
                    elif any(item in command for item in Scratch):
                        codepath = 'C:\\Program Files (x86)\\Scratch 3\\Scratch 3.exe'
                        os.startfile(codepath)
                        print('scratch is open now.')
                    elif any(item in command for item in dnplayer):
                        codepath = 'E:\\LDPlayer\\LDPlayer9\\dnplayer.exe'
                        os.startfile(codepath)
                        print('ld player is open now.')
                    elif any(item in command for item in Photoshop):
                        codepath = 'C:\\Program Files\\Adobe\\Adobe Photoshop 2024\\Photoshop.exe'
                        os.startfile(codepath)
                        print('photoshop 2024 is open now.')
                    elif any(item in command for item in Flight):
                        codepath = 'C:\\Program Files (x86)\\Microsoft Flight Simulator X\\fsx.exe'
                        os.startfile(codepath)
                        print('microsoft flight simulator is open now.')
                    elif any(item in command for item in code):
                        codepath = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
                        os.startfile(codepath)
                        print('vs code is open now.')
                    else:
                        print('pardon me please say that again')
                        #speak('pardon me please say that again')
                elif any(item in command for item in Question):
                    text = input('Enter the word you want to search for:')
                    print(text)
                    time.sleep(3)
                    result = wikipedia.summary(text, sentences=6)
                    print(result)
                    #speak(result)
                    user = result
                    option = Translator(from_lang="en" , to_lang="persian")
                    print(option.translate(user))
                elif any(item in command for item in clipboard):
                    text2speech()
                elif any(item in command for item in weather):
                    api_key="8ef61edcf1c576d65d836254e11ea420"
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    print("whats the city name")
                    #speak("whats the city name")
                    city_name=input('enter:')
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        print(" Temperature in kelvin unit is " +
                                str(current_temperature) +
                                "\n humidity in percentage is " +
                                str(current_humidiy) +
                                "\n description  " +
                                str(weather_description))
                        print(" Temperature in kelvin unit = " +
                                str(current_temperature) +
                                "\n humidity (in percentage) = " +
                                str(current_humidiy) +
                                "\n description = " +
                                str(weather_description))
                    else:
                        print(" City Not Found ")
                    user = weather_description
                    option = Translator(from_lang="en" , to_lang="persian")
                    print(option.translate(user))
                elif any(item in command for item in whoareyou):
                    print('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                            'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                            'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
                elif any(item in command for item in ask):
                    print('I can answer to computational and geographical questions and what question do you want to ask now')
                    #speak('I can answer to computational and geographical questions and what question do you want to ask now')
                    question=input('Enter ask:')
                    app_id="R2K75H-7ELALHR35X"
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(question)
                    answer = next(res.results).text
                    print(answer)
                    #speak(answer)
                elif any(item in command for item in search):
                    command = input('Enter Question:')
                    print(command)
                    time.sleep(3)
                    webbrowser.open_new_tab(command)
                    time.sleep(5)
                elif any(item in command for item in camera):
                    ec.capture(0,"robo camera","img.jpg")
                elif any(item in command for item in whomadeyou):
                    #speak("I was built by mohsen")
                    print("I was built by mohsen")
                elif any(item in command for item in play):
                    pyautogui.press('playpause')
                    print('ok')
                elif any(item in command for item in stop):
                    pyautogui.press('playpause')
                    print('ok')
                elif any(item in command for item in sound_command):
                    if any(item in command for item  in upsounds):
                        print("ok, sound uped")
                        pyautogui.press('volumeup')
                    elif any(item in command for item in sounddown):
                        print('sound downed')
                        pyautogui.press('volumedown')
                    elif any(item in command for item in soundmute):
                        print("sound muted")
                        pyautogui.press('volumemute')
                    else:
                        print('pardon me please say that again')
                        #speak('pardon me please say that again')
                elif any(item in command for item in nexttrack):
                    print('ok')
                    pyautogui.press('nexttrack')
                elif any(item in command for item in prevtrack):
                    print('ok')
                    pyautogui.press('prevtrack')
                else:
                    command = input('جوابی برای این سوال پیدا نکردم آیا می خواهید برایتان سرچ کنم؟')
                    areh = ['yes']
                    na = ['no']
                    def yes():
                        com = input(':بفرمایید چه می خواهید')
                        webbrowser.open_new_tab(com)
                    def no():
                        print('خیلی خوب دیگه چه کمکی می تونم بکنم؟')
                    
                    if any(item in command for item in areh):
                        yes()
                    if any(item in command for item in na):
                        no()

for i in range(3):
	name = input('enter name:')
	password = input('enter password:')
	command = input('Enter:')
	if "Mohsen_maleki1389" in name and "msn422777" in password and "hello" in command:
		print('welcome') 
		mohsen()
	else:
		print('not')
