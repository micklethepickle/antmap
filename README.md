antmap
======

Set of tools to parse, classify and represent species data in the bio lab I intern at


Uses a parsing script written in python with the docx parsing library to parse and populate SQlite DB through Django.

Information is sent with django preprocessor and using javascript, I parse the data and format them into first geocode requests to Google API then use the returned GPS coordinates, I make a second request to Google map's API
