import pyfiglet
import sys

def generate_art(text, font="standard"):
    return pyfiglet.figlet_format(text, font=font)

def main():
    # Take input from command line arguments
    if len(sys.argv) < 2:
        print("Usage: asciify <text>")
        return
    
    text = " ".join(sys.argv[1:])
    print(generate_art(text))