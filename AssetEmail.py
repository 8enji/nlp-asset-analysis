from AssetAnalysis import AssetAnalysis
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import time

class AssetEmail:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sender = 'nlp.asset.analysis@gmail.com'
    server.login(sender, 'altkbmizwthslytd')

    def get_tickers(self):
        cont = True
        tickers = []
        while cont:
            add_ticker = input('Would you like to add a ticker to your watchlist [yes/no]: ')
            if add_ticker == 'yes':
                ticker = input('Enter ticker: ')
                tickers.append(ticker.upper())
            else:
                cont = False
        return tickers
    
    def get_frequency(self):
        frequency = ''
        while type(frequency) is not int:
            frequency = input('How often (in hours) would you like to recieve updates?: ')
            try:
                frequency = eval(frequency)
            except:
                frequency = ''
        return frequency

    def get_analysis(self, tickers):
        analysis = AssetAnalysis(tickers)
        analysis.export_csv()

    def send_email(self, email):
        msg = MIMEMultipart()
        body_part = MIMEText('Hello, \n\nHere is your newsletter!\n\nEnjoy,\nAsset Analysis Team', 'plain')
        msg['from'] = self.sender
        msg['to'] = email
        msg['subject'] = 'Asset Analysis Newsletter'
        msg.attach(body_part)

        with open('summaries.csv', 'rb') as file:
            msg.attach(MIMEApplication(file.read(), Name='summaries.csv'))

        self.server.sendmail(msg['From'], msg['To'], msg.as_string())

    def start_email_loop(self):
        print()
        tickers = self.get_tickers()
        email = input('What is your email?: ')
        frequency = self.get_frequency()
        print()

        while True:
            time.sleep(frequency * 3600)
            try:
                self.get_analysis(tickers)
                self.send_email(email)

            except KeyboardInterrupt:
                self.server.quit()
                break
            except:
                print('Error occured')
                self.server.quit()
                break
        


    