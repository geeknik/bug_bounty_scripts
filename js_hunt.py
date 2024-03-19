#!/usr/bin/env python3

import os
import sys
import requests
from bs4 import BeautifulSoup

def get_urls(website):
    try:
        # Make the request with a user agent.
        response = requests.get(website, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all of the URLs to JavaScript files.
    urls = []
    for link in soup.find_all('script', src=True):
        if link['src'].endswith('.js'):
            urls.append(link['src'])
    return urls

def main():
    # Get the website from the command line.
    try:
        website = sys.argv[1]
    except IndexError:
        print('Usage: {} <website>'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    # Get the URLs to JavaScript files.
    urls = get_urls(website)
    # Print the URLs to the user.
    if not urls:
        print("No JavaScript files found.")
    else:
        for url in urls:
            print(url)

# Invoke the main function.
if __name__ == '__main__':
    main()
