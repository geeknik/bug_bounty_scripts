# Bug Bounty Scripts
Making the hunt for bugs just a little bit easier


IP Range Generator (print_full_ip_range.py)
--------------------------------
The IP Range Generator script is a Python command-line tool that generates a list of IP addresses within a specified range. The user is prompted to enter a starting IP address and an ending IP address, and the script generates all the IP addresses in between.

The script validates the input to ensure that the IP addresses are in the correct format and generates an error message if an invalid IP address is entered. It then iterates over the range of IP addresses and prints each one to the console.


JavaScript File Finder (js_hunt.py)
--------------------------------
The JavaScript File Finder script is a Python command-line tool that extracts URLs of JavaScript files from a given website. The user is prompted to enter a website URL, and the script uses the `requests` library to send an HTTP request to the website and retrieve its HTML content.

The script then uses the `BeautifulSoup` library to parse the HTML content and extract the URLs of all JavaScript files found on the website. It prints each URL to the console.

The script includes error handling for requests that fail or raise an exception, and it prints an error message if an invalid URL is entered. It also includes a user agent in the request to avoid being blocked by certain websites. If no JavaScript files are found on the website, the script prints a message to the user.

Firebase Scanner (firebase-scanner.py)
--------------------------------
![image](https://github.com/geeknik/bug_bounty_scripts/assets/466878/84548548-612c-4801-b89c-569e2e13a504)

The Firebase Scanner script is a Python command-line tool that crawls a list of URLs whilst simultaenously scanning for patterns consistent with Firebase configuration options. For example:
```python
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
```

Pull Requests
--------------------------------
- Find a bug?
  - Submit a pull request! 
- Want to add a feature?
  - Submit a pull request!

# Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The use of our Software and any associated materials (including but not limited to code, libraries, scripts, and examples) is at your own risk. By using our Software, you understand and agree that you are solely responsible for your actions and the consequences thereof. We expressly disclaim any liability or responsibility for any harm resulting from your use of our Software, and by using our Software, you agree to this disclaimer and our terms of use.

Our Software is intended to be used for legal purposes only. It is your responsibility to stay compliant with all the local, state, and federal laws and regulations applicable to you when using our Software. You agree not to use our Software in an illegal manner or to infringe on the rights of others. You agree that you will not use our Software to commit a crime, or to enable others to commit a crime.

We are not responsible for any harm or damage caused by your use of our Software. You agree to indemnify and hold harmless the authors, maintainers, and contributors of the Software for any and all claims arising from your use of our Software, your violation of this disclaimer, or your violation of any rights of a third party.

If you do not agree with this disclaimer, please do not use our Software. Your use of our Software signifies your agreement with this disclaimer.

This disclaimer is subject to change without notice, and it is your responsibility to review this disclaimer periodically to ensure you are aware of its terms.
