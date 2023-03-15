

dict = {}

a = "acb"
b = "ahbgdc"

def test(s, t):
    temp = t
    for char in s:
        if char not in temp:
            return False
        temp = temp[temp.find(char)+1:len(temp)]
    return True



print(test(a,b))