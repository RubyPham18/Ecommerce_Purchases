#!/usr/bin/env python
# coding: utf-8

# In[50]:


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


# In[51]:


#3.How does purchase value depend on the Internet Browser used and Job (Profession) of the purchaser?
#Group by job and browser preferences
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



# In[61]:


#4.What are the patterns, if any, on the purchases based on Location (State) and time of purchase (AM or PM)?

res=data.groupby(by='State', as_index=False)['Purchase Price'].count()
res = res.sort_values(by='Purchase Price', ascending=False).iloc[:5,:]
res4=data.groupby(by=['State','AM or PM'], as_index=False)['Purchase Price'].count()
res4= res4.sort_values(by='Purchase Price', ascending=False)

plt.title('Most purchases done by State (locations) and time')
ax = sns.barplot(x = "Purchase Price_y", y = "State",hue="AM or PM" , orient = 'h', \
                 data = res.merge(res4, on = 'State', how = 'inner'))
ax.set(ylabel="Top ordering states", xlabel = "Total Count of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[64]:


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





# In[73]:


#6.What are top 5 Location(State) for purchases?
fig, axarr = plt.subplots(1, 2, figsize=(24, 5))
#print('The TOP 5 Locations(state) with number of purchase...')
res=data.groupby(by='State', as_index=False).count()[['State','Purchase Price']]
res = res.sort_values(by='Purchase Price', ascending=False).head()
ax = sns.barplot(x = "State", y = "Purchase Price", data = res, ax=axarr[0])
axarr[0].set_title("Top Most Number of Purchases done by Location(State)", fontsize=15)
ax.set(xlabel=None, ylabel = "Total Number of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

#print('The TOP 5 Locations(state) with max amount of purchase...')
res=data.groupby(by='State', as_index=False).sum()[['State','Purchase Price']]
res = res.sort_values(by='Purchase Price', ascending=False).head()
ax = sns.barplot(x = "State", y = "Purchase Price", data = res, ax=axarr[1])
axarr[1].set_title("Top Most Value of Purchases done by Location(State)", fontsize=15)
ax.set(xlabel=None, ylabel = "Total Value of Purchases")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()

