from Savingsaccount import SavingsAccount
import pickle

class Bank(object):
    def __init__(self, fileName = 'accounts.txt'):
        self.accounts = {}
        self.fileName = fileName

        if fileName != None:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break

    def __str__(self) :
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        return name + "/" + pin
    
    def add(self, account):
        key = self.makeKey(account.getName(),
        account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def save(self, fileName = None):

        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return

        fileObj = open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

bank = Bank()
print(bank) #for testting purposes
