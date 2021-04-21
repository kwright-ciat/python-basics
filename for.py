''' flow_for.py
Show basic for loop
'''
colors=["red", "blue", "yellow", "green"]
for hue in colors:
    print (hue, "is my favorite color")

props = dir(colors)
print("Properties of the color list")
for prop in props:
    if not prop.startswith("__"):
        print(prop,end=' ')
else:
    print()