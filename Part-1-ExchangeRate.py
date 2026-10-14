'''
Part-1-ExchangeRate.py
Assignment 1- Part 1- Exchange Rate Converter
Faiza Tasnim Khandaker
'''

import pandas as pd #using the pandas library to read the CSV file

class ExchangeRates: #creating a class called ExchangeRates 

    def __init__(self, BankOfCanadaExchangeRate): #defining the constructor for the class
        values = pd.read_csv(BankOfCanadaExchangeRate)
        self.exchange_rate = values["FXAUSDCAD"].iloc[-1]  #defining the exchange rate as the last value in the column

    def convert(self, amount, from_currency, to_currency): #creating a function to convert the amount from one currency to another

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.exchange_rate

        if from_currency == "CAD" and to_currency == "USD":
            return amount / self.exchange_rate

#assuming that users will provide legitimate input values (such as no $ or commas and only use uppercase USD/CAD) so no validation checks or invalid input messages are required.

calculator = ExchangeRates("BankOfCanadaExchangeRate.2026.csv") 

#prompting the user to enter the amount and the currencies to convert from and to

amount = float(input("Enter amount: ")) 
from_currency = input("Enter FROM currency (USD or CAD): ") 
to_currency = input("Enter TO currency (USD or CAD): ")
answer = calculator.convert(amount, from_currency, to_currency)

#formatting output rounding to 2 decimal places and printing the result based on the target currency

if to_currency == "CAD":
    print("${:,.2f} CAD".format(answer))
if to_currency == "USD":
    print("${:,.2f} USD".format(answer))
