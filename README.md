# Trendyol Login Automation Project

 This project is a Python application that automates the login process on the Trendyol website using Selenium. The user provides their email and password, and the program attempts to log in to Trendyol. The result of the login attempt is displayed to the user.

## Features
- Pop-up Close: Automatically closes pop-up windows on the website.
- Automatic Login: Logs in to Trendyol using the email and password entered by the user.
- Success/Failure Check: Informs the user if the login was successful or if there was an error.
- Random Wait Time: Adds random delays to make the process less likely to be detected as a bot.

## Libraries Used

- `selenium`: Used for web browser automation.
- `random`: Used to create random wait times.
- `time`: Used for adding delays.

## Installation

1. Ensure Python 3 and pip are installed.
2. Install the necessary libraries: Run the following command in the project directory to install the required Python library:
   ```bash
   pip install -r requirements.txt

3.  Run the project with the following command:
   ```bash
    python main.py