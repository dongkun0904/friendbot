from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from trainset import conversations


class Friendbot():
    bot = None

    def __init__(self, name="friendbot"):
        # Create a friendbot
        Friendbot.bot = ChatBot(
            name,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///data/db.sqlite3',  # sqlite:// if you want in memory
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, I\'m not sure',
                    'maximum_similarity_threshold': 0.90
                }
            ]
        )
        self.name = name

    def train(self):
        trainer = ListTrainer(Friendbot.bot)

        for conversation in conversations:
            c = []
            for response in conversation:
                c.append(response.format(name=self.name))
            trainer.train(c)

    def getBotResponse(userResponse):
        botResponse = Friendbot.bot.get_response(userResponse)
        return botResponse
