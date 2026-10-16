
import streamlit as st
from gtts import gTTS
from io import BytesIO
import os
from pyngrok import ngrok

st.set_page_config(page_title="Text to Speech", page_icon="🔊")

if "ngrok_url" not in st.session_state:
    try:
        token = os.environ.get("NGROK_AUTHTOKEN")

        if not token:
            st.error("NGROK_AUTHTOKEN is not set. Configure it in PowerShell before starting Streamlit.")
            st.stop()

        ngrok.set_auth_token(token)
        tunnel = ngrok.connect(8501)
        st.session_state.ngrok_url = tunnel.public_url
        print("Public URL:", tunnel.public_url)

    except Exception as e:
        st.error(f"Ngrok connection failed: {e}")
        st.stop()

st.title("🔊 Text to Speech")

text = st.text_area("Enter your text:", height=150)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te"
}

lang_name = st.selectbox("Language:", list(languages.keys()))
slow = st.checkbox("Speak slowly")

if st.button("Convert to Speech"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating audio..."):
            try:
                tts = gTTS(
                    text=text,
                    lang=languages[lang_name],
                    slow=slow
                )

                audio = BytesIO()
                tts.write_to_fp(audio)
                audio.seek(0)

                audio_bytes = audio.getvalue()

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="Download MP3",
                    data=audio_bytes,
                    file_name="speech.mp3",
                    mime="audio/mp3"
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
