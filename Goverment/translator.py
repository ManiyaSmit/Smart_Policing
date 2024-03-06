#from translate import Translator
from googletrans import Translator

def translate_text(text, source_language, target_language):
    target_lang_code = ''

    source_lang_code = ''
    if target_language == 'Hindi': target_lang_code = 'hi' 
    elif target_language == 'Bengali' : target_lang_code = 'bn'
    elif target_language == 'Telugu' : target_lang_code = 'te'
    elif target_language == 'Marathi' : target_lang_code = 'mr'
    elif target_language == 'Tamil' : target_lang_code = 'ta'
    elif target_language == 'Gujarati' : target_lang_code = 'gu'
    elif target_language == 'Kannada' : target_lang_code = 'kn'
    elif target_language == 'Punjabi' : target_lang_code = 'pa'
    elif target_language == 'Malayalam' : target_lang_code = 'ml'
    elif target_language == 'Urdu' : target_lang_code = 'ur'
    elif target_language == 'English' : target_lang_code = 'en'
    '''
    if source_language == 'Hindi': source_lang_code = 'hi' 
    elif source_language == 'Bengali' : source_lang_code = 'bn'
    elif source_language == 'Telugu' : source_lang_code = 'te'
    elif source_language == 'Marathi' : source_lang_code = 'mr'
    elif source_language == 'Tamil' : source_lang_code = 'ta'
    elif source_language == 'Gujarati' : source_lang_code = 'gu'
    elif source_language == 'Kannada' : source_lang_code = 'kn'
    elif source_language == 'Punjabi' : source_lang_code = 'pa'
    elif source_language == 'Malayalam' : source_lang_code = 'ml'
    elif source_language == 'Urdu' : source_lang_code = 'ur'
    '''
    translator = Translator()
    translated = translator.translate(text, src=source_language, dest=target_lang_code)
    return translated.text



'''

def translate_text(text, target_language):
    target_lang_code = ''
    if target_language == 'Hindi': target_lang_code = 'hi' 
    elif target_language == 'Bengali' : target_lang_code = 'bn'
    elif target_language == 'Telugu' : target_lang_code = 'te'
    elif target_language == 'Marathi' : target_lang_code = 'mr'
    elif target_language == 'Tamil' : target_lang_code = 'ta'
    elif target_language == 'Gujarati' : target_lang_code = 'gu'
    elif target_language == 'Kannada' : target_lang_code = 'kn'
    elif target_language == 'Punjabi' : target_lang_code = 'pa'
    elif target_language == 'Malayalam' : target_lang_code = 'ml'
    elif target_language == 'Urdu' : target_lang_code = 'ur'
    translator = Translator(to_lang=target_lang_code)
    translated_text = translator.translate(text)
    return translated_text

'''