class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __str__(self):
        return f"(Name = {self.name}, SellIn = {self.sell_in}, Quality = {self.quality})"