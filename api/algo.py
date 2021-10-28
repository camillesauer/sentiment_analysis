import spacy
from spacytextblob import SpacyTextBlob
from pydantic import BaseModel

class SentimentQueryModel(BaseModel):
    text : str

class SentimentModel:
    @Language.spacytextblob
    def get_sentiment(self, text):
        nlp = spacy.load('en_core_web_sm')
        spacy_text_blob = SpacyTextBlob()
        nlp.add_pipe(spacy_text_blob)

        doc = nlp(text)

        polarity = doc._.sentiment.polarity
        subjectivity = doc._.sentiment.subjectivity

        return polarity, subjectivity