
while quit != "q":

    import random
    print
    print "Rolling Dice Game"
    print
    print "Press Enter to roll"

    raw_input()
    number = random.randint(1,6)

    if number == 1:
        print "[-----------------]"
        print "[                 ]"
        print "[        O        ]"
        print "[                 ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()

    if number == 2:
        print "[-----------------]"
        print "[                 ]"
        print "[   O         O   ]"
        print "[                 ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()

    if number == 3:
        print "[-----------------]"
        print "[        O        ]"
        print "[                 ]"
        print "[  O           O  ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()

    if number == 4:
        print "[-----------------]"
        print "[  O            O ]"
        print "[                 ]"
        print "[  O            O ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()

    if number == 5:
        print "[-----------------]"
        print "[ O             O ]"
        print "[        O        ]"
        print "[ O             O ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()

    if number == 6:
        print "[-----------------]"
        print "[ O             O ]"
        print "[ O             O ]"
        print "[ O             O ]"
        print "[-----------------]"
        print "Type 'q' to quit"
        quit = raw_input()
