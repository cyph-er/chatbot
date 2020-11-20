from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])


corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')



small_talk=['hi there!',
            'hi!','how do you do?','how are you?','i\'m cool','fine, you?',
            'always cool','i\'m okay','glad to hear that.','i\'m fine','glad to hear that','i feel awesome','excellent, glad to hear that.','i feel awesome','excellent, glad to hear that.','not so good','sorry to hear that.','what\'s your name?','i\'m Jacob. ask me anything please.']


math_talk_1 = ['pythagorean theorem','a squared plus b squared equals c swuared']

math_talk_2 = ['law of cosines', 'c**2=a**2+b**2 -2*a*b*cos(gamme)']

list_trainer = ListTrainer(my_bot)
for item in (small_talk,math_talk_1,math_talk_2):
    list_trainer.train(item)

print(my_bot.get_response("hey jarvis"))

