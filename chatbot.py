from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create a new chatbot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus data
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Start chatting with the bot
if __name__ == "__main__":
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
