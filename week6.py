tuple1=(1,1,32,2,'cuc')
print(tuple1)
list1=(1,1,32,'cuc')
print(list1)

myList=(1,2,3,5,4)
print(sorted(myList))

score_list=[100,95,85,60,65,70]
print(score_list)
print(score_list[3])
score_list.append(50)
print(score_list)

del(score_list[6])
print(score_list[3:7])
print(score_list)

score_list.append([1,2,3,'I am from CUC',True])
print(score_list)

second_list=[11,22,33]
second_list.append([44,55,66])
score_list.append(second_list)
print(score_list)

score_list.remove(100)
print(score_list)

dict1={'Peter':80,'David':90,'Mary':100}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1['David'])
score_list=[]
score_list.append(dict1)
print(score_list)

my_set={1,'Hello',(1,2,3)}
print(my_set)
print(type(my_set))

test1={'Peter':50,'David':60,'Mary':70}
assignment1={'Peter':50,'David':70,'Mary':80}
score_list=[]
score_list.append(test1)
score_list.append(assignment1)
print(score_list)

my_set={1,2,2,3,4,4,5}
print(my_set)

i=1
for i in range(1,10):
print(i)

hrs_list=[30,40,50,60]
rate_list=[65,75,65,75]
name_list=['John','Mike','Mary','Jane']
fee_list=[]
for number in range(len(name_list)):
    hrs=hrs_list[number]
    rate=rate_list[number]
    fee=hrs*rate
    fee_list.append(fee)
    money_made=name_list[number]+'makes'+str(fee)+'.'
print(money_made)

money_list=[]
money_list.append(name_list)
money_list.append(fee_list)
print(money_list)

my_list=['red','green','blue','orange','black']
index=0
for i in my_list:
    if i=='blue':
        print(index,'Blue is printed.')
        index+=1
    else:
        print(index,my_list[index])
        index=index+1
print('This is done.')

import pandas as pd
df1=pd.DataFrame({
    'Product ID':[1,2,3,4],
    'Product Name':['T-shirt','Shirt','Jeans','Coat'],
    'Color':['Blue','Green','Red','Trench'],
    'Units sold':[250,300,180,200]
})
print(df1)
