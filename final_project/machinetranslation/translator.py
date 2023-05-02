"""module imports"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-02',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
        translates english to french
    """
    french_text = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text


def french_to_english(french_text):
    """
        translates french to english
    """
    english_text = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text
