''' flow_while.py '''

invalid = True

while invalid:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)
        if age > 0 and age < 150: # 0 < age < 150:
            invalid = False
            print("Your age in days is about", int(age * 365.25))
    else:
        print("You must input a valid integer age!")

count = 0
while True:
    print('hello')
    count = count + 1
    if count > 10:
        break