import requests
import re
import os
from colorama import init, Fore, Style
from urllib.parse import urlparse, urlunparse, urljoin
from validators import url as validator_url
from concurrent.futures import ThreadPoolExecutor
import urllib3

init()  # Initialize colorama for color output
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Suppress InsecureRequestWarning

def is_valid_url(url):
    return validator_url(url)

def add_scheme(url):
    if not urlparse(url).scheme:
        schemes = ["http://", "https://"]
        for scheme in schemes:
            new_url = urlunparse((scheme, url, "", "", "", ""))
            try:
                response = requests.head(new_url)
                if response.status_code < 400:
                    return new_url
            except requests.exceptions.RequestException:
                pass
    return url

def process_url(url):
    print(f"\nScanning: {url}")
    try:
        url = add_scheme(url)  # Add scheme if missing
        if is_valid_url(url):  # Validate URL after adding the scheme
            scan_firebase_config(url)
        else:
            print(f"{Fore.RED}Invalid URL: {url}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error occurred while processing the URL: {url}{Style.RESET_ALL}")
        print(f"{Fore.RED}Error details: {str(e)}{Style.RESET_ALL}")
        with open("errors.txt", "a") as file:
            file.write(f"Error occurred while processing the URL {url}: {str(e)}\n")


def download_js_files(url):
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification
        content = response.text

        # Regular expression pattern to find JavaScript file URLs
        pattern = r'<script\s+src="([^"]+\.js)"'
        js_files = re.findall(pattern, content)

        # Download each JavaScript file
        for js_file in js_files:
            js_url = urljoin(url, js_file)  # Construct the absolute URL
            js_response = requests.get(js_url, verify=False)  # Disable SSL verification
            with open(os.path.basename(js_file), "w") as file:
                file.write(js_response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading JavaScript files: {e}")

def scan_firebase_config(url):
    try:
        # Add scheme if missing
        url = add_scheme(url)

        # Fetch the website content
        response = requests.get(url, verify=False)
        content = response.text

        # Regular expression patterns for Firebase configuration variables
        patterns = [
                # Handle variables defined with var, let, const, and no keyword
                r'(?:var|let|const|\s)apiKey\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)authDomain\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)databaseURL\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)projectId\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)storageBucket\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)messagingSenderId\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)appId\s*=\s*([\'"\`].*?[\'"\`])',
		r'(?:var|let|const|\s)measurementId\s*=\s*([\'"\`].*?[\'"\`])',
		# Handle objects defined with curly braces and new keyword
		r'(?:new\s+FirebaseConfig|\{)\s*apiKey\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*authDomain\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*databaseURL\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*projectId\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*storageBucket\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*messagingSenderId\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*appId\s*:\s*([\'"\`].*?[\'"\`])',
		r'(?:new\s+FirebaseConfig|\{)\s*measurementId\s*:\s*([\'"\`].*?[\'"\`])',
		# Handle comments
		r'/\*[\s\S]*?apiKey\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?apiKey\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?authDomain\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?authDomain\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?databaseURL\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?databaseURL\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?projectId\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?projectId\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?storageBucket\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?storageBucket\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?messagingSenderId\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?messagingSenderId\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?appId\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?appId\s*:\s*([\'"\`].*?[\'"\`])',
		r'/\*[\s\S]*?measurementId\s*:\s*([\'"\`].*?[\'"\`])[\s\S]*?\*/',
		r'//.*?measurementId\s*:\s*([\'"\`].*?[\'"\`])',
	]

        # Search for Firebase configuration variables in the content
        found_variables = []
        for pattern in patterns:
            matches = re.findall(pattern, content)
            if matches:
                found_variables.append(matches[0])

        if found_variables:
            print(f"{Fore.GREEN}Firebase configuration variables found in {url}:{Style.RESET_ALL}")
            for variable in found_variables:
                print(f"  - {variable}")
            with open("results.txt", "a") as file:
                file.write(f"Firebase configuration variables found in {url}:\n")
                for variable in found_variables:
                    file.write(f"  - {variable}\n")
        else:
            print(f"{Fore.YELLOW}No Firebase configuration variables found in {url}{Style.RESET_ALL}")

        # Download and scan JavaScript files
        download_js_files(url)
        js_files = [file for file in os.listdir() if file.endswith(".js")]
        for js_file in js_files:
            with open(js_file, "r") as file:
                js_content = file.read()
                js_found_variables = []
                for pattern in patterns:
                    matches = re.findall(pattern, js_content)
                    if matches:
                        js_found_variables.append(matches[0])
            if js_found_variables:
                print(f"{Fore.GREEN}Firebase configuration variables found in {js_file}:{Style.RESET_ALL}")
                for variable in js_found_variables:
                    print(f"  - {variable}")
                with open("results.txt", "a") as file:
                    file.write(f"Firebase configuration variables found in {js_file}:\n")
                    for variable in js_found_variables:
                        file.write(f"  - {variable}\n")
            os.remove(js_file)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error occurred while fetching the website: {url}{Style.RESET_ALL}")
        print(f"{Fore.RED}Error details: {str(e)}{Style.RESET_ALL}")
        with open("errors.txt", "a") as file:
            file.write(f"Error occurred while fetching the website {url}: {str(e)}\n")

def read_urls_from_file(file_path):
    with open(file_path, "r") as file:
        urls = file.read().splitlines()
    return urls

def get_user_input():
    urls = []
    while True:
        url = input("Enter a URL (or press Enter to finish): ")
        if url == "":
            break
        urls.append(url)
    return urls

def main():
    print("Firebase Configuration Scanner")
    print("1. Read URLs from a file")
    print("2. Enter URLs manually")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        file_path = input("Enter the file path containing URLs: ")
        urls = read_urls_from_file(file_path)
    elif choice == "2":
        urls = get_user_input()
    else:
        print("Invalid choice. Exiting.")
        return

    for url in urls:
        print(f"\nScanning: {url}")
        if is_valid_url(url):
            scan_firebase_config(url)

    with ThreadPoolExecutor() as executor:
        for url in urls:
            if is_valid_url(url):
                executor.submit(process_url, url)

    print("\nScanning completed.")
    print("Results saved in 'results.txt'.")
    print("Errors logged in 'errors.txt'.")

if __name__ == "__main__":
    main()
