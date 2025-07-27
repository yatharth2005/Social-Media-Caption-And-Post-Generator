# Social-Media-Caption-And-Post-Generator
# 🧠 Social Media Caption and Post Generator

This project is built as part of the **IBM Virtual Internship Program (PBEL)**. It leverages state-of-the-art open-source AI models to automate the creation of engaging social media captions, posts, hashtags, and emojis based on images or input themes.

<p align="center">
  <img src="screenshots/app_ui.png" width="600"/>
</p>

---

## 🚀 Features

🔹 **Image Captioning**  
Upload an image or provide a URL to automatically generate a descriptive and contextually relevant caption using BLIP.

🔹 **Theme-based Post Generation**  
Enter a theme (e.g., *"travel"*, *"fitness"*, *"motivation"*) and get a catchy post along with auto-generated emojis and hashtags using `Phi-2`.

🔹 **Post Enhancer**  
Improve a raw caption by adding relevant hashtags and emojis, making it perfect for platforms like Instagram, LinkedIn, and Twitter.

🔹 **Multilingual Support (Optional)**  
Translation can be integrated using `LibreTranslate` for multilingual social media campaigns.

---

## 🛠️ Tech Stack

| Module | Library/Tool |
|--------|--------------|
| Frontend | Gradio |
| Image Captioning | BLIP (Salesforce/blip-image-captioning-base) |
| Text Generation | Phi-2 (microsoft/phi-2) |
| Text Enhancer | Custom logic + keyword matching |
| TTS/STT/Translation (Optional) | LibreTTS, Whisper, LibreTranslate |

---

## 📂 Project Structure

Caption_and_post_generator/
├── app.py # Gradio app with 3 tabs (Captioning, Enhancer, Post Generator)
├── caption.py # BLIP-based image captioning
├── generator.py # Phi-2 powered post generation
├── enhancer.py # Adds hashtags & emojis to captions
├── requirements.txt # Dependencies
├── pycache/ # Python cache
└── screenshots/ # Project screenshots for demo




