#!/usr/bin/env python
# coding: utf-8

# In[1]:


#задание 1
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

print(set(sum(ids.values(), [])))


# In[2]:


#задание 2
queries = [
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

storage = {}

for query in queries:
    words = query.split()

    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage.update({
            len(words): 1
        })

for key, value in storage.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)')


# In[3]:


#задание 3
results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}

for key, value in results.items():
    value['ROI'] = round(((value['revenue'] / value['cost']) - 1)*100 , 2)

    print(key, value)


# In[4]:


#задание 4
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
print('Максимальный объем продаж на рекламном канале:', max(stats, key = lambda k: stats[k]))


# In[ ]:




