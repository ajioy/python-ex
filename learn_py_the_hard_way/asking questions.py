#ex 11
print "How old are you?" #no comma will end a line with a newline,input something.
age = raw_input()
print "How tall are you?", #doesn't matter,ignore comma
height = raw_input()
print "How much do you weigh?",
weigh = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age,height,weigh)