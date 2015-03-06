def formulario(user):
    print ("hello", user, "the next questions are only with the purpouse to
            know more about you")
    print "qution 1: HOw OLd Are YOU?"
    age = raw_input()
    if age <= 15:
        print "ohh I can see that you are very youngh.."
    elif age > 15 and age <28:
        print "ohh come on lets go for some beers"
    else:
        print "well, I imagine that you are married, arent you?"
        usr = raw_input("y/n")
