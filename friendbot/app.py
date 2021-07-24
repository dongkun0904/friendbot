from flask import Flask, request

from friendbot.friendbot import Friendbot

app = Flask(__name__)


# Create and train the friendbot
bot = Friendbot('Oppa')
bot.train()


@app.route('/friendbot', methods=['POST'])
def friendbot():
    data = request.json
    if 'userInput' in data:
        userInput = data['userInput']
        print('user: {}'.format(userInput))
        botResponse = Friendbot.getBotResponse(userInput)
        print('bot: {}'.format(botResponse))
        return botResponse.text, 200
    return 'Invalid data', 400


# if __name__ == '__main__':

#     app.run(host='0.0.0.0', port=105)
