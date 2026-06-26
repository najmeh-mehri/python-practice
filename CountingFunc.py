"""
String and Number Counting Functions

1. count(num, number) - Count how many times a digit appears in a number
2. count(text) - Count vowels using count() method
3. count(text) - Count vowels using a loop
4.Count character frequencies in a string.

"""
def CountDigit(num, number):
    num = str(num)
    number = str(number)
    return(number.count(num))


def CountVowls(Text):
    a=Text.count('a') 
    i=Text.count('i')
    u=Text.count('u')
    o=Text.count('o')
    e=Text.count('e')
    Text=a+i+u+o+e
    return Text

def CountVowls_2(Text):
    NumeberOfVowl = 0
    for i in Text:
        if i == 'a' or i == 'o' or i == 'e' or i == 'i' or i == 'u':
            NumeberOfVowl += 1
    return NumeberOfVowl


def CountChar(Text):
     counts = {}
     for ch in Text:
            if ch != ',':
                counts[ch] = counts.get(ch, 0) + 1

     for ch, count in counts.items():
            print(f"* {ch} : {count}")
#Exercise
Text = input("Please Enter your text:")
Uper = 0
Lower =0
for i in Text:
    if i.isupper():
       Uper +=1
    elif i.islower():
        Lower+=1
        
print(f"Upper: {Uper} - Lower: {Lower}")

Text = input("Please Enter your text:")
print(Text[::-1])

def is_palindrome(Txt):
    return Txt == Txt[::-1]
print(is_palindrome(Text))

Text = input("Please Enter your text:")

# پاک‌سازی رشته
cleaned_text = Text.strip().lower()

# حذف فاصله‌ها
no_spaces = cleaned_text.replace(" ", "")

print(f"Original: {Text}")
print(f"Cleaned: {no_spaces}")

Text = input("Please Enter your text:")
counts = {}
for ch in Text:
       if ch != ',':
              counts[ch] = counts.get(ch, 0) + 1

for ch, count in counts.items():
       print(f"* {ch} : {count}")
            
NameList =["Nazanin","Nivan","Nicholas","Iran"]
ScoreList = [18,20,17,20]
StDict = dict(zip(NameList, ScoreList))
print(StDict)

if __name__ == "__main__":
    
    print("Testing CountDigit:")
    print(f"CountDigit(4, 4143131) = {CountDigit(4, 4143131)}")  # 2
    print(f"CountDigit(1, 1234561) = {CountDigit(1, 1234561)}")  # 2
    
    print("\n" + "=" * 30)
    print("Testing CountVowls:")
    print(f"CountVowls('hello world') = {CountVowls('hello world')}")  # 3
    print(f"CountVowls('aeiou') = {CountVowls('aeiou')}")  # 5
    
    print("\n" + "=" * 30)
    print("Testing CountVowls_2:")
    print(f"CountVowls_2('hello world') = {CountVowls_2('hello world')}")  # 3
    print(f"CountVowls_2('python') = {CountVowls_2('python')}")  # 1 (o)
    
    print("\n" + "=" * 30)
    print("Testing CountChar:")
    print("Input: 'aabc'")
    CountChar('aabc')
    print("\nInput: 'hello, world'")
    CountChar('hello, world')
