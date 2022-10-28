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


# Spustí program ffmpeg.exe a přeconvertuje soubory mp3 na soubory ogg

itemu_celkem = str(len(mp3))  # počet mp3 souborů v listu (vypisování postupu)
navysovani = 1

print("\nCTRL+C pro ukončení\n\nPostup:")
if volba == "1":
    for zvukovy_soubor in mp3:
        os.system(f"ffmpeg.exe -y -hide_banner -loglevel error -i ./MP3/\"{zvukovy_soubor}.mp3\" ./OGG/\"{zvukovy_soubor}.ogg\"")  # přepínač -y je pro overwrite
        
        print(f"Hotovo {navysovani}/{itemu_celkem}")
        navysovani = navysovani + 1

elif volba == "2":
    for zvukovy_soubor in mp3:
        os.system(f"ffmpeg.exe -y -hide_banner -loglevel error -i ./MP3/\"{zvukovy_soubor}.mp3\" ./OGG/\"track{str(navysovani)}.ogg\"")
        
        print(f"Hotovo {navysovani}/{itemu_celkem}")
        navysovani = navysovani + 1
else:
    print("Neplatný výběr!")

input("\n\nZmáčkni ENTER pro ukončení...")
