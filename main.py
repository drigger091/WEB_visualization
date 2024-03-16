import os

# reuirment modules
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# set page configuation

st.set_page_config(page_title = "Data Visualization", layout="wide",page_icon ="📊")


#title of the image
st.title("📊 Data Visualizer - web application")


#getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

data_path = f"{working_dir}/datas"

#list the files in data folder

files = [f for f in os.listdir((data_path)) if f.endswith(".csv")]

#drop down for the files

selected_file = st.selectbox("Select a file",files, index = None)

st.write(selected_file)

if selected_file :

    #get the complete path of the selected file

    file_path = os.path.join(data_path,selected_file)

    # reading the file as datframe
    df = pd.read_csv(file_path)
    column1 , column2 = st.columns(2)

    columns = df.columns.tolist()

    with column1:
        st.write("")
        st.write(df.head(6))

    with column2:

        # user selection of df  columns to plot
        x_axis = st.selectbox("Select the X-axis",options = columns + ["None"],index =None)
        y_axis = st.selectbox("Select the Y-axis",options = columns + ["None"],index = None)

        plotlist = ['Line Plot', "Bar Chart","Scatter Plot","Distribution plot","Count plot"]

        selected_plot = st.selectbox("Select a plot", options = plotlist)

        st.write("X axis selected is:--- ",x_axis)
        st.write("Y axis selected is :---- ",y_axis)
        st.write("Visualization type selected is :--- ",selected_plot)

# buton to genrerate plots
        
if st.button('Generate Plot'):

    fig , ax = plt.subplots(figsize=(8,6))

    if selected_plot == 'Line Plot':
        sns.lineplot(x = df[x_axis],y = df[y_axis],ax=ax)

    elif selected_plot == "Bar Chart":
        sns.barplot(x = df[x_axis],y = df[y_axis],ax=ax)

    elif selected_plot == "Scatter Plot":
        sns.scatterplot(x = df[x_axis],y = df[y_axis],ax=ax)

    elif  selected_plot == "Distribution plot":
        sns.histplot(x = df[x_axis],kde=True ,ax=ax)
        y_axis = "Density"
    
    elif selected_plot == "Count plot":
        sns.countplot(x=df[x_axis],ax=ax)
        y_axis = "Count"



    # adjusting the label size
    ax.tick_params(axis ="x",labelsize = 12)
    ax.tick_params(axis ="y",labelsize = 12)

    # adjust the title and labels
    plt.title(f'{selected_plot} of {y_axis} vs{x_axis}',fontsize =142)
    plt.xlabel(x_axis,fontsize = 12)
    plt.ylabel(y_axis,fontsize = 12)


    #show results

    st.pyplot(fig)