import requests  # Allows us to easily make HTTP Get requests of URL's
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/cloud-computing-books"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# print(r.status_code) = shows if successful (200)
# print(r.text) = shows all of the text of the HTML of the link we scraped as a string

# Bundle Tiers = .dd-header-headline

# soup.find_all('h2') = find_all finds all of the same tag type, in this case, h2

# Now we want to build our data-structure, which will be a dictionary of tiers, which will contain a "Price" key of an int, and a "Product" value with a list of products of that price
#
#   - tier1 name and price
#       - product 1
#       - product 2
#   - tier2 name and price
#       - product 1
#       - product 2

tier_dict = {}

tiers = soup.select(".dd-game-row")

for tier in tiers:
    # Only for sections that have a headline
    if tier.select(".dd-header-headline"):
        # Grab the name and price
        tiername = tier.select(".dd-header-headline").text.strip()
        # Grab tier product names
        product_names = tier.select(".dd-image-box-caption")
        product_names = [prodname.text.strip() for prodname in product_names]
        # Place in the dictionary
        tier_dict[tiername] = {"products": product_names}

###################################[Individual Pieces Below]###################################################################

# Get all of the elements within the headline's component in the website
tier_headlines = soup.select(".dd-header-headline")
# Get the text, then strip the white-space around it
tier_headlines[0].text.strip()

# Loop for stripping the whitespace
new_tiers = []
for tier in tier_headlines:
    new_tiers.append(tier.text.strip())

# Loops through the tier_headlines for the tiers and allows us to text/strip them, equivalent to the above loop
stripped_tiernames = [tier.text.strip() for tier in tier_headlines]


# Get the product names from the soup
product_names = soup.select(".dd-image-box-caption")
stripped_product_names = [prodname.text.strip() for prodname in tier_headlines]

# Now get the prices from the products in the soup


# print(tiers["tier1"]["products"])

for tiername, tierinfo in tiers.items():  # Use "items()" for Dictionaries, "enumerate" for Lists
    print(tiername)
    print("products:")
    print(", ".join(tierinfo['products']))
    print("\n\n")
