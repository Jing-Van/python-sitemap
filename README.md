# Python-Sitemap

# reference: https://github.com/c4software/python-sitemap

crawl one domain and create a sitemap.xml of all public link in it.

Language supported:; Python3

## usage

	$ python main.py --domain https://www.sedna.com --output sitemap.xml
	$ python main.py --domain  https://www.sedna.com/ --output sitemapimages.xml --images --debug --verbose
    $ python main.py --domain  https://www.sedna.com/ --output sitemapimages.xml --images --report --skipext pdf --skipext xml --parserobots --num-workers 4
    
## report output
Number of found URL : 110
Number of links crawled : 108
Number of link block by robots.txt : 0
Number of link exclude : 2
Nb Code HTTP 200 : 108    
#### --images Enable Image Sitemap

#### --report Enable report for print summary of the crawl:

#### --skipext pdf --skipext xml Skip url (by extension) (skip pdf AND xml url):

#### --drop "id=[0-9]{5}" Drop a part of an url via regexp :
  ```
  $ python main.py --domain https://www.sedna.com --output sitemap.xml --drop "id=[0-9]{5}"
  ```
#### Exclude url by filter a part of it :
  ```
  $ python main.py --domain https://www.sedna.com --output sitemap.xml --exclude "action=edit"
  ```
#### --parserobots Read the robots.txt to ignore some url:

#### --num-workers 4 Multithreaded