#ex 8
formatter = "%r %r %r %r" # replace r -> s ,see what happen

print formatter % (1,2,3,4)
print formatter % ("one", 11.212,'three',True,) #all parameters are ok.
print formatter % (True,False,False,True)
print formatter % (formatter, formatter, formatter, formatter) #'%r ...'
print formatter % (
	"i had this thing.",
	"that you could type up right.", #show single quotes
	"but it did't sing.", #show double quotes.why?
	'so i said goodnight.'
	)