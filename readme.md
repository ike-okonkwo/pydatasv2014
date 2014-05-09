# Data Engineering 101: Building your first data product

_Delivered May 4th, 2014 at [PyData SV](http://pydata.org/sv2014/abstracts/#217)_

* [Presentation](https://speakerdeck.com/clearspandex/data-engineering-101-building-your-first-data-product-pydata-sv-2014) (also in [slides.pdf](slides.pdf))
* [Example code](http://nbviewer.ipython.org/github/Jay-Oh-eN/pydatasv2014/blob/master/notebook.ipynb) ([notebook.ipynb](notebook.ipynb))
* [data](data.pkl)

Often times there exists a divide between data teams, engineering, and product managers in organizations, but with the dawn of data driven companies/applications, it is more prescient now than ever to be able to automate your analyses to personalize your users experiences. LinkedIn's People you May Know, Netflix and Pandora's recommenders, and Amazon's eerily custom shopping experience have all shown us why it is essential to leverage data if you want to stay relevant as a company.

As data analyses turn into products, it is essential that your tech/data stack be flexible enough to run models in production, integrate with web applications, and provide users with immediate and valuable feedback. I believe Python is becoming the lingua franca of data science due to its flexibility as a general purpose performant programming language, rich scientific ecosystem (numpy, scipy, scikit-learn, pandas, etc.), web frameworks/community, and utilities/libraries for handling data at scale. In this talk I will walk through a fictional company bringing it's first data product to market. Along the way I will cover Python and data science best practices for such a pipeline, cover some of the pitfalls of what happens when you put models into production, and how to make sure your users (and engineers) are as happy as they can be.

## References

* [Data Generating Products](http://www.adamlaiacano.com/post/57703317453/data-generating-products)
* [Lambda Architecture](http://lambda-architecture.net/)
* [Distilling Data Exhaust](http://www.slideshare.net/pskomoroch/distilling-data-exhaust)
* [Machine Learning, NLP, and Data Science in Python](https://vimeo.com/53058140)

### Libraries

* [requests](http://docs.python-requests.org/en/latest/)
* [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/)
* [pymongo](http://api.mongodb.org/python/2.7rc0/)
* [pandas](http://pandas.pydata.org/)
* [NLTK](http://www.nltk.org/)
* [scikit-learn](http://scikit-learn.org/stable/)
* [yHat](https://docs.yhathq.com/python)
* [Flask](http://flask.pocoo.org/)

#### At Scale

* [scrapy](http://scrapy.org/)
* [Hadoop Streaming](http://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/)
* [snakebite (HDFS)](https://github.com/spotify/snakebite)
* [mrjob](https://github.com/Yelp/mrjob)
* [MLlib](http://spark.apache.org/docs/0.9.0/mllib-guide.html) (and [pySpark](http://spark.apache.org/docs/0.9.1/python-programming-guide.html))