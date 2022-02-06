from bs4 import BeautifulSoup

# Reading data from the xml file
with open('Details.xml', 'r') as f:
	data = f.read()

# Passing the data of the xml
# file to the xml parser of
# beautifulsoup
bs_data = BeautifulSoup(data, 'xml')

# A loop for replacing the value
# of attribute `price` to WHAT !!
# The tag is found by the clause
# `bs_data.find_all('Product', {'name':'TV'})`
for tag in bs_data.find_all('Product', {'name':'TV'}):
	tag['price'] = "WHAT !!"


# Output the contents of the
# modified xml file
print(bs_data.prettify())
