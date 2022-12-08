# FE_All_in_one
A Generalized Repo for experimenting with Financial Engineering

"Long way to go, and big ideas yet to discover. We will stumble along the way, and learn a lot from contact with reality of market data.

It will somtimes be messy, and we will be forced to scrub. We will sometimes make really bad dcisions and end up with tons load of meaningless data, we will sometimes have moments of transcentdent progress and value" In all, we will create a tool likely to help us understand financial markets and data better.


Here are the following questions we like to answer regarding this repo

1. Use MAPE to predict trends - 24 hrs, 7 days, and 30 days
2. Obtain resistance and support levels for each the period
3. Obtain Stock trend - Bearish or Bullish for each of the period

So what I still have in mind is to abstract different levels right. the lowest level is the data sources. Right now there's only a stock price from yfinance. but soon we'd have stochastic data, fed data, crypto, and others. Then coming to the next abstraction block are signals from the data, some of which you mentioned. I think we would need to have basic technical indicators like RSI, MACD, OCV, stochastic oscillator, Kalman Filter instead of MA for sure, MAPE (whatever we deem good). Each of these signals generator can be a function and we parameterize the arguments such as window, timeframe, and all. We can experiment with multiple timeframes and see what comes out of them. 

For the MAPE, we have a function that takes the window and returns the MAPE signal. 

So the next block can be stats like correlation, and volatility(std)
But also on another note, these signals can be used as training features for whatever models we want to train. 

Still have thoughts on topics like portfolio management, and risk management. 

The other thing I'd say that I think is more fun for us right now is I came across this paper titled 151 trading strategies and if possible, I'd want us to make this a building block too. Imagine having a pipeline that by giving data we are able to efficiently evaluate these results to see if there are any signals or not. https://deanstreetlab.github.io/papers/papers/Systematic%20Trading/151%20Trading%20Strategies.pdf. 

If these are ways people have been using to find alphas, maybe we can train models optimized for this or look at correlations between these alpha signals too? 

@Siddesh
It's still too early to talk about lots of things. I want us to build from the ground up to understand what's in the industry today and where can we learn to have an edge.

The only philosophy I have is to go bottom-up and understand where we can have an edge. I think for that we need to know what state of the art and what's being researched and deployed at the moment

@James
Have also been thinking about applying Game Theory to Trading, but want to take it a step at a time - like optimizing strategies to maximize against expected competing interests and goals.

@Siddesh
Somewhere down the line, ill start a conversation in Deep Learning -> Reinforcement L. Deep Reinforcement L -> Liquid L too. but that will come later.