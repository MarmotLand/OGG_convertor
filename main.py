# Manuální převádění formátu MP3 na formát OGG:
# ffmpeg.exe -i MP3/"vstup.mp3" OGG/výstup.ogg

import os

volba = input("[1] = Obyčejné používání\n[2] = My Summer Car\n\n")

# Vrátí list všech souborů v složce programu 
vsechny_soubory = os.listdir("./MP3")
# vsechny_soubory = ['ffmpeg.exe', 'main.py', 'MP3', 'OGG', 'hudba.mp3']

# Vyfiltrování všech souborů s koncovkou .mp3
mp3 = []
for item in vsechny_soubory:
     if ".mp3" in item:
        mp3.append(item.replace(".mp3", "")) # ['hudba']

# Když nenajde zádné soubory s koncovkou .mp3 vypíše
if mp3 == []:
    print("Nenalezeny žádné MP3 soubory!") 

# Spústí program ffmpeg.exe a přeconvertuje soubory mp3 na soubory ogg
if volba == "1":
    for zvukovy_soubor in mp3:
        os.system(f"ffmpeg.exe -i MP3/\"{zvukovy_soubor}.mp3\" OGG/\"{zvukovy_soubor}.ogg\"")


elif volba == "2":
    navysovani = 1
    for zvukovy_soubor in mp3:
        os.system(f"ffmpeg.exe -i MP3/\"{zvukovy_soubor}.mp3\" OGG/\"track{str(navysovani)}.ogg\"")
        navysovani = navysovani + 1
else:
    print("Neplatný výběr!")

input("\n\nZmáčkni ENTER pro ukončení")
