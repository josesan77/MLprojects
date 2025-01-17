# MLprojects - LLMs

## Large Language models for varied tasks

### Secret code
Deciphering a secret code from a text with a *secret key*, using grammatical similarity.

Python, Notebooks

HUN and ENG version

in folder `secretcode`

### Movie transcript sentiment-analysis
Sentiment analysis using *HuggingFace* pretrained `lvwerra/distillert-imdb` model, where data is loaded with `DistilBertTokenizer` tokenizer.

Videos (with available transcripts!) from YouTube are selected and the sentiment of the videos are analysed using the model.

In addition, a Google API CLient is used to get the video titles.

Note: Google API KEY is not included, you should (get one and) use your own!

in folder: 'movie_transcript_sentiment'