from textblob import TextBlob

text = "amazing"
blob = TextBlob(text)

# Analyze sentiment polarity (-1 = negative, 1 = positive)
sentiment = blob.sentiment.polarity
print(f"Sentiment polarity: {sentiment}")