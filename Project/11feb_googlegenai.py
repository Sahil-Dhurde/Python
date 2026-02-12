import google.generativeai as genai
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 110)     # setting up new voice rate
a=input('Enter a question:')
genai.configure(api_key='AIzaSyCcCvrP4DinVFcW0_CKu1OKZWRaXRCsot4')
model=genai.GenerativeModel('gemini-2.5-flash')
response=model.generate_content(a)
print(response.text)
engine.say(response.text)
engine.runAndWait()
