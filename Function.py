def pig_latin (word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return word+'ay'
    else:
        return word[1:]+first_letter+'ay'
def Sumnumbers (*args):
    return sum(args) * 0.05

def Vegtiable(**kwargs):
    if 'fruit' in kwargs:
        print('My fruite choice is {}'.format(kwargs['fruit']))
    else:
        print('i didnt find any fruit')

def lesser_of_two_evens (a,b):
    if a%2 == 0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    else:
        if a>b:
            return a
        else:
            return b

def animal_crackers(str):
    strlist = str.split()
    return strlist[0][0] == strlist[1][0]

def returntwenty(a,b):
    return a==20 or b==20 or a+b==20

def old_macdonald(str):
    str[0].upper()+str[1:3]+str[4].upper()+str[4:]

def reverse(str):
    #I am Home
    strlist = str.split()
    return " ".join(strlist[::-1])

def Almostthere(n):
    return (abs(200-n) <= 10) or (abs(100-n) <=10)

def has_33 (nums):
    for i in range(0,len(nums)):
        if (nums[i] == 3) and (nums[i] == nums[i+1]):
            return True
    return False

def paper_doll (text):
    str = ''
    for i in range(0,len(text)):
        str = str+text[i]*3

    return str

def blackjack(a,b,c):
    sum = a+b+c
    if sum <= 21:
        return sum
    elif (sum >21) and (a==11 or b==11 or c==11):
        return sum-10
    elif sum>21:
        return 'Bust'

def SummerOf69(arr):
    sum = 0
     for i in range(0,len(arr)):
         sum = sum+arr[i]
    print(sum)

if __name__ == '__main__':
    answer = pig_latin("Omar")
    print(answer)
    print(Sumnumbers(40,40,50,60,80))
    print(Vegtiable(fruit='apple',veggie='lettuce'))
    print(lesser_of_two_evens(2,5))
    print(animal_crackers("Levelheaded blama"))
    print(returntwenty(5,10))
    old_macdonald("omarr")
    print(reverse("I am Home"))
    print(Almostthere(190))
    print(has_33 ([1,1,3,3,1]))
    print(paper_doll ('Hello'))
    print(blackjack(9,9,9))
    SummerOf69([1,2,3,6,8,8,9])
