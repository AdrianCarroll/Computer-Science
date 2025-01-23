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
print(inputInt)

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

D1=input("Enter string of digits")
D2=input("Enter string of digits")
if len(D1)>len(D2):
    small=D2
    large=D1
else:
    small=D1
    large=D2
new=' '
for element in small:
    result=int(element)+int(large[0])
    new=new+str(result)
    large=large[1:]
print(len(new))
print(new)
print(large)
print(small)

S=input("Enter string: ")
RS= ' '
for ch in S:
    RS=ch+RS
print(S+RS)

S=input("Enter string: ")
RS= ' '
for ch in S:
    RS=ch+2+RS
print(RS+S)

s="PURA VIDA"
print(s[9] + s[9:15])

s="PURA VIDA"
s1=(s[:10] + s[10:])
s2=(s[10]+s[-10])

s="PURA VIDA"
s1=s*2
s2=s1[-19] - s1[-20]
s3= s1[-19:]

s="PURA VIDA"
s1=s[:5]
s2=s[5:]
s3=s1*s2
s4=s2+'3'
s5=s3+3

"whenever".find("never")
"whenever".find("what")"""