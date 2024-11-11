# Requests vs Pycurl
When looking for python online data collection libraries (a.k.a. Scraping libraries) the main result is requests , however there is a much better library in my opinion called PyCurl, it is the python interface for libcurl which is basically the native library for curl . In this project I get immediately blocked when using requests, moreover the interesting part of the project is that we won't scrape an html code that we then have to parse with beautifulsoup, we will instead scrape data directly in a Json format. This gives us many advantages because Json is basically a dictionary that we can easily navigate, without need to learn a new library. Please have a look to this stackoverflow page if you are more interested in PyCurl vs Requests performances.

# Introduction
As Data Scientist we are probably used to query our data using SQL, I have noticed a very common problem in Junior but also Senior analytics professional, they think that a table in a database is at the very beginning of the process, this is because it is their process within a bigger one; sometimes it is just a matter of point of view, for a Data Engineer a table in a database is at the end of the process!

If we want to have a broader view we need to look out of the Analytics bubble, this is the reason why i started this project.

When scraping data, the most important part is the website structure analysis, in fact I have spent many hours navigating the website to get as much info as possible. I would like to guide you through some of the encountered problems.

# Javascript generated content
For complex websites you cannot directly scrape related HTML because most of the time there will be a JavaScript script generating informations. I have started considering Selenium to simulate a webdriver which would have fully loaded HTML info and then parse all this info with beautiful soup.

# Selenium
The first problem of vivino website using Selenium was to fully load the wine list scrolling to the bottom, this require a scroll call with selenium until the end is reached, however by using this strategy you have to perform multiple calls and there may be the risk of being banned.

# Find the most important JSON
When navigating the website I was not able to find a Json file with most of the info, this is because you get such file only after you start scrolling to the end of the first page. We now have a huge dictionary containing all details about a wine, even if some information in such dictionary are not displayed in the page you are looking.

# Tables that will be created from this code
- vintage (this is the main table)
- region_most_used_grapes
- flavor
  - flavor_primary_keywords
  - flavor_secondary_keywords
- prices
- food
- grapes
