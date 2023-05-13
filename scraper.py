import requests


ID_CREDENTIALS = "rKORoexkrfgZYPI1ScyMg1kzd2u266szTPq9nbSA"
PASS_CREDENTIALS = ""






def scraper_from_UPC():
    response = requests.get('https://api.fib.upc.edu/v2/assignatures/?format=api;lang=en;client_id='+ID_CREDENTIALS)
    return response
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


print(scraper_from_UPC().text)