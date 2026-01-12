from google import genai
client = genai.Client(
    api_key="AIzaSyDsPQlG8NGVxcTUharI5MQYNf5yMr9dX0o"
)

print("Hi, my name is quickBot!! what's in your mind!!")

while True:
    user_input = input("👱You: ")

    if(user_input=="exit"):
        print("bye , nice talking to you!!")
        break;

    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input,
    )
    print("🤖chatBot: " ,response.text)
    print()




