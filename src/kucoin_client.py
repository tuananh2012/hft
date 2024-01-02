#  MarketData
from kucoin.client import Market
from kucoin.client import Trade
class KucoinClient:
    def __init__(self) -> None:
        self.client = Market(url='https://api.kucoin.com')

        self.api_key = '658d87419acf1d0001a46bdb'
        self.api_secret = '0db9eb4c-8cfc-4da6-acf2-624e6fa7f1c2'
        self.api_passphrase = 'Tuan2012@1204'
        self.trade = Trade(key=self.api_key, secret=self.api_secret, passphrase=self.api_passphrase)

    def get_sever_time(self):
        return self.client.get_server_timestamp()
    
    def get_bbo(self, symbol_str):
        temp = self.client.get_ticker(symbol_str)
        return {
            "bid_price": float(temp['bestBid']), "bid_size": float(temp['bestBidSize']),
            "ask_price": float(temp['bestAsk']), "ask_size": float(temp['bestAskSize'])
        }
    def get_bbo_with_fee(self, symbol_str):
        ans = self.get_bbo(symbol_str)
        commission = 0.2/100
        ans["bid_price"] *= (1 - commission)
        ans["ask_price"] *= (1 + commission)
        return ans
    
    def make_new_order(self, symbol_str, price, size, side):
        return self.trade.create_market_order(symbol_str, side, size, price)

        



