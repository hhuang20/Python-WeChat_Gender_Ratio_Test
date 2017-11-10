
# coding: utf-8

# In[1]:

get_ipython().system('pip install itchat')


# In[1]:

import itchat
itchat.login()


# In[2]:

friends = itchat.get_friends(update = True)[0:]

male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1
total = len(friends[1:])
print("男性好友：%.2f%%"%(float(male)/total*100)+"\n"+ 
      "女性好友：%.2f%%"%(float(female)/total*100)+
      "\n"+"其他：%.2f%%"%(float(other)/total*100))


# In[3]:

import matplotlib.pyplot as plt
import numpy as np
female_percent = float(female)/total
male_percent = float(male)/total
other_percent = float(other)/total
list = [female_percent,male_percent,other_percent]
plt.bar(left = (0,1,2),height = (female_percent,male_percent,other_percent),width = 0.4, align = "center")
plt.xticks((0,1,2),("female","male","other"))
plt.show()


# In[4]:

labels = ["female","male","other"]
colors = ["paleturquoise","lightcoral","cornsilk"]
plt.pie(list,labels = labels,autopct='%1.2f%%',colors = colors,explode = (0.02,0.02,0.02))
name = friends[0]["NickName"]
#plt.title("Tiger's WeChat Gender Ratio",y=0.9)
plt.axis('equal')
plt.savefig("%s.jpg"%name)
plt.show()


# In[5]:

itchat.logout()


# In[ ]:



