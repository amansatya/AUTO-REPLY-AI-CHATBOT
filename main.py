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

# Function to check if the last message is from "SATYA AMAN"
def is_last_message_from_user(chat_log, user_name="SATYA AMAN"):
    messages = chat_log.strip().split("\n")  # Split messages by newline
    if not messages:
        return False  # No messages, assume it's safe to reply

    last_message = messages[-1]  # Get the last message
    return user_name in last_message  # Check if "SATYA AMAN" is in the last message

# Small delay to switch to the target window
time.sleep(2)

# Step 1: Click on the chat icon at (1389,1043)
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

# Step 4: Click on PyCharm Terminal at (990,1050) to show copied text
pyautogui.click(990, 1050)
time.sleep(1)  # Wait for terminal focus

# Step 5: Retrieve copied text from clipboard
chat_history = pyperclip.paste()
print("Copied Text:", chat_history)  # Debugging

# Step 6: Check if the last message is from "SATYA AMAN"
if is_last_message_from_user(chat_history, user_name="SATYA AMAN"):
    print("Last message was yours. No reply needed.")
else:
    # Step 7: Generate a response, ask for approval, and send only if confirmed
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    while True:
        # Initial prompt
        prompt = f"""
        You are Satya Aman, a professional coder from India. 
        You specialize in Python, C++, and AI/ML. You analyze chat conversations and provide coding-related insights, suggestions, and tech discussions.
        Here is the chat history:

        {chat_history}

        Now, generate a response in a natural, friendly, and technical tone.
        """

        response = model.generate_content(prompt)
        generated_response = response.text  # Extract response text
        print("\nGenerated Response:", generated_response)  # Debugging

        # Step 8: Ask user for confirmation before sending
        user_input = input("\nDo you want to send this message? (y/n): ").strip().lower()

        if user_input == "y":
            break  # Exit loop if the user confirms
        else:
            # Ask for a 30-word suggestion if user rejects the response
            print("\nProvide a brief suggestion (max 30 words) for improving the message:")
            user_suggestion = input("Suggestion: ").strip()

            # Modify the prompt with the user's suggestion
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

    # Step 9: Switch back to chat by clicking the chat icon (1389,1043)
    pyautogui.click(1389, 1043)
    time.sleep(1)  # Ensure the chat app is focused

    # Step 10: Copy the approved response to clipboard
    pyperclip.copy(generated_response)

    # Step 11: Click at message box (1225, 961)
    pyautogui.click(1225, 961)
    time.sleep(1)  # Wait to ensure the click is registered

    # Step 12: Paste the text and send
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for paste to complete
    pyautogui.press('enter')  # Send the message