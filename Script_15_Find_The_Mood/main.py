# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

with AudioFile('src/chile.wav') as audio_file:
  audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)

print(text)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)

if scores['compound'] > 0:
  print('Positive Speech')
else:
  print('Negative Speech')
