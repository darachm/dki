#!/usr/bin/env python3

import re, yaml, bs4, os

for each in os.scandir("dekorne_gnostic_pages"):
    if each.is_file():
        with open(each.path,"r") as infile:
            html = "".join(infile.readlines())
            soup = bs4.BeautifulSoup(html, 'html.parser')

            hex_number = soup.find(id=re.compile("hex"))['id']
            print(hex_number)

            plist = soup.find(id=re.compile("hex")).find_all("p")

            while plist:
                i = plist.pop(0)
                if re.search("NOTES AND PARAPHRASES",str(i)):
                    break

            while plist:
                i = plist.pop(0)
                if re.search("Line-1",str(i)):
                    break
                print(i)

            print()
            print()
            print()
            print()
