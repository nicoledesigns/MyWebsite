import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_welcome = load_lottieurl("https://lottie.host/d4118a51-82ae-4e7d-8135-a3c4974dffdd/3nDtWjEIrX.json")
lottie_coding = load_lottieurl("https://lottie.host/6e3e4dd8-7ca5-4ed6-9f64-ed7fa191a77d/vkFocxEFFP.json")

img_contact_form = Image.open("images/pet.png")
img2 = Image.open("images/project.png")
img3 = Image.open("images/chat.png")
img4 = Image.open("images/bibleapp.png") 

# Apply local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply styles
local_css("style/style.css")


# Create the layout
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2, 1])  

with left_column:
    st.subheader("Welcome to My Portfolio :wave:")
    st.title("Nicole Antoun")
    st.write(
        """
        I am a Software Engineering Student at Concordia University with strong skills in problem-solving, design, and full-stack development.  
        
        My goal is to transform technical knowledge into impactful, user-friendly solutions that help businesses grow.  
        
        I am highly motivated, quick to learn new technologies, and thrive in collaborative environments.  
        """
    )
    st.write("📄 [View My Resume](https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:bb8ccb1b-1a46-4ddd-87f8-4f832bbf36ea)") 
          
    with right_column:
        if lottie_welcome:
            st_lottie(lottie_welcome, height=400, key="welcome", width=400)  

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Core Skills")
        st.write(
            """
            - Creativity & Design Thinking  
            - Critical Analysis & Problem-Solving  
            - Full-Stack Web Development  
            - Adaptability & Continuous Learning  
            - Teamwork & Project Management  
            """
        )
       
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Highlighted Projects")
    st.write("##")

    # Project 1
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, use_container_width=True)
    with text_column:
        st.subheader("Pet Website")
        st.write(
            """
            A 7-page responsive website built with **HTML, CSS, and JavaScript**.  
            Designed for usability and aesthetics, earning a **97% grade**.  
            """
        )
        st.markdown("[🌐 View Project](https://ephemeral-pothos-cbb6ca.netlify.app)")

 
      # Project 2
image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img4, use_container_width=True)

with text_column:
    st.subheader("Bible App")
    st.write(
        """
        A Flutter app I built to make Bible reading and reflection more interactive.  

        - Read or listen to Scripture, highlight verses, and take notes  
        - Daily verses, prayer calendar, and verse search  
        - Biblical AI chat powered by **gpt-4o-mini**  
        - Built with **Flutter/Dart** and tested on iOS simulators via **Xcode**
        """
    )
  
    
    # Project 3
image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img3, use_container_width=True)
with text_column:
    st.subheader("ChatHaven (Team Project)")
    st.write(
            """
            A full-stack communication platform designed to improve **usability, privacy, and collaboration**.  

            - Built with **React, Express.js, and SQLite**  
            - Features include **group channels, private messaging, and media sharing**  
            - Developed using **Agile methodology**, enhancing teamwork and project management skills  
            """
    )

         
           # Project 4
image_column, text_column = st.columns((1, 2))
    
with image_column:
    st.image(img2, use_container_width=True)
with text_column:
    st.subheader("Portfolio Website")
    st.write(
            """
            Developed a personal portfolio using **Python (Streamlit) and CSS** with interactive **Lottie animations**.  
            This site demonstrates my ability to combine design and technical skills to create engaging user experiences.  
            """
    )
        

# Contact Me Section
with st.container():
    st.write("---")
    st.header("Get in Touch")
    st.write("##")
    
    contact_form ="""
    <form action="https://formsubmit.co/nicoleantounn@hotmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Message" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



