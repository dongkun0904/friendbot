from chatterbot.trainers import ListTrainer


def train(friendbot):
    conversations = [
        [
            "Hi",
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ], [
            "What is your name?",
            "I am {}!".format(friendbot.name),
            "I miss you.",
            "I miss you a lot..."
        ], [
            "Who are you?",
            "I am {}!".format(friendbot.name)
        ], [
            "Who is this",
            "I am {}!".format(friendbot.name)
        ]
    ]

    trainer = ListTrainer(friendbot)

    for c in conversations:
        trainer.train(c)
