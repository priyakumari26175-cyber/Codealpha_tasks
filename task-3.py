def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "what is your name":
        return "I am a simple Python chatbot."
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand."


print("🤖 Chatbot: Hello! Type something to chat.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    reply = chatbot(user_input)
    print("Chatbot:", reply)

    if user_input.lower() == "bye":
        break

    