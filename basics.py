'''
Python basics
Introduces basics
'''
print("Hello")
# prints hello
str1="Keith Wright" # my name
str2="""401 Mile of Cars Way
Suite 100
National City, CA 91950"""

print(str1 + ' ' + str2)
print(str1 + str2)
print("Name:", str1, str2)

print(dir(str1))
help(str2.upper)

print(str2.upper())
print(str2.isupper())
print(str2)

data="This is a good day to learn Python"
print("data[0:4] ->", data[0:4])
print("data[:4] ->", data[:4]) # From beginning to fifth character
print("data[-6:] ->", data[-6:]) # From six characters before the end to the end

colors=['red', 'blue', 'green', 'yellow']
print ("Original order:", colors)
colors.sort()
print ("Sorted order:", colors)
print ("colors[0:3] ->", colors[0:3])

print("type(colors) ->", type(colors))
print("dir(colors) ->", dir(colors))

hue=('red', 'green', 'red', 'yellow')
print("type(hue) ->", type(hue))
print("dir(hue) ->", dir(hue))

info={"name": "Bob Smith", "age": 25, "title": "manager"}
print ('info["name"] ->', info["name"])
print ('info["age"] ->', info["age"])
print("dir(info) ->", dir(info))
print("info.keys() ->", info.keys())
print("info.values() ->", info.values())
info.clear()
print("len(info) ->", len(info))
print("info.keys() ->", info.keys())