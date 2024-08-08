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