class Dollar:
    # TODO Moneyの丸め処理どうする？
    # TODO hashCode()
    def __init__(self, amount):
        # TODO amount を privateにする
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, dollar):
        return self.amount == dollar.amount
