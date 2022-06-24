from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from Bank import Bank
import sys

class ATM(QDialog, Bank):
    def __init__(self, ):
        super(ATM, self).__init__()
        loadUi('C:/Users/User/Desktop/Inlab/ATM.ui', self)   

        self.loginbtn.clicked.connect(self.Login)
        self.logoutbtn.clicked.connect(self.Logout)
        self.balancebtn.clicked.connect(self.getBalance)
        self.withdrawbtn.clicked.connect(self.Withdraw)
        self.depositbtn.clicked.connect(self.Deposit)
        self.bank = Bank()
        self.account = None

        self.logoutbtn.setEnabled(False)
        self.withdrawbtn.setEnabled(False)
        self.balancebtn.setEnabled(False)
        self.depositbtn.setEnabled(False)
        self.amount.setEnabled(False)   

        


    def Login(self):
        name = self.name.text()
        pin = self.pin.text()
        self.account = self.bank.get(name, pin)

        if self.account:
            self.logoutbtn.setEnabled(True)
            self.withdrawbtn.setEnabled(True)
            self.balancebtn.setEnabled(True)
            self.depositbtn.setEnabled(True)
            self.amount.setEnabled(True) 
            self.loginbtn.setEnabled(False)
            self.name.setEnabled(False)
            self.pin.setEnabled(False)
            self.pin.clear()
            self.status.setText('Successfully Login')

        else:
            self.status.setText('Invalid name or pin')

    def Logout(self):
        self.accouunt = None
        self.name.clear()
        self.amount.clear()
        self.logoutbtn.setEnabled(False)
        self.withdrawbtn.setEnabled(False)
        self.balancebtn.setEnabled(False)
        self.depositbtn.setEnabled(False)
        self.amount.setEnabled(False)   
        self.loginbtn.setEnabled(True)
        self.name.setEnabled(True)
        self.pin.setEnabled(True)
        self.status.setText('Welcome!')

    def getBalance(self):
        balance = self.account.getBalance()
        self.status.setText(f'Balance: \n{balance}')

    def Withdraw(self):
        amount = self.amount.text()
        message = self.account.withdraw(float(amount))
        if message:
            self.status.setText(f'{message}')
        else:
            self.status.setText(f'Successfully withdrawn: \n{amount}')

    def Deposit(self):
        amount = self.amount.text()
        self.account.deposit(float(amount))
        balance = self.account.getBalance()
        self.status.setText(f'Successfully Deposit: \n{amount}\nCurrent balance: \n{balance}')




app = QApplication(sys.argv)
mainwindow = ATM()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(403)
widget.setFixedHeight(229)
widget.show()
app.exec_()


