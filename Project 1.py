#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1.Find the relationship between top 5 Job designation and total Purchase amount
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('Ecommerce_Purchases.csv')
grouped_data = data.groupby('Job')['Purchase Price'].sum().reset_index()
top_5_jobs1 = grouped_data.sort_values('Purchase Price', ascending=False).head(5)
ax = sns.barplot(x = "Job", y = "Purchase Price", data = top_5_jobs1)
ax.set(xlabel="Profession", ylabel = "Total Purchase",title="Top 5 Jobs by Total Purchase Amount")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[14]:


#2.Find the relationship between Job designation and mean Purchase amount

data = pd.read_csv('Ecommerce_Purchases.csv')
Mean_grouped_data = data.groupby('Job')['Purchase Price'].mean().reset_index()
top_5_jobs2 = Mean_grouped_data.sort_values('Purchase Price', ascending=False).head(5)
ax = sns.barplot(x = "Job", y = "Purchase Price", data = top_5_jobs2)
ax.set(xlabel="Professional", ylabel = "Avg Purchase",title="Relationship between Job designation and mean Purchase amount")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[11]:


#3.How does purchase value depend on the Internet Browser used and Job (Profession) of the purchaser?
#Group by job and browser preferences
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Ecommerce_Purchases.csv')
jobBrowser = data.groupby(by=['Job', 'Browser'], as_index=False, )['Purchase Price'].count() 
plt.title(f"Browser Preferences of largest job groups :")
ax = sns.barplot(x = "Purchase Price_y", y = "Job",hue="Browser" ,  
                 orient = 'h', data = top_5_jobs1.merge(jobBrowser,on = 'Job' ,how = 'inner')) #merge with top 5 jobs
ax.set(ylabel="Job", xlabel = "Total Count of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()




# In[57]:


data = pd.read_csv('Ecommerce_Purchases.csv')
Mean_grouped_data = data.groupby('Job')['Purchase Price'].mean().reset_index()
top_5_jobs2 = Mean_grouped_data.sort_values('Purchase Price', ascending=False).head(5)
jobBrowser = data.groupby(by=['Job', 'Browser'], as_index=False, )['Purchase Price'].count() 
plt.title(f"Browser Preferences of largest job groups :")
ax = sns.barplot(x = "Purchase Price_y", y = "Job",hue="Browser" ,  
                 orient = 'h', data = top_5_jobs2.merge(jobBrowser,on = 'Job' ,how = 'inner')) #merge with top 5 jobs
ax.set(ylabel="Job", xlabel = "Total Count of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()



# In[19]:


#4.What are the patterns, if any, on the purchases based on Location (State) and time of purchase (AM or PM)?

group=data.groupby(by='State', as_index=False)['Purchase Price'].count()
group = group.sort_values(by='Purchase Price', ascending=False).iloc[:5,:]
group1=data.groupby(by=['State','AM or PM'], as_index=False)['Purchase Price'].count()
group1= group1.sort_values(by='Purchase Price', ascending=False)

plt.title('Most purchases done by State (locations) and time')
ax = sns.barplot(x = "Purchase Price_y", y = "State",hue="AM or PM" , orient = 'h', \
                 data = group.merge(group1, on = 'State', how = 'inner'))
ax.set(ylabel="Top ordering states", xlabel = "Total Count of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[18]:


#5.How does purchase depend on ‘CC’ provider and time of purchase ‘AM or PM’?
fig, axarr = plt.subplots(1, 2, figsize=(24, 5))
CC_data_hue_cnt = data.groupby(by=['CC Provider','AM or PM'], as_index=False)['Purchase Price'].count()
ax = sns.barplot(y = 'CC Provider', x = 'Purchase Price' ,hue='AM or PM', orient = 'h', data = CC_data_hue_cnt,\
            color = 'darkviolet', ax=axarr[0])
ax.set(xlabel="Number of Orders", ylabel='CC Provider')
axarr[0].set_title("CC Provider usage count at different times", fontsize=15)

CC_data_hue_sum = data.groupby(by=['CC Provider','AM or PM'], as_index=False)['Purchase Price'].sum()
ax = sns.barplot(y = 'CC Provider', x = 'Purchase Price' ,hue='AM or PM', orient = 'h', data = CC_data_hue_sum,\
            color = 'saddlebrown', ax=axarr[1])
ax.set(xlabel="Purchase Value", ylabel=None)
axarr[1].set_title("CC Provider usage value at different times", fontsize=15)
plt.show()


# In[ ]:





# In[12]:


#6.What are top 5 Location(State) for purchases?
fig, axarr = plt.subplots(1, 2, figsize=(24, 5))
#print number of purchase
group2=data.groupby(by='State', as_index=False).count()[['State','Purchase Price']]
group2 = group2.sort_values(by='Purchase Price', ascending=False).head()
ax = sns.barplot(x = "State", y = "Purchase Price", data = group2, ax=axarr[0])
axarr[0].set_title("Top Most Number of Purchases done by Location(State)", fontsize=15)
ax.set(xlabel=None, ylabel = "Total Number of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

#print amount of purchase
group2=data.groupby(by='State', as_index=False).sum()[['State','Purchase Price']]
group2 = group2.sort_values(by='Purchase Price', ascending=False).head()
ax = sns.barplot(x = "State", y = "Purchase Price", data = group2, ax=axarr[1])
axarr[1].set_title("Top Most Value of Purchases done by Location(State)", fontsize=15)
ax.set(xlabel=None, ylabel = "Total Value of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()


# In[ ]:




