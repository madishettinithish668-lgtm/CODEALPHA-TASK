def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm doing well, thank you! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "what is your name": "I'm your friendly chatbot!",
        "who created you": "I was created by a Python developer!",
        "what can you do": "I can chat with you and answer simple questions.",
        "thank you": "You're welcome!",
        "thanks": "Anytime!",
        "what is python": "Python is a popular programming language known for its simplicity.",
        "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "good morning": "Good morning! Hope you have a great day!",
        "good night": "Good night! Sleep well!"
    }
    normalized = user_input.strip().lower()
    for key in responses:
        if key in normalized:
            return responses[key]
    return "Sorry, I don't understand. Try asking something else."
def main():
    print("Chatbot is online! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower():
            break
if __name__ == "__main__":
    main()
