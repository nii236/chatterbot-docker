import sys
from chatterbot import ChatBot

chatbot = ChatBot(
            'Ron Obvious',
                trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
                )

resp = chatbot.get_response("Hello, how are you today?")
print resp
