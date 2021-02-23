from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
# soup.find(text="bad")

# 'bad'
# >>> soup.i
# <i>HTML</i>
# #
# >>> soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
# #
# >>> print(soup.prettify())
# <?xml version="1.0" encoding="utf-8"?>
# <tag1>
#  Some
#  <tag2/>
#  bad
#  <tag3>
#   XML
#  </tag3>
# </tag1> 