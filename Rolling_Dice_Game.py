
while quit != "q":

    import random
    print
    print "Rolling Dice Game"
    print
    print "Press Enter to roll"

    raw_input()
    number = random.randint(1,6)

    if number == 1:
        print " _________________ "
        print "|                 |"
        print "|        O        |"
        print "|                 |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
    if number == 2:
        print " _________________ "
        print "|                 |"
        print "|   O         O   |"
        print "|                 |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
    if number == 3:
        print " _________________ "
        print "|        O        |"
        print "|                 |"
        print "|  O           O  |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
    if number == 4:
        print " _________________"
        print "|  O            O |"
        print "|                 |"
        print "|  O            O |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
    if number == 5:
        print " _________________"
        print "| O             O |"
        print "|        O        |"
        print "| O             O |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
    if number == 6:
        print " _________________ "
        print "| O             O |"
        print "| O             O |"
        print "| O             O |"
        print "|_________________|"
        print
        print "Type 'q' to quit"
        quit = raw_input()
