from Grammer_Modification import HelperFunctions
from pattern.en import lexeme,pluralize,singularize
class IncorrectGrammerClass(HelperFunctions):                                             
    def ReplaceTense(self,sentence,word,Tense_type):
        wrong_word = self.replace_tense(word,Tense_type) # choosing any random tense other than itself
        if wrong_word == None:
            return None
        wrong_sent = self.replace_word_in_sentence(word,wrong_word,sentence)
        return sentence,wrong_sent,word,wrong_word
    
    def ReplacePastTense(self,sentence,tense):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'VBD':
                return self.ReplaceTense(sentence,word[0],tense)

        
    def ReplaceContTense(self,sentence,tense):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'VBG':
                return self.ReplaceTense(sentence,word[0],tense)

    
    def ReplacePresentTense(self,sentence,tense):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'VBP':
                return self.ReplaceTense(sentence,word[0],tense)

    
    def ReplaceNounWithVerb(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
                if word[1] == 'NN':
                    wrong_word = self.convert(word[0],'n','v')
                    if wrong_word == []:       
                        return None
                    wrong_sent = self.replace_word_in_sentence(word[0],wrong_word[0][0],sentence)
                    return sentence,wrong_sent,word[0],wrong_word

    
    def RemovePreposition(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)  
        for word in pos_tags:
            if word[1] == 'IN':
                wrong_word = ""
                wrong_sent = self.replace_word_in_sentence(word[0],wrong_word,sentence)
                return sentence,wrong_sent,word[0],alternative_word
    
    def ReplacePreposition(self,sentence):
        TargetFirstPrepositonsWrongMappings = {'to':'with','with':'to','behind':'inside','for':'from','in':'at','on':'by'
                                                    ,'since':'from','of':'for','against':'for','about':'with','by':'in',
                                                    'through':'from','from':'to','at':'of'}
        alternative_word,pos_tags = self.UtilityCreation(sentence)  
        for word in pos_tags:
            if word[1] == 'IN' and word[0] in TargetFirstPrepositonsWrongMappings.keys():
                wrong_word = TargetFirstPrepositonsWrongMappings[word[0]]
                wrong_sent = self.replace_word_in_sentence(word[0],wrong_word,sentence)
                return sentence,wrong_sent,word[0],wrong_word
            
    def RemoveDTa(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)  
        for word in pos_tags:
            if word[1] == 'DT' and word[0] == 'a':
                wrong_word = ""
                wrong_sent = self.replace_word_in_sentence(word[0],wrong_word,sentence)
                return sentence,wrong_sent,word[0],alternative_word

    
    def Singularize(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'NNS':
                wrong_word = singularize(word[0])
                wrong_sent = self.replace_word_in_sentence(word[0],wrong_word,sentence)
                return sentence,wrong_sent,word[0],wrong_word

    def Pluralize(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'NN':
                wrong_word = pluralize(word[0])
                wrong_sent = self.replace_word_in_sentence(word[0],wrong_word,sentence)
                return sentence,wrong_sent,word[0],wrong_word  
