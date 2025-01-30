#import packages and library
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import streamlit as st


#Membuah fungsi yang akan menyiapkan berbagai dataframe tambahan yang dibutuhkan dari dataset utama
def create_usercasualregistered_df(df):
    colom_sum = ['casual', 'registered']
    total = df[colom_sum].sum()
    usercasualregistered_df = pd.DataFrame(total).T

    return usercasualregistered_df

def create_userbyyear_df(df):
    userbyyear_df = df.groupby(by=['year',]).agg({
        'casual' : 'sum',
        'registered' : 'sum'
    }).reset_index()

    return userbyyear_df

def create_yeartimeline_df(df):
    yeartimeline_df= df.resample(rule='M', on='date').agg({
        "casual": "sum",
        "registered": "sum"
    })
    yeartimeline_df.index = yeartimeline_df.index.strftime('%Y-%m')
    yeartimeline_df = yeartimeline_df.reset_index()

    return yeartimeline_df

def create_userbyseason_df(df):
    userbyseason_df = df.groupby(by=['season',]).agg({
        'casual' : 'sum',
        'registered' : 'sum'
    }).reset_index()
    
    return userbyseason_df

def create_userbyweather_df(df):
    userbyweather_df = df.groupby(by=['weather',]).agg({
        'casual' : 'mean',
        'registered' : 'mean'
    }).reset_index()
    
    return userbyweather_df
 
def create_userbyday_df(df):
    userbyday_df = df.groupby(by=['day_of_week',]).agg({
        'casual' : 'sum',
        'registered' : 'sum'
    }).reset_index()

    return userbyday_df

def create_userbyworkingday_df(df):
    userbyworkingday_df = df.groupby(by=['workingday',]).agg({
        'casual' : 'mean',
        'registered' : 'mean'
    }).reset_index()

    return userbyworkingday_df

def create_userbyhour_df(df):
    userbyhour_df = df.groupby(by=['hour']).agg({
        'casual' : 'sum',
        'registered' : 'sum'
    }).reset_index()

    return userbyhour_df

#Membuat beberapa fungsi tambahan untuk mengubah format angka yang ada pada visualisasi data agar lebih menarik
def number_formating(value):
    return f"{value:,.0f}".replace(",", ".")

def number_formating2(value, pos):
    if value >= 10**9:
         return f'{value*1e-9:.1f} B'
    elif value >= 10**6:
         return f'{value*1e-6:.1f} M'
    elif value >=10**3:
         return f'{value*1e-3:.1f} K'
    else:
        return str(value)

#Mengambil dataset Utama
#Untuk dataset yang saya gunakan bukan dataset asli atau mentah tapi dataset yang sudah dibersihkan untuk melihat proses pembersihan datanya bisa melihat di file notebook.ipnyb
hour_df = pd.read_csv("clean_hourdata.csv")
day_df = pd.read_csv("clean_daydata.csv")

#Configurasi untuk web, seperti judul web dan layout
st.set_page_config(page_title="Bike Sharing Sytem",
                   layout="wide")

#Membuat variable max_date dan min_date dari colom date untuk dijadikan filter data
datetime_columns = ['date']
hour_df.sort_values(by="date", inplace=True)
hour_df.reset_index(inplace=True)

day_df.sort_values(by="date", inplace=True)
day_df.reset_index(inplace=True)

for column in datetime_columns:
    hour_df[column] = pd.to_datetime(hour_df[column])
    day_df[column] = pd.to_datetime(day_df[column])

min_date_day = day_df['date'].min()
max_date_day = day_df['date'].max()

#Membuat Side yang berisi logo judul dan filter
with st.sidebar:
    st.image("logo.png")
    st.header("2011 - 2012 Performance Report")

    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date_day,
        max_value=max_date_day,
        value=[min_date_day, max_date_day]
    )

main_hour_df = hour_df[(hour_df['date'] >= str(start_date)) &
                       (hour_df['date'] <= str(end_date))]
main_day_df = day_df[(day_df['date'] >= str(start_date)) &
                       (day_df['date'] <= str(end_date))]

#Membuat dataset tambahan dengan fungsi yang telah dibuat
usercasualregistered_df = create_usercasualregistered_df(main_day_df)
userbyyear_df = create_userbyyear_df(main_day_df)
yeartimeline_df = create_yeartimeline_df(main_day_df)
userbyseason_df = create_userbyseason_df(main_day_df)
userbyweather_df = create_userbyweather_df(main_hour_df)
userbyday_df = create_userbyday_df(main_day_df)
userbyworkingday_df = create_userbyworkingday_df(main_day_df)
userbyhour_df = create_userbyhour_df(main_hour_df)

#Judul Utama
st.header('Project Dicoding : Bike Sharing Sytem')

st.text("")
st.text("")
st.text("")

#Sub untuk menghitung seluruh total rentals
st.subheader('Total Rentals')

col1, col2, col3 = st.columns(3)
with col1:
    casual_user = main_day_df.casual.sum()
    st.metric("Casual User", value=number_formating(casual_user))
with col2:
    registered_user = main_day_df.registered.sum()
    st.metric("Registered User", value=number_formating(registered_user))
with col3:
    total_user = main_day_df.total_user.sum()
    st.metric("Total User", value=number_formating(total_user))

st.text("")
st.text("")

