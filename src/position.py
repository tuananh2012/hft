class PositionMananger:
    def __init__(self, path):
        f = open(path,'r')
        self.position = {}
        for line in f.readlines():
            pos = line.split()
            self.position[pos[1]] = float[pos[2]]
    def GetPos(self, coin):
        if coin in self.position:
            return self.position[coin]
        else:
            return 0
    def OnExecution(self, base_coin, quote_coin, price_after_fee, size):
        if base_coin not in self.position:
            self.position[base_coin] = 0.0
        if quote_coin not in self.position:
            self.position[quote_coin] = 0.0
        self.position[base_coin] += size
        self.position[quote_coin] += size * price_after_fee