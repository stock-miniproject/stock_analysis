# Stock_Analysis

This repository focuses on stock price prediction using machine learning algorithms. By creating a model from existing stock prices, the stock prices for a maximum of next 5 years are predicted. The libraries used are fbprophet, streamlit, yfinance, plotly and datetime.

The current stock prices are imported from yfinance( yahoo- finance) and fbprophet which is a facebook library. Make sure the correct version of python and numpy are installed to avoid any errors during installation. To predict from a given date till the number of years required, the datetime library is used.

The prediction is executed using streamlit which adds an essence to the project with its attractive features. Plotly library also used which enhances the project with its graphs.


Front end 
 
The home page has been developed using html and css, which contains details about the stock price and current trends.


Back end 
Create a request.py file using python to connect to the django server.
Then create the views.py file which imports the request file, and then mentions the name of the html file.
Create a directory called templates which contains the html file and other front end documents. The html file will have the button to execute the stock prediction python program.
The views.py will have the request to render the html file. This will put the output on the same page.
The urls.py will connect the views.py and the html file.
