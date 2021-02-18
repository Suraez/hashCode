s = input().strip('"')
mylist = []
for letter in s:
    if letter == '(' or letter == '{' or letter == '[' or len(mylist) == 0:
        mylist.append(letter)
    if len(mylist) != 0:
        if letter == ')':
            if mylist[len(mylist)-1] == '(':
                mylist.pop()
            else:
                mylist.append(letter)
        if letter == '}':
            if mylist[len(mylist)-1] == '{':
                mylist.pop()
            else:
                mylist.append(letter)
        if letter == ']':
            if mylist[len(mylist)-1] == '[':
                mylist.pop()
            else:
                mylist.append(letter)
    
if len(mylist) == 0:
    print(True)
else:
    print(False)