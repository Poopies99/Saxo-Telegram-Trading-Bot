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

# Features

Menu can be accessed by sending any message or simply starting the bot

<img src="https://user-images.githubusercontent.com/69495787/184651858-e76724fc-1975-4559-b4f8-0986f730d586.PNG" width="250">

1. View your Open Positions

<img src="https://user-images.githubusercontent.com/69495787/184652935-6ef37cff-7b75-491a-aa7e-dfb949815d32.PNG" width="250">

2. View your Account Balance

<img src="https://user-images.githubusercontent.com/69495787/184653440-e58bc430-0d05-44b7-b0c8-3a9b21fee124.PNG" width="250">

3. View your Price Alerts

<img src="https://user-images.githubusercontent.com/69495787/184653615-6365d408-0623-4eb4-80ae-e9b7b4ea1842.png" width="250">

4. Create an Order

<img src="https://user-images.githubusercontent.com/69495787/184653862-46833254-c441-4598-8a67-58c8f72f0a32.PNG" width="250">

Select the order details step by step

## Future Implementations
Machine Learning for Responses
Logging through AWS CloudWatch
Event Driven Cloud Approach
