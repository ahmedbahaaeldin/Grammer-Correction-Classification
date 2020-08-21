import random
import nltk 
from nltk.corpus import wordnet 
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk import RegexpParser
from pattern.en import lexeme,pluralize,singularize,tenses
class HelperFunctions():
    def find_similar(self,word):
        synonyms = [] 
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas():
                if word != l.name():
                    synonyms.append(l.name()) 
        return synonyms
    
    def convert(self,word, from_pos, to_pos):
        WN_NOUN = 'n'
        WN_VERB = 'v'
        WN_ADJECTIVE = 'a'
        WN_ADJECTIVE_SATELLITE = 's'
        WN_ADVERB = 'r'
        synsets = wn.synsets(word, pos=from_pos)
        if not synsets:
            return []
        lemmas = []
        for s in synsets:
            for l in s.lemmas():
                if s.name().split('.')[1] == from_pos or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and s.name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                    lemmas += [l]
        derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]
        related_noun_lemmas = []

        for drf in derivationally_related_forms:
            for l in drf[1]:
                if l.synset().name().split('.')[1] == to_pos or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and l.synset().name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                    related_noun_lemmas += [l]
        words = [l.name() for l in related_noun_lemmas]
        len_words = len(words)
        result = [(w, float(words.count(w)) / len_words) for w in set(words)]
        result.sort(key=lambda w:-w[1])
        return result
    
    def UtilityCreation(self,sentence):
        alternative_word = ""
        pos_tags = self.POS(sentence)
        return alternative_word,pos_tags
    
    def ListPOS(self,List):
        tagged = pos_tag([i for i in List if i])
        return tagged
    
    def POS(self,text):
        split_text = text.split()
        return pos_tag(split_text)
    
    def get_conjugate(self,word):
        list_of_conjugates = lexeme(word)
        if word in list_of_conjugates:
            list_of_conjugates.remove(word)
        return list_of_conjugates
    
    def replace_word_in_sentence(self,target_word,fake_word,sentence):
        original_words = sentence.split()
        for i,word in enumerate(original_words):
            if word == target_word:
                original_words[i] = fake_word
        final_sentence = ' '.join(word for word in original_words) 
        return final_sentence
    
    def replace_tense(self,word,tense):
        TenseMapping = {'Cont':'VBG','Past':'VBD','Present':'VBP'}
        verb_forms = self.get_conjugate(word)
        target_tense = TenseMapping[tense]
        if len(verb_forms) > 0:
            different_tenses = self.ListPOS(verb_forms)
            for tense in different_tenses:
                if tense[1] == target_tense:
                    return tense[0]
        else:
            return None