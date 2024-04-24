# The Server Setup
import urllib.request    # For requests
import sys               # For closing the program
import os                # For clearing the screen, for getting the terminal size.
from pathlib import Path # For getting the last saved server
from datetime import date

today = date.today().strftime('%Y-%m-%d')

def dash():
    dashs = ""
    while not len(dashs) == os.get_terminal_size().columns:
        dashs = f"{dashs}-"
    return dashs

def request(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    contents = urllib.request.urlopen(req).read().decode('utf-8').strip()
    return contents

def newarticle():
    title=input("Name of article:\n> ")
    content=input("Content: (use backslash as newline)\n> ")
    with open(Path("./num.txt"), "r") as f:
        num=int(f.read().strip())
    with open(Path("./num.txt"), "w") as f:
        f.write(str(num+1))
    num=num+1
    os.mkdir(f"./news/{str(num)}")
    with open(Path(f"./news/{num}/metadata.txt"), "w") as f:
        f.write(f"{title}\\{today}\\")
    with open(Path(f"./news/{num}/content.txt"), "w") as f:
        f.write(content)
    print("Done!")
    

def firststart():
    print("Server not set up yet.")
    print(dash())
    title=input("Name: (ex. \"Example News\")\n> ")
    disc=input("Discription: (ex. \"The news filled with examples!\")\n(use backslashes as newlines)\n> ")
    with open(Path("./num.txt"), "w") as f:
       f.write("-1")
    with open(Path("./disc.txt"), "w") as f:
       f.write(disc)
    with open(Path("./title.txt"), "w") as f:
       f.write(title)
    os.mkdir("./news/")
    print("Creating new post...")
    newarticle()



def main():
    os.system("clear")
    print("Welcome to the setup script.")
    if Path("./num.txt").is_file():
        print("Detected server first-time setup has been done.")
        newarticle()
    else:
        firststart()

os.system("clear")
print(f"{dash()}\nINPORTANT\nIf there is an error above this text, this script will not work on your system.\nIf so, please set up the server manually.\n{dash()}\nNOTICE: This will setup in the directory that you are currently in.\n{dash()}")
if (input("Type \"y\" if there is no error message. ")=="y"):
   main()

