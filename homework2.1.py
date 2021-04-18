#!/usr/bin/env python
# coding: utf-8

# In[1]:


#задание1

s = input('Введите  слово:')
 
s1 = len(s)
s2 = s1 / 2
if s1 % 2 == 0:
    print(s[int(s2)-1:int(s2)+1])
elif s1 % 2 !=0:
    print(s[int(s2)])


# In[2]:


#задание2
a = int(input('Введите  число:'))
sum = 0
while a != 0:
    sum += a
    a = int(input())
 
print(sum)


# In[3]:


#задание3
boys = ['Peter','Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys)==len(girls):
    print("Идеальная пара:")
    boys.sort()
    girls.sort()
    dating = zip(boys, girls)
    for company in dating:
        print(f"{company[0]} и {company[1]}")
else:
 
    print("Кто-то может остаться без пары")


# In[5]:


#задание4
countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

for i in countries_temperature: 
    print(i[0], '-', round((sum(i[1]) / len(i[1]) - 32) / 1.8, 1), 'C')


# In[ ]:




