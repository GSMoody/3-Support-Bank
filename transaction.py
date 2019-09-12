class Transaction:
    def __init__(self, row):
        self.date = row[0]
        self.from_account = row[1]
        self.to_account = row[2]
        self.narrative = row[3]
        self.amount = int(row[4])

    def display(self):
        print(f"{self.date}: {self.from_account}")
