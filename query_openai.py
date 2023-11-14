import openai
import os

openai.api_key = "Deine API key"

class chatbot():
    def __init__(self):
        self._viewers = {}

    def new_chat(self, username:str, message:str):
        if username not in self._viewers.keys():   
            self._viewers[username] = [
                {"role": "system", "content": "Du bist ein witziger twitch.com-Bot, der nicht zu unhöflich ist. Beantworte die folgende Konversation unter Berücksichtigung früherer Antworten mit einer Klartextausgabe. Fügen Sie Twitch-kompatible Emotes oder Emote-Strings ein. Ihr Name ist {username}.  Antworte auf Deutsch."},
                {"role": "user", "content": message}
            ]   
        else:
            
            self._viewers[username].append({"role": "user", "content": message})
        chatbot_response = self._get_response(username)
        self._viewers[username].append(chatbot_response)
        return chatbot_response
                 
    def _get_response(self, username:str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self._viewers[username]
        )

        # Print the response and add it to the messages list
        chat_message = response['choices'][0]['message']['content']
        self._viewers[username].append({"role": "assistant", "content": chat_message})
        return(chat_message)

if __name__ == "__main__":
    chatbot()