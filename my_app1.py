import streamlit as st
st.write("hello world: getting bore , hello brother!!")
st.title ("display title use st.title()")
st.write("to write test use st.write()")
st.header("i am header to write header use st.header()")
st.subheader("i am subheader to write subheader use st.subheader()")
st.text("hey i am simple text to write simple text use st.text()")
#to create hyperlink
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[Streamlit CheatSheet](https://cheat-sheet.streamlit.app/)")
st.success("success")
st.info("information")
st.warning("this is warning")
st.error("this is an error!!")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes= video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TIS")

audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")

st.header("Button widgets")

if st.button("Play1"):
    st.text("Hellow world")

if st.button("Play2"):
    st.text("Enjoy music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
    
# radio_but=st.radio("your selecttion",["male","female"])
# if radio_but=="female":
#     st.info("you are female")
# else:
#     st.info("you are male")

radio_but=st.sidebar.radio("your selecttion",["male","female"])
if radio_but=="female":
    st.info("you are female")
else:
    st.info("you are male")

# city=st.selectbox("your city",["daman","diu","valsad","selvas"])
# if city=="daman":
#     st.info("i love daman")
# elif city=="diu":
#     st.info("i love diu")
# elif city=="valsad":
#     st.info("i love valsad")
# else:
#     st.info("i love selvas")

city=st.sidebar.selectbox("your city",["daman","diu","valsad","selvas"])
if city=="daman":
    st.info("i love daman")
elif city=="diu":
    st.info("i love diu")
elif city=="valsad":
    st.info("i love valsad")
else:
    st.info("i love selvas")

occupation=st.multiselect("your occupation",["programmer","data scientist","ITcouncultant","DBA"])

age=st.number_input("input a number")

msg=st.text_area("about NIELIT","WRITE SOMETHING----")
msg=st.text_area("address","WRITE SOMTHINGS---")

select_var=st.sidebar.slider("select a value",1,20)
#starting value=10.0 and ending value =20.0 incfement by 0.5
select_val1=st.sidebar.slider("select a value",10.0,20.0,0.5)
if st.button("balloons"):
    st.balloons()

#-----pandas dataframe-----
import streamlit as st
import pandas as pd

auto_data=pd.read_csv("auto.csv")
st.dataframe(auto_data.head())

st.table(auto_data.head(10))

st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))

st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time

today=st.date_input("today is",datetime.datetime.now())
hour=st.time_input("the time is",datetime.time(12,30))

st.code("import pandas as pd")
st.code("print(welcome to NIELIT Daman)")

import pandas as pd
import numpy as np

st.title("bar chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.bar_chart(df)

st.title("line chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.line_chart(df)

st.title("area chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.area_chart(df)