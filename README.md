# nlp asset analysis 📈

stock & crypto news analysis made easy...

## description

rather than wasting time reading every single news article regarding each company in your portfolio, this project allows the user to create an automated email bot which will send them all the information they need. the bot will input the user's monitored tickers and then will output summaries of the 5 most recent news articles regarding each ticker and the news articles sentiment values. the user is also able to customize the frequency at which they wish to recieve updates regarding their portfolio.

### how it works
* scrapes the web for relevant news links 🗞️
* cleans the links 🧼
* extracts the articles from each link 📰
* uses a pretrained financial NLP model to summarize each article 💸
* uses a sentiment analysis pipeline to analyze sentiment of each article 😄
* uses smtp and MIME to send completed analysis emails at a user specified frequency 📧

## getting started

* clone this github repo
* update the information in AssetEmail.py with an email you have access to (this will be used to send the summaries)
* run main.py

## example

below is an example output as a csv file ⬇️


![Screen Shot 2023-08-07 at 8 19 49 PM](https://github.com/8enji/nlp-asset-analysis/assets/58536087/dde99e37-6a14-4e09-9aa9-c1f4940df8bd)



below is an example of a scheduled newsletter ⬇️


![Screen Shot 2023-08-07 at 7 07 42 PM](https://github.com/8enji/nlp-asset-analysis/assets/58536087/fa22e9fd-89d7-4efa-a3ac-7206438a9701)


