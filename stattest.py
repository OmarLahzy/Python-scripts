#use For , Split , if to get strings start with S
st = "Ptint only the words that start with s in this sentence"
st_list  = st.split()
for word in st_list:
    if word[0] == 's':
        print(word)

#print Even number
for i in range(0,11):
    if i%2 == 0:
        print(i)
#List Comprehinesion For number divisable by 3
mylist = [x for x in range(1,51) if x%3 == 0 ]
print(mylist)

#if length of word is even print Even
st = "Print every word in this sentence that has an even number of letters"
for word in st.split():
    if len(word)%2 == 0:
        print("Even")
    else:
        print(word)
#print form 1-100 remove multi 3 with 'Fizz' and multi 5 'Buzz' multi 5and3 'FizzBuzz'
for num in range(1,100):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)
#use list Comprehinesion to crate a list of first letter in string
st = "Create a list of the first letter of every word in this string"
mylist = [word[0] for word in st.split()]
print(mylist)
