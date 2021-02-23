"""
Bank ATM Machine Simulator with a account number and password.
"""

import sys
from PyQt5 import QtWidgets
from bankui import Ui_BankWindow


# Global Constants

INITIAL_VALUE = 0
EXPRESSION = " "


class BankWindow(QtWidgets.QMainWindow, Ui_BankWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(BankWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.all_buttons()
        self.enter_value = INITIAL_VALUE
        self.expression = EXPRESSION
        self.bank_account = BankAccount("Test Case", 0)
        self.display_brower.setText("Enter the correct account number and password to unlock the use of all "
                                    "buttons.\n \n \n \nSample Account \n \nAccount Number: 906548236457\nPassword: "
                                    "1234")

    def display_widget(self):
        self.display_brower.setText("Hey {}, this is your balance: {}".format(self.bank_account.owner, self.bank_account.balance))
        self.account_number.setText("")
        self.cash_number.setText("")

    def cash_deposit_value(self):

        if self.expression != " ":
            self.display_brower.setText("Deposited {} dollars into the account".format(self.expression))
            self.expression = int(self.expression)
            self.bank_account.deposit(self.expression)
            self.textBrowser.setText(" ")

        else:
            self.display_brower.setText("Please enter a value")

    def cash_withdraw_value(self):

        if self.expression != " ":

            self.expression = int(self.expression)

            if self.expression <= self.bank_account.balance:
                self.bank_account.withdraw(self.expression)
                self.textBrowser.setText(" ")
                self.display_brower.setText("Withdrew {} dollars into the account".format(self.expression))

            else:
                self.display_brower.setText("Not enough funds in the account!")

        else:
            self.display_brower.setText("Please enter a value")

    def cash_bal_value(self):
        self.display_brower.setText(str(self.bank_account.balance))
        self.expression = " "

    def account_get(self):
        self.actnum = self.account_number.text()
        self.passnum = self.cash_number.text()

        if self.actnum == "906548236457" and self.passnum == "1234":
            self.display_widget()
            self.unlocked_buttons()
        else:
            self.display_brower.setText("Please enter the correct account number and associated password!")

    def clear_text_nums(self):
        self.textBrowser.setText(" ")
        self.expression = " "

    def clicked_number_1(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "1")
        self.expression = self.expression + "1"

    def clicked_number_2(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "2")
        self.expression = self.expression + "2"

    def clicked_number_3(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "3")
        self.expression = self.expression + "3"

    def clicked_number_4(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "4")
        self.expression = self.expression + "4"

    def clicked_number_5(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "5")
        self.expression = self.expression + "5"

    def clicked_number_6(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "6")
        self.expression = self.expression + "6"

    def clicked_number_7(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "7")
        self.expression = self.expression + "7"

    def clicked_number_8(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "8")
        self.expression = self.expression + "8"

    def clicked_number_9(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "9")
        self.expression = self.expression + "9"

    def clicked_number_0(self):
        self.expression = str(self.expression)
        self.textBrowser.setText(self.expression + "0")
        self.expression = self.expression + "0"

    def exit_action(self):
        self.close()

    def all_buttons(self):

        self.submit_btn.clicked.connect(self.account_get)


    def unlocked_buttons(self):
        self.button_1.clicked.connect(self.clicked_number_1)
        self.button_2.clicked.connect(self.clicked_number_2)
        self.button_3.clicked.connect(self.clicked_number_3)
        self.button_4.clicked.connect(self.clicked_number_4)
        self.button_5.clicked.connect(self.clicked_number_5)
        self.button_6.clicked.connect(self.clicked_number_6)
        self.button_7.clicked.connect(self.clicked_number_7)
        self.button_8.clicked.connect(self.clicked_number_8)
        self.button_9.clicked.connect(self.clicked_number_9)
        self.button_0.clicked.connect(self.clicked_number_0)

        self.exit_btn.clicked.connect(self.exit_action)
        self.depo_btn.clicked.connect(self.cash_deposit_value)
        self.with_btn.clicked.connect(self.cash_withdraw_value)
        self.bal_btn.clicked.connect(self.cash_bal_value)
        self.enter_btn.clicked.connect(self.clear_text_nums)


class BankAccount(object):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_value):
        self.balance = self.balance + deposit_value

    def withdraw(self, amount):
        self.balance = self.balance - amount

        if self.balance < amount:
            print("Not Enough Funds")

    def __str__(self):
        return f"The owner is {self.owner} and the balance is {self.balance}"


app = QtWidgets.QApplication(sys.argv)

window = BankWindow()
window.show()
app.exec()
