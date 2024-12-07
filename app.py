from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# The SQLStorageAdapter is ChatterBot’s default adapter.
#  If you do not specify an adapter in your constructor,
#  the SQLStorageAdapter adapter will be used automatically.

medical_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
                    logic_adapters=["chatterbot.logic.BestMatch"]) ,database_uri='sqlite:///database.sqlite3'
#  ,preprocessors=['chatterbot.preprocessors.clean_whitespace']


    # logic_adapters=[
    #     {
    #         "import_path": "chatterbot.logic.BestMatch",
    #         "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
    #         "response_selection_method": chatterbot.response_selection.get_first_response
    #     }
    # ]


# https://chatterbot.readthedocs.io/en/stable/logic/response_selection.html
# https://chatterbot.readthedocs.io/en/stable/storage/text-search.html
# https://chatterbot.readthedocs.io/en/stable/conversations.html
# https://chatterbot.readthedocs.io/en/stable/corpus.html
# https://chatterbot.readthedocs.io/en/stable/django/wsgi.html

#trainer = ChatterBotCorpusTrainer(medical_bot)
#trainer = ListTrainer(medical_bot)
#trainer.train("med_conversations")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(medical_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
