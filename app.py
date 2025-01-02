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

# Apply local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply styles
local_css("style/style.css")


# Create the layout
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2, 1])  # Adjust column widths as needed

with left_column:
    st.subheader("Welcome to My Website :wave:")
    st.title("Nicole Antoun")
    st.write(
        "As a Software Engineering Co-op Student at Concordia University, my goal is to use the most of what I learn from school, work, daily life and surrounding to accomplish the needs of your company as well as producing the best and most successful resolution. With me in your team, you can expect to see me learn fast and make your company grow."
    )
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("You can view my Resume here: [Resume](https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:b9f1cc6d-521f-4029-90b9-48b88b80dec7)") 
          
    with right_column:
        if lottie_welcome:
            st_lottie(lottie_welcome, height=400, key="welcome", width=400)  # Adjust height and width as needed

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Some of my skills:")
        st.write(
            """
            	&#10061; creativity and design\n  
            	&#10061; critical thinking\n
            	&#10061; problem assessment and analysis\n 
            	&#10061; adaptability\n
            """
        )
       
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("Pet Website")
        st.write(
            """
            In this project, I used HTML, CSS, and JavaScript to build and design my website pages. It includes 7 different pages. A high mark of 97% was given for it.   
            Take a look at my website here:
            """
        )
    with image_column:
        st.image(img2)
    with text_column:
    	
        st.markdown("[Nicole's Website](https://ephemeral-pothos-cbb6ca.netlify.app)")
        st.subheader("Nicole's Website")
        st.write(
            """
            In this project, I used Python and CSS to build and design my website, incorporating Lottie animations to enhance user experience. This highlights both my creativity and passion for web development.
            
            """
        )
        
        
        

# Contact Me Section
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
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

