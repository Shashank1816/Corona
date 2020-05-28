#!/usr/bin/env python
# coding: utf-8

# # Effect Corona in India

# ### 1) Importing necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
print("imported")


# ### 2) Importing and Reading the dataset

# In[73]:


C_India=pd.read_csv("covid_apr.csv")


# ### 3) Displaying the Dataset

# In[3]:


C_India


# ### 4) Installing and importing folium library

# In[4]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# ### 5 ) Locating India

# In[19]:


india=folium.Map(location=[20.5937,78.9629],zoom_start=5)
india


# In[35]:


loc=[20.5937,78.9629]
india=folium.Map(location=loc,tiles='Stamen terrain',zoom_start=5)
india


# ## 6) Marking Death counts in each state

# In[44]:


deaths=folium.map.FeatureGroup()

for lat,long in zip(C_India.Lat,C_India.Long):
    deaths.add_child(folium.features.CircleMarker([lat,long],radius=5,color='red',fill=True,fill_color='purple',fill_opacity=0.6))
    
# adding markers on the map
india.add_child(deaths)


# ### Converting TCC to String

# In[65]:


C_India[['TCC']].astype(str)


# # Marking Labels For Total Corona Cases

# In[71]:


total_cases = folium.map.FeatureGroup()

for lat, lng, in zip(C_India.Lat, C_India.Long):
    total_cases.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5,
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(C_India.Lat)
longitudes = list(C_India.Long)
labels=list(C_India.TCC.astype(str))
for lat, lng, lab in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=lab).add_to(india)    
    
india.add_child(total_cases)        


# # Marking Labels For total Number of Deaths in Each State

# In[72]:


death_count = folium.map.FeatureGroup()

for lat, lng, in zip(C_India.Lat, C_India.Long):
    death_count.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, 
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

latitudes = list(C_India.Lat)
longitudes = list(C_India.Long)
labels=list(C_India.Death.astype(str))
for lat, lng, lab in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=lab).add_to(india)    
    
india.add_child(death_count)


# ## Labels For Cured Cases

# In[80]:


cured = folium.map.FeatureGroup()

for lat, lng, in zip(C_India.Lat, C_India.Long):
    cured.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, 
            color='green',
            fill=True,
            fill_color='white',
            fill_opacity=0.6
        )
    )

latitudes = list(C_India.Lat)
longitudes = list(C_India.Long)
labels=list(C_India.Cured.astype(str))
for lat, lng, lab in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=lab).add_to(india)    
    
india.add_child(cured)


# In[ ]:




