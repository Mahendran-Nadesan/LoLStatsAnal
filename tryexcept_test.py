# Test script for try...except

##def main(name, mydict):
##    print "Checking if data exists..."
##    try:
##        is_data(name, mydict)
##    except:
##        print "Not found..."
##
##
##def is_data(name, mydict):
##    if name in mydict:
##        print "Name found!"
##    
##
##
##x = {}
##x['a'] = 3
##main('b', x)

##x = {}
##x['a'] = {}
##x['a']['1'] = 0
##x['a']['2'] = 0
##
##for i in x['a'].keys():
##    x['a'][i] = 1

a = 2
try:
    x = a
    b = c
except:
    print x, a
    print "no c"
