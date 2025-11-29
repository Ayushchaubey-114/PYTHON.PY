import google.generativeai as genai
import google as genai
key = "AIzaSyAes0_YomBR_WuCG-WLIWxVfjQKSeAsL3g"
print(key)
genai.configure(api_key = key)
model= genai.GenerativeModel("gemini-1.5-flash")

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = model.generate_content(promt= user)
    print("AI: ", response.text)
