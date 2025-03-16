import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_AI_BOT_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Small delay to switch to the target window
time.sleep(2)

# Step 1: Click on the icon at (1389,1043)
pyautogui.click(1389, 1043)
time.sleep(1)  # Wait for the window to open if needed

# Step 2: Click and drag to select text
pyautogui.moveTo(674, 227)
pyautogui.mouseDown()
pyautogui.moveTo(1719, 913, duration=0.5)  # Smooth drag
pyautogui.mouseUp()

time.sleep(0.5)  # Wait for selection to register

# Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Allow time for copying

# Step 4: Retrieve copied text from clipboard
chat_history = pyperclip.paste()
print("Copied Text:", chat_history)  # Debugging

# Step 5: Send chat history to Gemini API for response
model = genai.GenerativeModel("gemini-pro")
prompt = f"""
You are Satya Aman, a professional coder from India. 
You specialize in Python, C++, and AI/ML. You analyze chat conversations and provide coding-related insights, suggestions, and tech discussions.
Here is the chat history:

{chat_history}

Now, generate a response in a natural, friendly, and technical tone.
"""

response = model.generate_content(prompt)

generated_response = response.text  # Extract response text
print("Generated Response:", generated_response)  # Debugging

# Step 6: Copy the generated response to clipboard
pyperclip.copy(generated_response)

# Step 7: Click at coordinates (1623, 868)
pyautogui.click(1623, 868)
time.sleep(1)  # Wait to ensure the click is registered

# Step 8: Paste the text and send
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)  # Wait for paste to complete
pyautogui.press('enter')  # Send the message
