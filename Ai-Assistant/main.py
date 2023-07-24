from ai_functions.core_ops import configure_engine, greet_user, take_user_input, goodbye, get_audio
from analyze_query import analyze_query
from variables import WAKEWORD



def winstonAi():

    configure_engine()

    while True:
        print("Listening")
        text = get_audio()

        if text.count(WAKEWORD) > 0:

            greet_user()

            query = take_user_input()

            analyze_query(query)

            goodbye()
