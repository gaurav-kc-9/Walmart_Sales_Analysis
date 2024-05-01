#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df = pd.read_csv('Walmart Sales.csv')


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe( )


# In[9]:


df.shape


# In[10]:


df.isnull().sum()


# In[12]:


df.head( )


# In[19]:


columns_to_remove = [ 'Unnamed: 12', 'Unnamed: 13','Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20']


# In[20]:


df = df.drop(columns= columns_to_remove)


# In[21]:


df.head( )


# In[22]:


df.tail( )


# In[23]:


rows_tobe_remove = [1000, 1001]


# In[25]:


df = df.drop(rows_tobe_remove)


# In[26]:


df.tail( )


# In[27]:


df.isnull().sum()


# In[28]:


df['Unit price'] = pd.to_numeric(df['Unit price'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')


# In[29]:


df['Sales'] = df['Unit price'] * df['Quantity']


# In[30]:


city_sales = df.groupby('City')['Sales'].sum().reset_index()
city_revenue = df.groupby('City')['Sales'].mean().reset_index()


# In[31]:


city_sales.rename(columns={'Sales': 'Total Sales'}, inplace=True)
city_revenue.rename(columns={'Sales': 'Average Revenue'}, inplace=True)


# In[32]:


print("Total Sales by City:")
print(city_sales)
print("\nAverage Revenue by City:")
print(city_revenue)


# In[33]:


branch_sales = df.groupby('Branch')['Sales'].sum().reset_index()
branch_revenue = df.groupby('Branch')['Sales'].mean().reset_index()


# In[34]:


branch_sales.rename(columns={'Sales': 'Total Sales'}, inplace=True)
branch_revenue.rename(columns={'Sales': 'Average Revenue'}, inplace=True)


# In[35]:


print("Total Sales by Branch:")
print(branch_sales)
print("\nAverage Revenue by Branch:")
print(branch_revenue)


# In[45]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[47]:


plt.figure(figsize=(10, 6))


# In[48]:


plt.subplot(1, 2, 1)
sns.barplot(x='Branch', y='Total Sales', data=branch_sales)
plt.title('Total Sales by Branch')


# In[49]:


plt.subplot(1, 2, 2)
sns.barplot(x='Branch', y='Average Revenue', data=branch_revenue)
plt.title('Average Revenue by Branch')


# In[52]:


plt.subplot(1, 2, 1)
sns.barplot(x='City', y='Total Sales', data=city_sales)
plt.title('Total Sales by City')
plt.xticks(rotation=45)


# In[53]:


plt.subplot(1, 2, 2)
sns.barplot(x='City', y='Average Revenue', data=city_revenue)
plt.title('Average Revenue by City')
plt.xticks(rotation=45)


# In[60]:


branch_city_wise_avgprice = df.groupby(['City', 'Branch'])['Unit price'].mean().reset_index()


# In[61]:


print(branch_city_wise_avgprice)


# In[66]:


plt.figure(figsize=(6, 4))
sns.barplot(x='Unit price', y='Branch', hue='City', data=avg_price_per_branch_city)
plt.title('Average Price of Items Sold by Each Branch and City')
plt.xlabel('Branch')
plt.ylabel('Average Price of Items Sold')
plt.legend(title='City')
plt.show()


# In[67]:


df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month


# In[68]:


sales_revenue_overmonths = df.groupby(['Product line', 'Month'])[['Sales']].sum().reset_index()


# In[70]:


plt.figure(figsize=(10, 5))

sns.lineplot(data = sales_revenue_overmonths, x='Month', y='Sales', hue='Product line', marker='o')
plt.title('Monthly Sales of each Product')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))  
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 

plt.tight_layout()
plt.show()


# In[71]:


sales_revenue_overmonths = df.groupby(['Gender', 'Month'])[['Sales']].sum().reset_index()


# In[74]:


sns.lineplot(data = sales_revenue_overmonths, x='Month', y='Sales', hue='Gender', marker='o')
plt.title('Monthly Sales by Male and Female')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))  # Set x-axis ticks to show all months
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot

plt.tight_layout()
plt.show()


# In[76]:


monthly_sales = df.groupby(['Payment', 'Month'])[['Sales']].sum().reset_index()



# In[77]:


print(monthly_sales)


# In[78]:


plt.figure(figsize=(10, 5))

sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Payment', marker='o')
plt.title('Monthly Sales by Different Payment Method')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))  
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 

plt.tight_layout()
plt.show()


# In[ ]:




