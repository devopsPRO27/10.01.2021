#define list from range
list1=list(range(1,19,4))
print(list1)

#do-while
while True : # DO WHILE
    x = int(input("input"))
    if x==1:
        continue
    print("hii")

    if x==4:
        break
print("out Of the loop")

#reversed range
for i in range(200,1,-1):
    print(i)

#how to create a list ?
lst=[]
for i in range(11):
    lst.append(i**2)
print(lst)
lst2=[float(i*3//5) for i in range(1,100) ]
lst3=list(range(7,100,7))
print(lst2)
print(lst3)

lst1=[1,4,6,8,2]
lst4=[]
print(lst1)
for x in lst1:
    lst4.append(x*3)
print(lst4)

lst5=[x for x in lst1]
print(lst5)

lst6=lst1.copy()
lst1[1]=55
print(lst1)
print(lst6)

#9
for i in range(100):
    if i %7 ==0:
        print(i)
print(list(range(7,100,7)))
print([i for i in range(7,100,7)])
x=7
while x<100 and x%7==0:
    print(x)
    x = x + 7

#10
sum=0
while True:
    x=int(input("please enter a number \n"))
    if x<0:
        break
    sum += x #sum =sum+x
print(sum)

makhpilah=1
for i in range (1,int(input("please enter a number"))+1):
    makhpilah*=i
print(makhpilah)

x=1
lis11=[i for i in range(1,int(input("please enter a number"))+1) ]
for x in lis11 :
    x*=s
print(lis11)
lis11(x)

#11
import random
print(random.randint(2,49))

luckyNumbers=[7,17,24,36,48]
remainGuesses=luckyNumbers.copy()# copy of the lucky list
guesses=[]#user right guess
counter=[] #guesses counter
while len(guesses) < len(luckyNumbers):
    if len(counter)==20:
        counter=[]
        guesses=[]
        remainGuesses = luckyNumbers.copy()
        print("here we go again")
    x=int(input(f"enter your guess ({len(counter)} guess)"))
    if x>49 or x<2:
        print('out of range')
        continue
    if x in counter:
        break
    if x in remainGuesses:
        guesses.append(x)
        remainGuesses.remove(x)
    counter.append(x)
if len(guesses)==len(luckyNumbers):
    print(f'we have a winner  counter = {len(counter)}')
else:
    print("you entered the same number twice")










