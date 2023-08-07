# NLP Asset Analysis 📈

Stock & Crypto analysis made easy...

## Description

Rather than wasting time reading every single news article regarding each company in your portfolio, this project allows the user to create an automated email bot which will send them all the information they need. The bot will input the user's monitored tickers and then will output summaries of the 5 most recent news articles regarding each ticker and the news articles sentiment values. The user is also able to customize the frequency at which they wish to recieve updates regarding their portfolio.

### How It Works
* scrapes the web for relevant news links 🗞️
* cleans the links 🧼
* extracts the articles from each link 📰
* uses a pretrained financial NLP model to summarize each article 💸
* uses a sentiment analysis pipeline to analyze sentiment of each article 😄
* uses smtp and MIME to send completed analysis emails at a user specified frequency 📧

## Getting Started

* clone this github repo
* update the information in AssetEmail.py with an email you have access to (this will be used to send the summaries)
* run main.py

## Example

Below is an example output as a csv file ⬇️


![Screen Shot 2023-08-07 at 7 05 10 PM](https://github.com/8enji/nlp-asset-analysis/assets/58536087/97c3001e-df67-42db-a930-2a50e2ea270c)


Below is an example of a scheduled newsletter ⬇️


![Screen Shot 2023-08-07 at 7 07 42 PM](https://github.com/8enji/nlp-asset-analysis/assets/58536087/fa22e9fd-89d7-4efa-a3ac-7206438a9701)


