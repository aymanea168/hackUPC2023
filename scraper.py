import requests


ID_CREDENTIALS = ""
PASS_CREDENTIALS = ""



fr

def scraper_from_UPC():
    response = requests.get("https://api.fib.upc.edu/")

    """
    url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

    # API uses JSON.
    headers = {'content-type': 'application/json'}
    # Send HTTP POST with username and password.
    response = requests.request("POST",
                                url, 
                                auth=HTTPBasicAuth(username, password),
                                headers=headers, verify=False)
        """
