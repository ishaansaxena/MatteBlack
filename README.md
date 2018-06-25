# MatteBlack
A Django-based stock analysis tool using the Python AlphaVantage API Wrapper.

Resource guide:
1. AlphaVantage.co - [Documentation](https://www.alphavantage.co/documentation/)
1. AlphaVantage API Python Wrapper - [Github](https://github.com/RomelTorres/alpha_vantage)
1. Plotly.js - [Documentation](https://plot.ly/javascript/)

This proejct:
1. Code on [Github](https://github.com/ishaansaxena/AlphaVantage)
1. Build on [Heroku](https://matteblack.herokuapp.com)

To-do:
1. Find ways to get company information (name, sector, etc) dynamically from the stock ticker
    1. Update secwiki?
1. Find ways to get company market cap
1. Find ways to get stock % fall/rise
1. Create dashboard page:
    1. User tracked symbols (watchlist)
    1. Popular symbols
    1. Tickers and time series from tracked symbols
1. Create user model extending Django's model
    1. Allow Google Sign-in
    1. Send confirmation email (necessary?)
    1. Restrict registration (for now)
    1. Require sign-in for dashboard etc.
1. Change @login_required to @permission_required
