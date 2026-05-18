"""
#Cleaning a user input 
name = input("Whats your name? ").strip()
print(f"hello, {name}")

#if have a character special like ','

name = input("Whats your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello ", {name})    


import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#extract a input from the user like a url

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

#5
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
"""
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))    