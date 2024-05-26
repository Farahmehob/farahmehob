quiz=open('./New Text Document.txt','r(
Name=input('Enter Your Full Name')
Age=input('Enter Your Age')
Number=input('Enter Your Number')
a =[]
ca = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,17,18,19,20]
result = 0
print(f'Student Info:Name:{Name},Age:{Age},Number:{Number}')
print('Start!')
for Q in range(20):
  A=input(f'{quiz.readline()}')
  a.append(A)
for i in range (20):
  if a[i] == ca[i] :
   result += 0.5
import json
Details={"Name":Name,"Age":Age,"Number":Number,"Result":result}
with open(".\Result.json","w") as  file:
             json.dump(Details,file)
