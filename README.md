## • API Setup

* Go to http://my.telegram.org  and log in.
* Click on API development tools and fill the required fields.
* put app name you want & select other in platform Example :
* copy "api_id" & "api_hash" after clicking create app ( will be used in setup.py )

`$ python -m venv myvenv`

`$ source myvenv/bin/activate`

* Install requierments & Setup Configuration File. ( apiID, apiHash )

`$ python setup.py`

* To Scare members from group.

`$ python scraper.py`

* Add Scarped members to your group. 

`$ python adder.py`