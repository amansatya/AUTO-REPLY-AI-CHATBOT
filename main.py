import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_AI_BOT_KEY")
genai.configure(api_key=api_key)
def is_last_message_from_user(chat_log, user_name="SATYA AMAN"):
    messages = chat_log.strip().split("\n")
    if not messages:
        return False
    last_message = messages[-1]
    return user_name in last_message
time.sleep(2)
pyautogui.click(1389, 1043)
time.sleep(1)
pyautogui.moveTo(674, 227)
pyautogui.mouseDown()
pyautogui.moveTo(1719, 913, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.click(990, 1050)
time.sleep(1)
chat_history = pyperclip.paste()
print("Copied Text:", chat_history)
if is_last_message_from_user(chat_history, user_name="SATYA AMAN"):
    print("Last message was yours. No reply needed.")
else:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    while True:
        prompt = f"""
        You are Satya Aman, a professional coder from India. 
        You specialize in Python, C++, and AI/ML. You analyze chat conversations and provide coding-related insights, suggestions, and tech discussions.
        Here is the chat history:
        {chat_history}
        Now, generate a response in a natural, friendly, and technical tone.
        """
        response = model.generate_content(prompt)
        generated_response = response.text
        print("\nGenerated Response:", generated_response)
        user_input = input("\nDo you want to send this message? (y/n): ").strip().lower()
        if user_input == "y":
            break
        else:
            print("\nProvide a brief suggestion (max 30 words) for improving the message:")
            user_suggestion = input("Suggestion: ").strip()
            prompt = f"""
            You are Satya Aman, a professional coder from India.
            You analyze chat conversations and provide helpful insights.
            Here is the chat history:
            {chat_history}
            The user wants a refined response. Follow this additional suggestion:
            "{user_suggestion}"
            Now, generate a more refined response based on this input.
            """
            print("\nRegenerating response based on your suggestion...")
    pyautogui.click(1389, 1043)
    time.sleep(1)
    pyperclip.copy(generated_response)
    pyautogui.click(1225, 961)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')