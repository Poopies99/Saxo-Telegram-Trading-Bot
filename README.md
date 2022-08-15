# Saxo-Telegram-Trading-Bot
Have direct access to your Saxo Trading Account through Telegram. Receive Alerts and Create Orders, View Balances, Alerts and Positions directly from the Telegram

# High Level Diagram

![alt text](https://user-images.githubusercontent.com/69495787/184612855-d9fec1ce-6e33-4041-ac68-d3c070847d92.png)

1. User input on Telegram sends get request via AWS API Gateway to access Lambda function
2. Lambda function sends get request to Saxo to process request
3. Result is sent back to User through Telegram

# How to use

1. Clone this repository
2. Use command python3 main.py inside the folder directory
3. Try the App [here](https://web.telegram.org/z/#5456469961)

## Future Implementations
Machine Learning for Responses
Logging through AWS CloudWatch
Event Driven Cloud Approach
