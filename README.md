# 🤖 AUTO-REPLY-AI-CHATBOT 🚀  

An **automated AI chatbot** that uses **Google Gemini API** to **analyze chat history and generate smart replies**. It interacts with chat applications using **PyAutoGUI** and automates responses based on user input.  

---

## 📖 Table of Contents  
- [Introduction](#introduction)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Flow](#flow)  
- [Demo Video](#demo-video)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 📝 Introduction  
AUTO-REPLY-AI-CHATBOT is an **intelligent chatbot** that automates replies based on **Google Gemini AI**. It interacts with chat apps, reads the latest messages, and generates responses. Users can **approve, modify, or regenerate** replies before sending.  

---

## ✨ Features  
- 🤖 **AI-Powered Chatbot** – Uses **Google Gemini API** to generate intelligent responses.  
- 🔍 **Automated Message Selection** – Selects text from chat using **PyAutoGUI**.  
- ⏳ **User Confirmation** – Asks if the user wants to send the generated reply.  
- 🎭 **Customizable Responses** – Allows users to modify responses before sending.  
- 🔄 **Auto-Regeneration** – If a response is rejected, the user can suggest improvements.  
- 🖥️ **PyCharm Terminal Integration** – Displays copied chat history in **PyCharm terminal**.  
- 🔒 **Secure API Handling** – Uses **dotenv** to store API keys securely.  

---

## 🛠️ Tech Stack
- Python 3.8+
- Google Generative AI SDK
- PyAutoGUI
- Pyperclip
- python-dotenv

---

## 🛠️ Installation  

```bash
# Clone the Repository
git clone https://github.com/yourusername/AUTO-REPLY-AI-CHATBOT.git
cd AUTO-REPLY-AI-CHATBOT

# Install Dependencies
pip install pyautogui google-generativeai pyperclip python-dotenv

# Set Up Environment Variables
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

---

## 🚀 Usage  

```bash
# Run the chatbot script
python main.py
```

1. Copy the latest chat message
   - The script detects copied text and sends it to Google Gemini API.
2. AI generates a reply
   - The response appears in the terminal for approval.
3. Approve or modify response
   - Press Y to send, N to reject, or edit before sending.

---

## 🔄 Flow  
1. User copies a message from chat.
2. PyAutoGUI captures text and sends it to Google Gemini API.
3. AI generates a smart reply.
4. User reviews, edits, or approves the response.
5. Approved responses are automatically pasted in the chat box.

---

## 📹 Demo Video  
🔗 Watch the demo here (Add YouTube link when available)

---

## 🤝 Contributing  

```bash
# Fork the repository
git clone https://github.com/your-username/AUTO-REPLY-AI-CHATBOT.git

# Create a new branch for your feature
git checkout -b feature-name

# Make changes & commit
git commit -m "Added a new feature"

# Push changes to GitHub
git push origin feature-name
```