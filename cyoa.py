

def story():
    print "You are in a locked room."
    print ("> Look around")
    print ("> Wait")
    print ("> Cry")
    user_input = raw_input().lower()
    if user_input == "Look around".lower():
        print "You see a door."
    elif user_input == "Wait".lower():
        print "A hatch opens. A gun falls from the ceiling!! The hatch closes."
    elif user_input == "Cry".lower():
        print "It's gonna be ok :-)"
    else:
        print "You can't do that."
        story()

user_input = raw_input("What is your name?")
print "Hello, " + user_input
story()
