import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
sentence = "Vegtables are types of plants."

# Tokenazing sentences

sentence_tokens = nltk.word_tokenize(sentence)
# print(sentence_tokens)

pos_tags = nltk.pos_tag(sentence_tokens)
# print(pos_tags)

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    return sentence_lemmas

print(lemma_me('Vegtables are types of plants.'))