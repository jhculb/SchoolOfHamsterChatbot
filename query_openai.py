import openai
import os
import pandas

openai.api_key = "Deine API Key"

input_sentences = pandas.read_csv("examples.csv", delimiter=",", header=None)
print(input_sentences[0])
responses = []
for line in input_sentences[0]:
    print(line)
    messages = [{"role": "system", "content": "Du bist ein witziger twitch.com-Bot, der nicht zu unhöflich ist. Beantworte die folgende Konversation unter Berücksichtigung früherer Antworten mit einer Klartextausgabe. Fügen Sie Twitch-kompatible Emotes oder Emote-Strings ein. Antworte auf Deutsch."},
                {"role": "user", "content": line}
        ]    
    print(messages, flush=True)
    responses.append(openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    ))
pandas.DataFrame(responses).to_csv("responses.csv")