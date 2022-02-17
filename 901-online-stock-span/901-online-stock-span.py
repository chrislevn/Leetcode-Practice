class StockSpanner:

    def __init__(self):
        self.list = []

    def next(self, price: int) -> int:
        res = 1
        while self.list and self.list[-1][0] <= price: 
            res += self.list.pop()[1]
        self.list.append([price, res])
        return res
    
    
    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)