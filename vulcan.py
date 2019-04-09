# this is a vulcan.py file
# the feature is ..errr.. is sth...

try:
    a=int(input("please input a int:"))
    print("what you input is:",a)
except IOError:
    print("Error:IOError...")
else:
    print("else except...")
finally:
    print("End...")

