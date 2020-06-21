---
title: "Ultimate exception handler"
date: 2016-02-25
permalink: /blog/2016/02/25/ultimate-exception-handler
tags:
  - python
---

So the last five minutes were spent on writing this simple python script that takes any exception as input and searches for a solution on Stack Overflow.

It was inspired by [this joke on reddit](https://www.reddit.com/r/ProgrammerHumor/comments/45oyre/the_ultimate_php_exception_handler).

Anyway, the code is very simple:

```python
import webbrowser

def handle(err, url='http://stackoverflow.com'):
    """Open browser and search for exception on StackOverflow"""
    err = str(err) # conver Exception object to string
    url += '/search?q=python+' + err.replace(' ', '+') # join search string
    webbrowser.open(url)
```

Now an exception can be treated like this:

```python
try:
    x = 1 / 0
except Exception as e: # note the Python 3 syntax
    handle(e)
```

The function will construct a search query string and open the resulting url in a new tab of the default browser.

This post was written as an Jupyter Notebook. You can view or download it using [nbviewer](http://nbviewer.ipython.org/github/dennissergeev/dennissergeev.github.io/blob/master/_blog/_notebooks/2016-02-25-ultimate-exception-handler.ipynb)
