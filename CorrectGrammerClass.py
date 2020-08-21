from Grammer_Modification import HelperFunctions

class CorrectGrammerClass(HelperFunctions):
    def ReplaceAdverbSimilarMeaning(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'JJ':
                alternative_word = self.find_similar(word[0]) # choosing any random tense other than itself
                for w in alternative_word:
                    type_of_word = self.POS(w)
                    if type_of_word[0][1] == 'JJ':
                        alternative_word = type_of_word[0][0]
                        alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                        return sentence,alt_sent,word[0],alternative_word

                
    def ReplaceVerbSimilarMeaning(self,sentence):
        alt,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'VBP' or word[1] == 'VB':
                alternative_word = self.find_similar(word[0]) 
                for w in alternative_word:
                    type_of_word = self.POS(w)
                    if type_of_word[0][1] == 'VB' or type_of_word[0][1] == 'VBD':
                        alt = type_of_word[0][0]
                        break
                alt_sent = self.replace_word_in_sentence(word[0],alt,sentence)
                return sentence,alt_sent,word[0],alt

    
    def FromPresentToPast(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'VBP' or word[1] == 'VB':
                alternative_word = self.get_conjugate(word[0])
                if alternative_word == []:
                    return None
                if len(alternative_word) == 4:
                    alternative_word = alternative_word[-2]
                else:
                    alternative_word = alternative_word[-1]
                alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                return sentence,alt_sent,word[0],alternative_word

            
    def FromPastToPresent(self,sentence):
        alt_word,pos_tags = self.UtilityCreation(sentence)
        alt_list = None
        for word in pos_tags:
            if word[1] == 'VBD':
                alt_list = self.get_conjugate(word[0])
                if len(alt_list) > 1:
                    alt_word = alt_list[0]
                if alt_list == None:
                    return None
                alt_sent = self.replace_word_in_sentence(word[0],alt_word,sentence)
                return sentence,alt_sent,word[0],alt_word

    
    def SelfPrepositionToHe(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'PRP' and word[0]=="I":
                alternative_word = "He"
                alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                for second_level_words in pos_tags:
                    if second_level_words[1] == 'VBP':
                        alternative_word_2 = "is"
                        final_sent = self.replace_word_in_sentence(second_level_words[0],alternative_word_2,alt_sent)
                        return sentence,final_sent

    
    def HePrepositionToSelf(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'PRP' and word[0]=="He":
                alternative_word = "I"
                alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                for second_level_words in pos_tags:
                    if second_level_words[1] == 'VBZ':
                        alternative_word_2 = "am"
                        final_sent = self.replace_word_in_sentence(second_level_words[0],alternative_word_2,alt_sent)
                        return sentence,final_sent

    def ShePrepositionToSelf(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'PRP' and word[0]=="She":
                alternative_word = "I"
                alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                for second_level_words in pos_tags:
                    if second_level_words[1] == 'VBZ':
                        alternative_word_2 = "am"
                        final_sent = self.replace_word_in_sentence(second_level_words[0],alternative_word_2,alt_sent)
                        return sentence,final_sent
                    
    def SelfPrepositionToShe(self,sentence):
        alternative_word,pos_tags = self.UtilityCreation(sentence)
        for word in pos_tags:
            if word[1] == 'PRP' and word[0]=="I":
                alternative_word = "She"
                alt_sent = self.replace_word_in_sentence(word[0],alternative_word,sentence)
                for second_level_words in pos_tags:
                    if second_level_words[1] == 'VBP':
                        alternative_word_2 = "is"
                        final_sent = self.replace_word_in_sentence(second_level_words[0],alternative_word_2,alt_sent)
                        return sentence,final_sent
                    
