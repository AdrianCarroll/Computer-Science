"""print ('''
1
2
3
''')

text= "Test. \nNext line"
print(text)

print ('One', 'Two' * 2)
print ('One' + 'Two' * 2)
print (len('0123456789'))

s = '0123456789'
print (s[3], ", ", s[0:3], "-", s[2:5])
print (s[:3], ", ", s[3:], ", ", s[3:100])
print (s[20:], s[2:1], s[1:1])

s = '987654321'
print (s[-1], s[-3])
print (s[-3], s[-3])
print (s[-100:-3], s[-100:3])

x= "hello" * 3
y= str(123)
print (x, y)
x= "Hello" + "World"
y= len(x)
print (y, x)

x= "hello" + \
   "to Python" + \
   "world"
for char in x:
    y = char
    print (y, ':', end=' ')

x='hello world'
print (x[:2], x[:-2], x[-2:])
print (x[6:], x[2:4])
print (x[2:-3], x[-4:-2])

theStr = 'This is a test'
inputStr = input("Enter integer: ")
inputInt = int(inputStr)
testStr = theStr
while inputInt >= 0:
    testStr = testStr[1:-1]
    inputInt=inputInt-1
testBool= 't' in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)

testStr = 'abcdefghi'
inputStr = input("Enter integer: ")
inputInt = int(inputStr)
count=2
newStr=' '
while count <= inputInt:
    newStr=newStr+testStr[0:count]
    testStr=testStr[2:]
    count = count + 1
print(newStr)
print(testStr)
print(count)
print(inputInt)"""

app=input("Give me a string: ")
big=0
lil=0
other=0
for ele in app:
    if ele >= "a" and ele < "m":
        lil=lil+1
    elif ele > 'm' and ele <= 'z':
        big=big+1
    else:
        other=other+1
print(big)
print(lil)
print(other)
print(app.isdigit())