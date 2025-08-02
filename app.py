import streamlit as st
from PIL import Image

# ---- TITLE AND HEADER ----
st.title("🌍 Hello World App")
st.header("👋 Welcome to Your Interactive Streamlit App")
st.subheader("🚀 Let's explore Streamlit features")

# ---- BASIC TEXT AND FORMATTING ----
st.markdown("### 📄 Text and Markdown")
st.text("This is plain text.")
st.markdown("> 💡 This is a blockquote.")
st.code("def hello():\n    print('Hello, World!')", language='python')

# ---- USER INPUT ----
st.markdown("### ✍ User Input")
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, *{name}*! 👋")

# ---- BUTTON ----
st.markdown("### 🔘 Button")
if st.button("Click Me!"):
    st.balloons()
    st.info("🎉 You clicked the button!")

# ---- SELECTBOX ----
st.markdown("### 🎨 Choose Your Favorite Color")
color = st.selectbox("Pick a color:", ["Red", "Green", "Blue"])
st.write(f"You selected: {color}")

# ---- SLIDER ----
st.markdown("### 😊 Mood Slider")
mood = st.slider("How happy are you today?", min_value=0, max_value=100, value=50)
st.write(f"Happiness level: {mood}/100")

# ---- IMAGE ----
st.markdown("### 🖼 Image Display")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/640px-Cat_poster_1.jpg",
    caption="A cute kitten 🐱",
    use_container_width=True
)

# ---- EXPANDER (FIXED) ----
st.markdown("### 📦 Expander Section")
with st.expander("🔽 Click here to expand"):
    st.write("✅ This is some hidden content inside the expander.")
    st.markdown("- You can add text, images, or even charts here.")
    st.markdown("- It's great for keeping your UI clean!")

# ---- COLUMNS ----
st.markdown("### 🧱 Columns Section")
left_col, right_col = st.columns(2)

with left_col:
    st.success("✅ This is the left column")
    st.write("You can add text, images, or widgets here.")

with right_col:
    st.warning("⚠ This is the right column")
    st.write("Each column acts like its own mini page.")

# ---- FOOTER ----
st.markdown("---")