#GraphikPertanyaan No.1
st.subheader("Casual User vs Registered User")

casual_user = main_day_df.casual.sum()
registered_user = main_day_df.registered.sum()
data = [casual_user, registered_user]
label = ['Casual', 'Registered']
fig,ax = plt.subplots()
ax.pie(data, autopct='%1.0f%%', colors=['#0D9488','#FB923C'])
ax.legend(
    labels=label, 
    loc='upper left', 
    bbox_to_anchor=(1, 1), 
    title='Tipe Pengguna',
    fontsize=12
)
st.pyplot(fig)

st.text("")
st.text("")

#Grafik Pertanyaan No 2

st.subheader("Total User per Year")
X_axis = np.arange(len(userbyyear_df['year']))
fig, ax = plt.subplots()
ax.bar(X_axis - 0.2, userbyyear_df['casual'], 0.4, label='Casual User', color='#0D9488')
ax.bar(X_axis + 0.2, userbyyear_df['registered'], 0.4, label='Registered User', color='#FB923C')
ax.set_xticks(X_axis)
ax.set_xticklabels(userbyyear_df['year'])
ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
ax.legend()
st.pyplot(fig) 

st.subheader("Timeline Total User")
X_axis = np.arange(len(yeartimeline_df['date']))
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(X_axis, yeartimeline_df['casual'], label = 'Casual User', color='#0D9488', marker='o', markersize=6)
ax.plot(X_axis, yeartimeline_df['registered'], label = 'Registered User', color='#FB923C', marker='o', markersize=6)
for i in range(len(X_axis)):
    ax.plot([X_axis[i], X_axis[i]], [0, yeartimeline_df['casual'][i]], 'k--', alpha=0.5)  # Garis untuk Casual User
    ax.plot([X_axis[i], X_axis[i]], [0, yeartimeline_df['registered'][i]], 'k--', alpha=0.5)  # Garis untuk Registered User
ax.set_xticks(X_axis, yeartimeline_df['date'], rotation= 45, ha='right')
ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
ax.legend()
st.pyplot(fig)

st.text("")
st.text("")

#Grafik Pertanyaan No 3
st.subheader("Season and Weather Impact to Bike Sharing")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total User per Season")
    X_axis = np.arange(len(userbyseason_df['season']))
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(X_axis - 0.2, userbyseason_df['casual'], 0.4, label='Casual User', color='#0D9488' )
    ax.bar(X_axis + 0.2, userbyseason_df['registered'], 0.4, label='Registered User', color='#FB923C')
    ax.set_xticks(X_axis)
    ax.set_xticklabels(userbyseason_df['season'])
    ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Average User per Weather")
    X_axis = np.arange(len(userbyweather_df['weather']))
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(X_axis - 0.2, userbyweather_df['casual'], 0.4, label='Casual User', color='#0D9488')
    ax.bar(X_axis + 0.2, userbyweather_df['registered'], 0.4, label='Registered User', color='#FB923C')
    ax.set_xticks(X_axis)
    ax.set_xticklabels(userbyweather_df['weather'])
    ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
    ax.legend()
    st.pyplot(fig)

st.text("")
st.text("")

#Grafik Pertanyaan No. 4
st.subheader("Workingday, Weekday, Holiday")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total User per Day")
    X_axis = np.arange(len(userbyday_df['day_of_week']))
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(X_axis - 0.2, userbyday_df['casual'], 0.4, label='Casual User', color='#0D9488')
    ax.bar(X_axis + 0.2, userbyday_df['registered'], 0.4, label='Registered User', color='#FB923C')
    ax.set_xticks(X_axis)
    ax.set_xticklabels(userbyday_df['day_of_week'])
    ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Average User in Workingday vs Holiday")
    X_axis = np.arange(len(userbyworkingday_df['workingday']))
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(X_axis - 0.2, userbyworkingday_df['casual'], 0.4, label='Casual User', color='#0D9488')
    ax.bar(X_axis + 0.2, userbyworkingday_df['registered'], 0.4, label='Registered User', color='#FB923C')
    ax.set_xticks(X_axis)
    ax.set_xticklabels(userbyworkingday_df['workingday'])
    ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
    ax.legend()
    st.pyplot(fig)

st.text("")
st.text("")

#Grafik Pertanyaan No. 5
st.subheader("Total user in everyhour")
X_axis = np.arange(len(userbyhour_df['hour']))
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(X_axis, userbyhour_df['casual'], label = 'Casual User', color='#0D9488', marker='o', markersize=6)
ax.plot(X_axis, userbyhour_df['registered'], label = 'Registered User', color='#FB923C', marker='o', markersize=6)

for i in range(len(X_axis)):
    ax.plot([X_axis[i], X_axis[i]], [0, userbyhour_df['casual'][i]], 'k--', alpha=0.5)  # Garis untuk Casual User
    ax.plot([X_axis[i], X_axis[i]], [0, userbyhour_df['registered'][i]], 'k--', alpha=0.5)  # Garis untuk Registered User

ax.set_xticks(X_axis, userbyhour_df['hour'])
ax.yaxis.set_major_formatter(FuncFormatter(number_formating2))
ax.legend()
st.pyplot(fig)

st.text("")
st.text("")

##footer
st.caption('Project ini dibuat oleh : Tegar Kamarulzaman')
    