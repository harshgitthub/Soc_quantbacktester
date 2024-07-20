soc_quantbacktester
Welcome to the Beautiful Mess of Stock Analysis
Thanks for stumbling on my project of financial backtesting and machine learning (well, sort of). This project combines a Flask backend and a React frontend in a way that might just make you question your life choices. Let’s dive into the chaos:

How to Start (Because You Have to)
Pull the Latest Code:


git pull


Backend (soc_backend):
Navigate to the soc_backend directory and run:
python main.py  # Or just `flask run` if you're feeling fancy


Frontend (soc_frontend):
Navigate to soc_frontend > myapp and start:
npm start
What’s Actually Working
Show Data Page:
Input your stock ticker (in the prestigious .NS /.BO format) and watch the magic unfold. Click on the stock or nifty to see tables and celebrate their cumulative returns. If you’re lucky, you’ll also get a comparison of their returns and some thrilling plots of stock prices.

Strategy Page:
Apologies in advance—this is still a work in progress. You’ll see a basic strategy that tells you whether to buy (1) or sell (-1). Treat it like a weather forecast from the 90s—vaguely interesting but not to be relied upon for your next million-dollar decision.

Post-Trade Page:
Here’s where we get all “serious” with RSI, Sharpe ratios, and other fancy metrics. Expect tables with monthly returns and plots that might actually make you look like you know what you’re doing. If you only see a few rows, don’t panic; it’s just how months work.

Guess Page:
Prepare yourself for an aesthetically questionable design and a page that runs slower than a snail on vacation. This page provides a JSON of the next 10 days of prices. It’s not fast, but it’s a glimpse into the future!

Notes (Because I Care)
Glitches:
I’ve tested this , but if you encounter glitches, remember: I’m working on it.
Increase the date range (preferably in years) if you’re not seeing results.

Design:
Apologies for the design. I’m currently honing my design skills in a parallel universe where I’m also a artist . 

Enjoy exploring this rollercoaster of a project, and remember, investing in stocks might be more predictable than this code.