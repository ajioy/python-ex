#exercise 6
x = "there are %d types of people," % 10
binary = "binary"
do_not  = "don't"
y = "those who know %s and those who %s" % (binary,do_not)

print x
print y

print "i said: %r." % x # keep up single quotes
print "i said: %s." % x # no single quotes

print "i also said: '%s'." % y

hilarious = False 
joke_evalutation = "isn't that joke so funny? %r"

print joke_evalutation % hilarious 
w = "this is the left side of ..." 
e = "a string with a right side."
print w + e