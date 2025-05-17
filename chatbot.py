
def chatbot():
    print("Hi! I’m your farm assistant. Ask me about livestock status.")

    while True:
        query = input("You: ").lower()
        if "health" in query:
            print("Chatbot: The livestock are in healthy condition.")
        elif "temperature" in query:
            print("Chatbot: Current average temperature is 38.6°C.")
        elif "exit" in query:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn’t understand that.")

chatbot()
