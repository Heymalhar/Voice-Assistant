from translate import Translator

def translate_text(dest_lang, src_lang, text):
    # Get user input for the source language and destination language
    # src_lang = input("Enter the source language (e.g., 'en' for English): ")
    # dest_lang = input("Enter the destination language (e.g., 'es' for Spanish): ")

    # Create a translator object
    translator = Translator(to_lang=dest_lang, from_lang=src_lang)

    # Get user input for the text to translate
    # text = input("Enter the text to translate: ")

    # Translate the text
    translated_text = translator.translate(text)

    # Display the translated text
    print(translated_text)

translate_text('es', 'en', 'hola')