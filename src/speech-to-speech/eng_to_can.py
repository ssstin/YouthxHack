import speech_recognition as sr
import pyttsx3
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Load the M2M100 model and tokenizer for English to Chinese translation
translation_model_name = "facebook/m2m100_418M"
translation_tokenizer = M2M100Tokenizer.from_pretrained(translation_model_name)
translation_model = M2M100ForConditionalGeneration.from_pretrained(translation_model_name)

def initialize_speech_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speaking rate if needed
    voices = engine.getProperty('voices')

    # Print all available voices
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.name} - {voice.languages}")

    # Set a voice that supports Cantonese (zh_HK) or another Chinese language
    for voice in voices:
        if 'zh_HK' in voice.languages:  # Look for Cantonese (Hong Kong)
            engine.setProperty('voice', voice.id)
            print(f"Set voice to: {voice.name}")
            break
        elif 'zh_CN' in voice.languages:  # Fallback to Simplified Chinese if needed
            engine.setProperty('voice', voice.id)
            print(f"Set voice to: {voice.name}")
            break
    else:
        print("No suitable Cantonese voice found. Using default voice.")
    
    return engine

def SpeakText(command):
    """
    Function to convert text to speech.
    
    Args:
        command (str): The text to be spoken.
    """
    print(f"Speaking: {command}")  # Debugging line to check if function is called
    engine.say(command)
    engine.runAndWait()

def translate_english_to_cantonese_speech():
    """
    Function to recognize speech in English and translate it to Cantonese speech.
    """
    with sr.Microphone() as source:
        print("Listening in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        # Listen for the user's input
        audio = recognizer.listen(source)

        try:
            # Using Google Speech Recognition to recognize the audio in English
            recognized_text = recognizer.recognize_google(audio)
            print(f"Recognized Text (English): {recognized_text}")

            # Translate the English text to Cantonese using M2M100
            cantonese_translation = translate_text_with_m2m100(recognized_text, "en", "zh")

            print(f"Translated Text (Cantonese): {cantonese_translation}")
            
            # Speak out the Cantonese translation
            SpeakText(cantonese_translation)
        
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Unknown error occurred.")

def translate_text_with_m2m100(text, source_lang, target_lang):
    """
    Function to translate text using M2M100 model.
    
    Args:
        text (str): Text to be translated.
        source_lang (str): Source language code.
        target_lang (str): Target language code.
        
    Returns:
        str: Translated text.
    """
    # Set source and target languages for M2M100
    translation_tokenizer.src_lang = source_lang
    encoded_text = translation_tokenizer(text, return_tensors="pt")
    
    # Generate translation with forced BOS token for target language
    generated_tokens = translation_model.generate(**encoded_text, forced_bos_token_id=translation_tokenizer.get_lang_id(target_lang))
    translated_text = translation_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text