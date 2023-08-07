from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from bs4 import BeautifulSoup
import requests
import re
from transformers import pipeline
import csv

class AssetAnalysis:
    def __init__(self, tickers) -> None:
        # monitored tickers
        self.tickers = tickers

    # summarization Model
    model_name = 'human-centered-summarization/financial-summarization-pegasus'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)

    #Sentiment Analysis
    sentiment = pipeline('sentiment-analysis')

    # search for stock news
    def get_stock_news_urls(self, ticker):
        search_url = 'https://www.google.com/search?q=yahoo+finance+{}+news&tbm=nws'.format(ticker)
        r = requests.get(search_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        atags = soup.find_all('a')
        hrefs = [link['href'] for link in atags]
        return hrefs

    # filter urls
    def filter_urls(self, urls):
        exclude_list = ['maps', 'policies', 'preferences', 'accounts', 'support', 'search']
        val = []
        for url in urls:
            if 'https://' in url and 'finance' in url and not any(exclude_word in url for exclude_word in exclude_list):
                res = re.findall(r'(https?://\S+)', url)[0].split('&')[0]
                val.append(res)
        return list(set(val))[:5]


    # scrape urls
    def process(self, urls):
        articles = []
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = [paragraph.text for paragraph in paragraphs]
            words = ' '.join(text).split(' ')[:350]
            article = ' '.join(words)
            articles.append(article)
        return articles

    # summarize
    def summarize(self, articles):
        summaries = []
        for article in articles:
            input_ids = self.tokenizer.encode(article, return_tensors='pt')
            output  = self.model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
            summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            summaries.append(summary)
        return  summaries

    # exporting to CSV
    def create_output_array(self, summaries, scores, urls):
        output = [['Ticker', 'Summary', 'Label', 'Confidence', 'URL']]
        for ticker in self.tickers:
            for i in range(len(summaries[ticker])):
                output_this = [
                    ticker,
                    summaries[ticker][i],
                    scores[ticker][i]['label'],
                    scores[ticker][i]['score'],
                    urls[ticker][i]
                ]
                output.append(output_this)
        return output

    def export_csv(self):
        raw_urls = {ticker : self.get_stock_news_urls(ticker) for ticker in self.tickers}
        print('URLs fetched...')
        cleaned_urls = {ticker : self.filter_urls(raw_urls[ticker]) for ticker in self.tickers}
        print('URLs filtered...')
        articles = {ticker : self.process(cleaned_urls[ticker]) for ticker in self.tickers}
        print('Articles fetched...')
        summaries = {ticker : self.summarize(articles[ticker]) for ticker in self.tickers}
        print('Summaries complete...')
        scores = {ticker : self.sentiment(summaries[ticker]) for ticker in self.tickers}
        print('Sentiment computed...')
        output = self.create_output_array(summaries, scores, cleaned_urls)
        print('Outputing... \n')
        with open('summaries.csv', mode='w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerows(output)

