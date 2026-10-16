# 🔊 Text-to-Speech Converter

A simple and interactive **Text-to-Speech (TTS) web application** built with Python and Streamlit. This application converts written text into natural-sounding speech in multiple languages and allows users to listen to and download the generated audio as an MP3 file.

## ✨ Features

- 📝 **Text Input:** Enter text to convert into speech.
- 🌐 **Multilingual Support:** Supports English, Hindi, Kannada, Marathi, Tamil, and Telugu.
- 🐢 **Slow Speech Mode:** Adjust speech speed for easier listening.
- 🔊 **Audio Playback:** Listen to generated speech directly in your browser.
- 📥 **MP3 Download:** Download generated speech for offline use.
- 🌍 **Public Access:** Share the application online using ngrok tunneling.
- ⚡ **Interactive UI:** Simple and user-friendly interface powered by Streamlit.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Web application framework
- **gTTS (Google Text-to-Speech)** — Speech generation
- **Pyngrok** — Secure tunneling for public access
- **BytesIO** — In-memory audio processing

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hussain205/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```

Replace `YOUR-REPOSITORY-NAME` with your actual repository name.

### 2. Install Dependencies

```bash
python -m pip install streamlit gTTS pyngrok
```

### 3. Configure ngrok

Create an account at [ngrok](https://dashboard.ngrok.com/signup) and obtain your authentication token.

Set the token in PowerShell:

```powershell
$env:NGROK_AUTHTOKEN="YOUR_NGROK_TOKEN"
```

Keep your authentication token private and never commit it to GitHub.

### 4. Run the Application

```bash
python -m streamlit run 4.py
```

Open the local URL displayed in your terminal. The ngrok public URL will also be available when the tunnel starts successfully.

## 📖 How to Use

1. Enter your text in the input area.
2. Select your preferred language.
3. Enable **Speak slowly** if required.
4. Click **Convert to Speech**.
5. Listen to the generated audio.
6. Click **Download MP3** to save the audio file.

## 🌍 Supported Languages

| Language | Code |
|---|---|
| English | `en` |
| Hindi | `hi` |
| Kannada | `kn` |
| Marathi | `mr` |
| Tamil | `ta` |
| Telugu | `te` |

## 🎯 Use Cases

- Language learning and pronunciation practice
- Accessibility and text reading
- Educational applications
- Audio content creation
- Multilingual speech generation

## ⚠️ Requirements

- Python 3.9 or later
- Internet connection for Google Text-to-Speech
- ngrok account and authentication token for public access

## 🔒 Security

Never upload your ngrok authentication token or other secrets to a public repository. Use environment variables to store credentials securely.

## 👨‍💻 Author

**Hussain Kola**

AI & Machine Learning Engineering Student | Aspiring AI Engineer

- GitHub: [@hussain205](https://github.com/hussain205)

---

⭐ If you find this project useful, consider giving the repository a star!
