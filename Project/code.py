import google.generativeai as genai
import pyttsx3

# Initialize text-to-speech engine

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 110)

genai.configure(api_key="AIzaSyAjEcwi56XsljMAMn-cHUvcdE1KBBWXNnk")

model = genai.GenerativeModel("gemini-2.5-flash")


user_input = input("Enter C language code: ")


prompt = f"""
You are a programming assistant.
Explain ONLY the following C language code.
If the input is not C language code, reply with:
"I only explain C language code."

C Code:
{user_input}
"""


response = model.generate_content(prompt)


print("\nExplanation:\n")
print(response.text)

# Speak response
engine.say(response.text)
engine.runAndWait()
