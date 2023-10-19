from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

# Get Configuration Settings
load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')

# Configure speech service
speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
# print('Ready to use speech service in:', speech_config.region)

def Transcribe():
    command = ''

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(filename="station (1).wav")
    # audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        # print(command)
    else:
        
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command