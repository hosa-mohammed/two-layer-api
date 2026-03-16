student = {
    
}
student["name"]=input("Enter your name ")
student['class']='last class'
student['grade']= input("Enter your grade ")
student['age']=input("Enter your age ")
print(f"Student : {student['name']}\nAge : {student['age']}\nGrade : {student['grade']}")
text = input("Enter a text : ")
words = text.split()
word_count ={}
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1 
for word, count in word_count.items():
    print(f"{word} : {count}")
totle_word = len(words)
print(totle_word)