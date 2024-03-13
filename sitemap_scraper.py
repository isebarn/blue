import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_urls():
    # URL of the sitemap
    sitemap_url = "https://www.bluettipower.eu/sitemap_products_1.xml?from=6644260962501&to=8453516230923"

    # Send a GET request to the sitemap URL
    response = requests.get(sitemap_url)

    # # Parse the XML content of the sitemap
    soup = BeautifulSoup(response.content, "xml")
    #
    # # Find all <loc> tags and store their text content (URLs) in a list
    urls = [url.text for url in soup.find_all("loc")]

    #
    # # Remove shopify cdn links
    clean_urls = [url for url in urls if url.startswith("https://www.bluettipower.eu/products")]

    # # Convert the list of URLs into a DataFrame
    urls_df = pd.DataFrame(clean_urls, columns=["URLs"])

    # # Save the DataFrame to an Excel file
    urls_df.to_excel("urls.xlsx", index=False)

get_urls()