antmap
======

Set of tools to parse, classify and represent species data in the bio lab I intern at

hey


Uses a parsing script written in python with the docx parsing library to parse and populate SQlite DB through Django.

Data is sent with django preprocessor and using javascript, the broswer parses the data and format them into first geocode requests to Google API then use the returned GPS coordinates to make a second request to Google map's API

python 2.7.6


## References
[https://developers.google.com/maps/documentation/geocoding/](https://developers.google.com/maps/documentation/geocoding/ "Geocode API")

[https://developers.google.com/maps/documentation/javascript/tutorial](https://developers.google.com/maps/documentation/javascript/tutorial](https://developers.google.com/maps/documentation/javascript/tutorial "Google maps API")

[https://github.com/mikemaccana/python-docx](https://github.com/mikemaccana/python-docx "python-docx")
