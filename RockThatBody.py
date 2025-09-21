# This program is just a program that I found on Instagram in which uses the rich and time libraries to print
# out lyrics from Black Eyed Peas song "Rock That Body"
import sys
from rich import print
from time import sleep
import time

def printLyrics():

    lines = [
        "I wanna da-",
        "I wanna dance in the lights",
        "I wanna ro-",
        "I wanna rock your body",
        "I wanna go",
        "I wanna go for a ride",
        "Hop in the music and",
        "Rock your body",
        "Rock that body",
        "Come on, come on",
        "Rock that body",
        "Rock your body",
        "Rock that body",
        "Come on, come on",
        "Rock that body",
    ]

    target_line_duration = 1.5

    delays_after_line = 0.5
    
    for line in lines:
        # Auto calculating per-character delay
        char_delay = target_line_duration / len(line)

        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)

        print()
        time.sleep(delays_after_line)

if __name__=="__main__":
        printLyrics()  