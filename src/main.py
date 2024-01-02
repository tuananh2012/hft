from kucoin_client import KucoinClient
from mexc_client import MexcClient
from lol import Notification
from position import PositionMananger
import time
cl1 = KucoinClient()
cl2 = MexcClient()
pairs = [["MYRO", "USDT"], ["ANALOS", "USDT"]]
noti = Notification()
noti.SetTarget("loiluxycr@gmail.com")
kucoin_pos = PositionMananger("kucoin_pos.txt")
mexc_pos = PositionMananger("mexc_pos.txt")

while True:
    for symbol in pairs:
        ins_kucoin = symbol[0] + "-" + symbol[1]
        ins_mexc = symbol[0] + symbol[1]
        bbo_kucoin = cl1.get_bbo_with_fee(ins_kucoin)
        bbo_mexc = cl2.get_bbo_with_fee(ins_mexc)
        if bbo_kucoin["bid_price"] > bbo_mexc["ask_price"]:
            message = "Gia dang ngon: {} kucoin bid: price {}, size {}; mexc ask: price {}, size {}".format(
                ins_kucoin, bbo_kucoin["bid_price"], bbo_kucoin["bid_size"], bbo_mexc["ask_price"], bbo_mexc["ask_size"])
            noti.SendEmail(message)
            print("kucoin", bbo_kucoin, "mexc:", bbo_mexc)
            # order_id = cl1.make_new_order(ins_kucoin, bbo_kucoin["bid_price"], bbo_kucoin["bid_size"], "sell")
            # cl2.make_new_order(ins_mexc, bbo_mexc["ask_price"], bbo_kucoin["ask_size"], "BUY")
            time.sleep(300)
        if bbo_kucoin["ask_price"] < bbo_mexc["bid_price"]:
            message = "Gia dang ngon: {} kucoin ask: price {}, size {}; mexc bid: price {}, size {}".format(
                ins_kucoin, bbo_kucoin["ask"], bbo_kucoin["ask_size"], bbo_mexc["bid_price"], bbo_mexc["bid_size"])
            noti.SendEmail(message)
            print("kucoin", bbo_kucoin, "mexc:", bbo_mexc)
            # order_id = cl1.make_new_order(ins_kucoin, bbo_kucoin["bid_price"], bbo_kucoin["bid_size"], "sell")
            # cl2.make_new_order(in


# cl2.make_test_order("MYROUSDT")


