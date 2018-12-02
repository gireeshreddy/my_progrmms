str1 = "this a mad race"
#vowel = ['a','e','i','o','u']
vowels = 'aeiou'
for idx in vowels:
    if idx in str1:
        str1=str1.replace(idx,'')
print(str1)
#print(str1.count(vowel[0]))
#str2=str1.count(vowel[0])
#str2=str1.count(vowel[1])
#str2=str1.count(vowel[2])
#str2=str1.count(vowel[3])
#str2=str1.count(vowel[4])
