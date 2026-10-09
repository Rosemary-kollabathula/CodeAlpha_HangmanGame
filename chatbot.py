def chatbot():
print("Bot: Hello! Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message == "hello":
        print("Bot: Hi! How can I help you?")
    elif message == "how are you":
        print("Bot: I am fine, thank you!")
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")

chatbot()