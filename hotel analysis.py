#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # loading dataset
# 

# In[2]:


df=pd.read_csv('hotel_bookings 2.csv')


# # Exploratory Data Analysis and Data Cleaning

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.info()


# In[8]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'],  format='%d/%m/%Y')


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.describe(include='object')


# In[12]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    
    print(df[col].count())
    
    print('-'*50)


# In[13]:


df.isnull()


# In[14]:


df.isnull().sum()


# In[15]:


df.drop(['company','agent'],axis=1, inplace=True)


# In[16]:


df.dropna(inplace=True)


# In[17]:


df.info()


# In[18]:


df.isnull().sum()


# In[19]:


df['adr'].plot(kind='box')


# In[20]:


df=df[df['adr']<5000]


# In[21]:


df.describe()


# # Data Analysis and Visualization

# In[22]:


can_per=df['is_canceled'].value_counts(normalize=True)
print(can_per)

plt.figure(figsize=(5,4))
plt.title('reservation status of hotel  ')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.8)
plt.show()


# In[23]:


plt.figure(figsize=(8,5))
a1=sns.countplot(x='hotel', hue='is_canceled', data=df , palette='Reds')
legend_labels,_ =a1.get_legend_handles_labels()
a1.legend(bbox_to_anchor=(1,1))
plt.title('reservation status in different hotels', size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservation')
plt.legend(['not canceled', ' canceled'])
plt.show()


# In[24]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[25]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[26]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[27]:


plt.figure(figsize=(20,10))
plt.title(' Average daily rate in city and resort ',fontsize=30)
plt.plot(resort_hotel.index , resort_hotel['adr'],label=' Resort Hotel')
plt.plot(city_hotel.index , city_hotel['adr'],label=' city Hotel')
plt.legend(fontsize=20)
plt.show()


# In[28]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
a1=sns.countplot(x='month',hue='is_canceled', data=df )
legend_labels,_=a1.get_legend_handles_labels()
a1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month ', size=20)
plt.xlabel('month')
plt.ylabel('number of reservation ')
plt.legend(['not cancled',' canceled'])
plt.show()


# In[29]:


plt.figure(figsize=(15,8))
plt.title('ADR per month', fontsize=30)
sns.barplot(x='month',y='adr', data= df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[30]:


cancelled_data= df[df['is_canceled']==1]
top10_country=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top10_country,autopct='%.2f',labels=top10_country.index)
plt.show()


# In[31]:


df['market_segment'].value_counts()


# In[32]:


cancelled_data['market_segment'].value_counts()


# In[46]:


cancelled_df_adr=cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date',inplace =True)

not_cancelled_data= df[df['is_canceled']==0]
not_cancelled_df_adr=not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace =True)

plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'] ,label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'] ,label='cancelled')
plt.legend()


# In[47]:


cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>='2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>='2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[49]:


plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'] ,label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'] ,label='cancelled')
plt.legend(fontsize=20)


# In[ ]:




