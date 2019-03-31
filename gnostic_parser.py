#!/usr/bin/env python3

import re, ruamel.yaml, bs4, os

hexes = dict()

def parseOutNotes( list_of_ps ):
    return_string = ""
    # scan for it
    while list_of_ps:
        i = list_of_ps.pop(0)
        if re.search("NOTES AND PARAPHRASES",str(i)):
            break
    # record it
    while list_of_ps:
        i = list_of_ps.pop(0)
        if re.search("Line-[0-9]",str(i)): 
            list_of_ps.insert(0,i)
            break
        return_string += str(i)
    return( ( return_string, list_of_ps ) )

for each in os.scandir("dekorne_gnostic_pages"):
    if each.is_file():
        with open(each.path,"r") as infile:
            html = "".join(infile.readlines())
            soup = bs4.BeautifulSoup(html, 'html.parser')

            hex_number = soup.find(id=re.compile("hex"))['id']
            hexes[hex_number] = dict()
            hexes[hex_number]["notes"] = ""
            hexes[hex_number]["lines"] = dict()

            plist = soup.find(id=re.compile("hex")).find_all("p")

            ( hexes[hex_number]["notes"], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][0], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][1], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][2], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][3], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][4], plist ) = parseOutNotes(plist)
            ( hexes[hex_number]["lines"][5], plist ) = parseOutNotes(plist)

with open("gnostic.yaml","w") as f:
    ruamel.yaml.dump(hexes,f)
