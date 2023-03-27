import pandas as pd
import spacy
from spellchecker import SpellChecker

class BadwordsFilter():
    def __init__(self, language, list_badwords, censor_text='*****') -> None:
        self.language = language
        self.list_badwords = list_badwords
        self.censor_text = censor_text
        self.spell_checker = SpellChecker(language=self.language)
        self.nlp = spacy.blank('en')
        pass

    def replace_token(self, text: str, old: str, new: str, error: int = 0) -> str:
        index = old.idx + error
        return text[:index] + new + text[index + len(old.text):]

    def difference_token_lenght(self, new, old):
        return len(new) - len(old)

    def is_badword(self, word):
        return word.lower() in self.list_badwords
    
    def censor(self, text):
        doc = self.nlp(text)
        error = 0
        for token in doc:
            candidates = self.spell_checker.candidates(token.text)
            for candidate in candidates:
                if self.is_badword(candidate):
                    text = self.replace_token(text, old=token, new=self.censor_text, error=error)
                    error += self.difference_token_lenght(token.text, self.censor_text)
        return text
    
    def add_word(self, word, frequency=100):
        self.spell_checker.word_frequency.add(word)
        self.spell_checker.word_frequency.dictionary[word] = frequency
        return None

    def export_vocabulary(self, path='./vocabulary.json'):
        self.spell_checker.export(path, gzipped=False)
        return None
    
    def import_vocabulary(self, path):
        self.spell_checker.word_frequency.load_dictionary(path)
        return None