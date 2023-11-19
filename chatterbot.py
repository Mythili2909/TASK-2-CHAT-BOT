# Define a dictionary of responses based on rules
responses = {
    "hello": "Hi there!",
    "how are you": "I'm good, thank you.",
    "what is your name": "I am a chatbot.",
    "bye": "Goodbye! Have a great day!",
    
}

# Function to get the response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that."

# Simulate a conversation with the chatbot
print("Chatbot: Hi! How can I help you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        bot_response = get_response(user_input)
        print(f"Chatbot: {bot_response}")
