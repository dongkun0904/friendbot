import sys

from chatterbot import ChatBot

from friendbot.friendbot import startFriendbot
from friendbot.train import train

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please pass the name of the friendbot")
        exit()

    name = sys.argv[1]

    # Create a friendbot
    friendbot = ChatBot(
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

    # Train the friendbot
    train(friendbot)

    # Run the friendbot
    startFriendbot(friendbot)
