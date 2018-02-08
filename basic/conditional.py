import unicodedata

test = None
mystring ="Hello"
myfloat = 10.0
myint = 1

if mystring.lower() == "hello".lower():
    print("Your message: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Yes, this is float and is %f" % myfloat)
if isinstance(myint, int) and myint == 1:
    print("Integer %d" % myint)