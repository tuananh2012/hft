
from mexc_sdk import Spot
class MexcClient:
    def __init__(self) -> None:
        self.client = Spot(api_key='mx0vglLOyWo3w7WU2f', api_secret='d9b89cefde2d4136a32f404ddd20ebd8')
    def get_bbo(self, symbol_str):
        temp = self.client.depth(symbol=symbol_str, options={"limit": 5})
        return { "bid_price": float(temp['bids'][0][0]), "bid_size": float(temp['bids'][0][1]),
                "ask_price": float(temp['asks'][0][0]), "ask_size": float(temp['asks'][0][1])}
    def get_bbo_with_fee(self, symbol_str):
        return self.get_bbo(symbol_str)
    
    # def make_test_order(self, symbol_str):
    #    res = self.client.new_order_test(symbol=symbol_str, side="BUY", order_type="LIMIT", options={ "quantity": 5, "price": 100, "newClientOrderId": 123})
    #    print(res)
    #    res1 = self.client.open_orders(symbol=symbol_str)
    #    print(res1)
    def make_new_order(self, symbol_str, price, size, side):
        res = self.client.new_order(symbol = symbol_str, side = side, order_type = "LIMIT", options={"quantity": size, "price": price, "timeInForce": "IOC"})