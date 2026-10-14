# FINE 3300 — Assignment 1: Exchange Rate Converter

**Student :** Faiza Tasnim Khandaker

## Project Overview

This project was completed for FINE 3300: Python for Finance Professionals course at Schulich School of Business. 
It involves developing a Python program to convert between US dollars (USD) and Canadian dollars (CAD) 
using annual exchange rate data provided by the Bank of Canada.
The assignment includes two separate implementations: 
a student written program (Part 1) and an independently AI generated program (Part 2). 

## Project Files
- **Part-1-ExchangeRate.py:** Student written program using pandas to read the CSV file and convert between USD and CAD.
- **ExchangeRatesAI.py:** AI generated version using Python's built in CSV module and decimal for currency calculations.
- **BankOfCanadaExchangeRate.2026.csv:** Bank of Canada exchange rate data given by the professor is used by both programs.

## Features
Both programs:
- Read the USD/CAD exchange rate from the supplied CSV file.
- Convert USD to CAD and CAD to USD.
- Prompt users to enter an amount and the from and to currencies.
- Display results with a dollar sign, currency identifier, and two decimal places.

## How to Run
1. Install Python 3. Part 1 also requires the pandas library.
2. Download and keep both Python files and the CSV file in the same folder.
3. Open the project folder in Visual Studio Code and run either Python file.
4. Enter the amount, the currency to convert from, and the currency to convert to when prompted.

## Example Results
Using the latest available exchange rate in the dataset (1 USD = 1.3978 CAD):
- **100,000 USD → 139,780.00 CAD**
- **100,000 CAD → 71,540.99 USD**

## AI Use
Part 1 contains the complete student written implementation. Part 2 was independently generated using AI model Claude Sonnet 5.5, without providing the student written code. The two implementations were tested successfully and compared as required by the assignment instructions. The comparison and AI prompts are written in detail in the assignment write up pdf submitted on canvas.
