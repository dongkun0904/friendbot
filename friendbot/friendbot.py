def startFriendbot(bot):
    print("Say hello to the bot!")
    while True:
        try:
            userResponse = input("You: ")

            botResponse = bot.get_response(userResponse)
            print("Bot: {}".format(botResponse))

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
