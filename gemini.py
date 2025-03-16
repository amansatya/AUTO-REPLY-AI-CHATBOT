import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_AI_BOT_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

command = '''
[12:59 AM, 3/15/2025] Me: Ok bro
[12:59 AM, 3/15/2025] GKD: Or kya kr rha h?
[1:00 AM, 3/15/2025] Me: Lab file likh raha hu
[1:00 AM, 3/15/2025] GKD: Dbms?
[1:00 AM, 3/15/2025] Me: Nahi iiot
[1:00 AM, 3/15/2025] GKD: Achha achha
[1:00 AM, 3/15/2025] GKD: Thik h likh le
[1:00 AM, 3/15/2025] GKD: Milte h kl
[1:00 AM, 3/15/2025] Me: Haa bro done
[1:01 AM, 3/15/2025] GKD: Hn
[1:01 AM, 3/15/2025] GKD: Byee..gud nyt
[1:01 AM, 3/15/2025] Me: Good night
[10:10 PM, 3/15/2025] Me: grp leader kaun hai apna
[2:39 PM, 3/16/2025] GKD: Koi assignment wagerah mila h kya?
[2:59 PM, 3/16/2025] Me: Nahi
'''

# Create a Gemini model instance
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Generate a response based on chat history
response = model.generate_content(f"""
You are 'Me' in this chat, a student discussing assignments, lab work, and general topics with a friend named 'GKD'. 
Analyze the chat history and generate a natural response that fits the ongoing conversation.

Here is the chat history:
{command}

Now generate a response in a natural, friendly, and conversational tone.
""")

# Print the response from Gemini
print(response.text)
