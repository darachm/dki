#!/usr/bin/env python3

import ruamel.yaml, random, json

with open("gnostic.yaml","r") as f:
    hexes = ruamel.yaml.safe_load(f)
with open("hexagrams.json","r") as f:
    ablwr_hexes = ruamel.yaml.safe_load(f)

def yarrow():
    return(random.choice([6,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9]))

this_hex = [ yarrow() for i in range(6) ]
this_hex_yang_yin = [ str(i % 2) for i in this_hex ]
changing_lines = [ int(i is 6 or i is 9) for i in this_hex ]
changed_hex = [ str( (int(i[0])+int(i[1])) % 2 ) for i in zip(this_hex_yang_yin,changing_lines) ]

this_hex_number = ablwr_hexes["".join(this_hex_yang_yin)]['number']
this_hex_hexagram = ablwr_hexes["".join(this_hex_yang_yin)]['hexagram']
changed_hex_number = ablwr_hexes["".join(changed_hex)]['number']
changed_hex_hexagram = ablwr_hexes["".join(changed_hex)]['hexagram']

print("<html><body>")
print("Generated: "+str(this_hex))
print("<hr/>")
print("<h1 class=\"hexagram\">"+this_hex_number+" "+this_hex_hexagram+"</h1>")
print(hexes["hex"+this_hex_number]["notes"])
for i in range(6):
    if changing_lines[i] == 1:
        print("<hr/><h2>Changing line "+str(i)+"</h2>")
        print(hexes["hex"+this_hex_number]["lines"][i])
if this_hex_number is not changed_hex_number:
    print("<hr>")
    print("<h1 class=\"hexagram\">"+changed_hex_number+" "+changed_hex_hexagram+"</h1>")
    print(hexes["hex"+changed_hex_number]["notes"])


print("</body></html>")

