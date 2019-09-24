from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class QueryBroker:
    "This class runs the trainer and also passes the customer query in simple string format to the chat bot"
    
    bot = ChatBot(
        'Agent',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.SpecificResponseAdapter',
            'chatterbot.logic.UnitConversion',
            
        ],
        database_uri='mongodb://localhost:27017/chatterbot-databases'
    )
        
    def parseQuery(self,query_str):
        
        user_data = str(query_str)
        print("user_data =",user_data)
        while query_str != "Quit":
            try:
                bot_response = QueryBroker.bot.get_response(user_data)
                return bot_response.__str__()

            # Press ctrl-c or ctrl-d on the keyboard to exit
            except (KeyboardInterrupt, EOFError, SystemExit):
                br