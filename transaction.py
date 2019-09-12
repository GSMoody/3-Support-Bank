class Transaction:
    def __init__(self, date,acc_from,acc_to,narrative,amount):
        self.date = date
        self.from_account = acc_from
        self.to_account = acc_to
        self.narrative = narrative
        self.amount = amount

    def __repr__(self):
        return f"""********************************************
        Date: {self.date}
        From: {self.from_account}
        To: {self.to_account}
        Narrative: {self.narrative}
        Amount: £{self.amount}"""

class TransactionSum:
    def __init__(self, name, amount):
        self.name = name.upper()
        self.amount = amount

    def __repr__(self):
        return f"""********************************************
        Account holder {self.name} has a total balance of: £{self.amount}"""