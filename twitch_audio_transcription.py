import requests
import irc.bot
from pymongo import MongoClient
from datetime import datetime
from google.cloud import speech
import io

# Replace these with your actual credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
BOT_TOKEN = 'your_bot_oauth_token'
BOT_NICK = 'your_bot_nickname'
CHANNEL = '#your_channel_name'

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['twitch_data']
streams_collection = db['streams']

class TwitchChatBot(irc.bot.SingleServerIRCBot):
    def __init__(self, token, nickname, channel):
        server = 'irc.chat.twitch.tv'
        port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        message = e.arguments[0]
        username = e.source.split('!')[0]
        print(f"{username}: {message}")
        # Store the comment in MongoDB
        streams_collection.update_one(
            {'channel': self.channel},
            {'$push': {'comments': {'time': datetime.now(), 'user': username, 'message': message}}}
        )

def transcribe_audio(file_path):
    client = speech.SpeechClient()

    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.AAC,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)

    return transcriptions

def store_transcriptions(transcriptions, channel):
    streams_collection.update_one(
        {'channel': channel},
        {'$set': {'transcription': {'time': datetime.now(), 'text': transcriptions}}}
    )

def main():
    bot = TwitchChatBot(BOT_TOKEN, BOT_NICK, CHANNEL)
    bot.start()

if __name__ == "__main__":
    main()
