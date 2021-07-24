import sys

from chatterbot import ChatBot

from friendbot.friendbot import Friendbot
# from friendbot.gui import createChattingWindow


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please pass the name of the friendbot")
        exit()

    name = sys.argv[1]

    # Create a friendbot
    friendbot = Friendbot(name)

    # Train the friendbot
    friendbot.train()

    # Run the friendbot
    print("Say hello to the bot!")
    while True:
        try:
            userResponse = input("You: ")

            botResponse = Friendbot.getBotResponse(userResponse)
            print("Bot: {}".format(botResponse))

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
