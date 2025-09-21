# This program is just a program that I found on Instagram in which uses the rich and time libraries to print
# out lyrics from Black Eyed Peas song "Rock That Body"
import sys
from rich import print
from time import sleep
import time

 # Now implement a code that takes any text file and is able to parse it w/out brute forcing the words

def printLyrics(filename):
    # Read all lines from the file, stripping newline characters
    with open(filename, "r", encoding="utf-8") as f:
         lines = [line.strip() for line in f if line.strip()] # ignoring the empty lines

    target_line_duration = 1.5          # how long each line should take
    delays_after_line = 0.5             # pause between lines
    
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
        printLyrics("Discord Shawty.txt")  # just point to your text file