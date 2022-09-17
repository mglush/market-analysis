# Market Analysis.
## Data Mining, Dimensionality Reduction, and Markov Chains.
#### By Michael Glushchenko.

## Table of Contents
* [Purpose](https://github.com/mglush/market-analysis/blob/main/README.md#purpose)
* [Goals and Steps](https://github.com/mglush/market-analysis/blob/main/README.md#goals-and-steps)
* [Files](https://github.com/mglush/market-analysis/blob/main/README.md#files)
* [How to Run](https://github.com/mglush/market-analysis/blob/main/README.md#how-to-run)
* [Technologies](https://github.com/mglush/market-analysis/blob/main/README.md#technologies)
* [Sources](https://github.com/mglush/market-analysis/blob/main/README.md#sources)

## Purpose
The purpose of this project is to improve my data-science skills by mining financial data as well as applying certain machine learning techniques to it, and to improve my statistical skills by attempting to apply what I've learned in undergrad Statistics to a real-world (mostly chaotic and unsolvable) problem. Since the stock market problem is chaotic, the ultimate goal of this project is to find models that approximate the movement of some stocks with a 'decently-high' degree of success.

## Goals and Steps
1. Since TD Ameritrade only allows one to view the last 10 days of by-the-minute stock data, the first goal of this project is to create a routine that will aggregate said data to a local microSD card (so that there's a sufficient amount of data we can work on).
  a) A little side project will later involve creating a local mini server using a Raspberry Pi Pico that will automatically run the routine we wrote every 10 days (while perhaps performing other tasks while it waits).
2. Next, we will clean up the aggregated data so that it's ready to be worked on via different dimensionality reduction techniques (while UMAP is out first choice, we will also try out other approaches as time goes on).
3. We will then use the Uniform Manifold Approximation & Projection Algorithm (UMAP) to reduce the dimensionality of each pattern (from 1000 data points to a 2-dimensional point on a plane). We will try to do this for separate groups of stocks, as well as separate time-frames, one time-frame at a time. The goals for this step would be to determine acceptable parameters for the UMAP algorithm, to obtain clusters/piles of different patterns, to run k-means clustering on the resulting patterns, and to map the labelings of each of those clusters back to the original patterns.
4. Once patterns are successfully labeled and put into separate groups, multiple statistical approaches will be applied to determine whether any of them allow for a high degree of predictability of a stock's next pattern given it's current one. The approaches studied will include a simple Markov Chain using a frequency count of how often each pattern follows another in our data, a more complex subordinated Poisson Process approach to see if we can determine the specific times at which a given stock jumps to a new pattern (and if there are certain conditions that lead to a jump to a new pattern), and a Time-Series approach (where we will study the auto-correlation of each stock prior to breaking it into patterns).
5. It would be nice to eventtually provide an interface where some user can enter a stock symbol, and, as output, receive a chart of that stock, with the 3-5 most-likely paths moving forward (within the next couple minutes). We are doing this on a minute-by-minute basis so that the amount of extraneous variables is kept to a minimum.

## Files
While the files contain self-explanatory code, this section briefly summarizes the purpose of each file.
1. [data_mining/td_price_history.py](https://github.com/glush-n-charles/market-analysis/blob/main/data_mining/td_price_history.py)
* This class was written to interract with the TD Ameritrade API. It contains methods that could be helpful in pulling the price history of a single stock, a group of stocks given a list, or to pull the price history of all the stocks available on there (excluding small OTC symbols). This file should be used as an import, and was only directly run at the very beginning of this project in order to set up all the files.
2. [data_mining/parallel_gen_data.py](https://github.com/glush-n-charles/market-analysis/blob/main/data_mining/parallel_gen_data.py)
* This file uses the class mentioned above, and is directly run whenever one would like to update their file-system with any new data that might've been recorded by the TD Ameritrade API since the files were last interracted with.
3. [dim_reduction/utils.py](https://github.com/glush-n-charles/market-analysis/blob/main/dim_reduction/utils.py)
* This file provides functions used in the pre-processing part of the machine learning portion of this project (functions that clean up the data, smooth it out, etc.).
4. [dim_reduction/pre_processing.py](https://github.com/glush-n-charles/market-analysis/blob/main/dim_reduction/pre_processing.py)
* Using functions from utils.py, this file cleans up the data we have collected (mainly the minute data in the data/minute folder), breaks up each stock's chart into patterns of a pre-specified length, and saves those patterns in preparation for the dimensionality reduction portion of the project.
5. [dim_reduction/Umap.ipynb](https://github.com/glush-n-charles/market-analysis/blob/main/dim_reduction/Umap.ipynb)
* In this Jupyter Notebook, we test out some parameters of UMAP on a small amount of data to get a feel for how it works, whether it works at all, and to outline the approach that will be used for the large amount of data we have at hand.

## How to Run
Not ready to run.

## Technologies
* TD Ameritrade API.
* Yahoo Finance API.
* Python (libraries include *requests*, *json*, *ijson*, *datetime*, *pandas*, *umap*, *matplotlib*, *multiprocessing*).

## Sources
* [Umap How To](https://umap-learn.readthedocs.io/en/latest/index.html)
* [Yahoo Finance How To](https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b)

2022 &copy; Michael Glushchenko, Charles Delapa
