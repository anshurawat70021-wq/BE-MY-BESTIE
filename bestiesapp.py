import streamlit as st

# Page config
st.set_page_config(page_title="Bestie Application 💕", page_icon="💖", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #ff4b91;'>💖 Bestie Application 💖</h1>", unsafe_allow_html=True)
st.write("Fill this form to see if you qualify to be my bestie 👀✨")

# Form
name = st.text_input("What's your name? 🌸")

fav_color = st.selectbox(
    "Choose your favorite color 🎨",
    ["Pink 💕", "Black 🖤", "Blue 💙", "Purple 💜", "Other"]
)

loyalty = st.slider("How loyal are you? 🤝", 0, 10, 5)

secrets = st.radio(
    "Can you keep secrets? 🤫",
    ["Yes, always!", "Maybe...", "No 😬"]
)

fun = st.slider("Fun level 🎉", 0, 10, 5)

late_reply = st.radio(
    "Will you reply late? 📱",
    ["Never!", "Sometimes", "Always 😒"]
)

# Button
if st.button("Check Result 💌"):
    score = 0

    # Conditions
    if loyalty >= 7:
        score += 1
    if secrets == "Yes, always!":
        score += 1
    if fun >= 6:
        score += 1
    if late_reply == "Never!":
        score += 1

    st.subheader("✨ Result ✨")

    if score == 4:
        st.success(f"OMG {name} 😭💖 YOU ARE MY BESTIE NOW!!! 💕👯‍♀️")
        st.balloons()
    elif score >= 2:
        st.warning(f"{name}, you passed... but on thin ice 😏💅")
    else:
        st.error(f"{name} 😤 Sorry, you don't qualify to be my bestie 🚫")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with 💕 using Streamlit</p>", unsafe_allow_html=True)
