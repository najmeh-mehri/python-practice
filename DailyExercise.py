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
            
Text = input("Please Enter your text:")
counts = {}

for ch in Text:
    if ch != ',':
        counts[ch] = counts.get(ch, 0) + 1

# پیدا کردن بیشترین تکرار
max_count = max(counts.values())

# پیدا کردن همه کاراکترهایی که بیشترین تکرار را دارند
most_frequent = [ch for ch, count in counts.items() if count == max_count]

print(f"Most frequent character(s): {most_frequent}")
print(f"Count: {max_count}")

NameList =["Nazanin","Nivan","Nicholas","Iran"]
ScoreList = [18,20,17,20]
StDict = dict(zip(NameList, ScoreList))
print(StDict)




def SumAll(*arg):
    sum = 0
    for item in arg:
        sum = sum + int(item)
    return sum
print(SumAll(2,5,6,7,4))
