import requests

from bs4 import BeautifulSoup

import re

def get_test_results(results_id):
    if not re.match(r'^[a-zA-Z0-9]*$', results_id):
        raise TypeError("Invalid results ID")
    results_url = f"https://bigfive-test.com/result/{results_id}?lang=en"
    req = requests.get(results_url)

    soup = BeautifulSoup(req.content, 'html.parser') 

    domains = {
        "extraversion" :"", 
        "neuroticism" :"", 
        "openness to experience" :"", 
        "agreeableness" :"", 
        "conscientiousness" :""
    }

    if soup.find('p', attrs={"class": "headline"}):
        raise TypeError("Invalid results ID")

    try:
        for key in domains.keys():
            a = soup.find(id=key)
            subheading = a.parent.find('p').contents[0]
            domains[key] = int(re.findall(r'\d+', subheading)[0])
    except:
        raise Exception("There was an error while scraping the page")

    domains['openness'] = domains.pop('openness to experience') # For cohesion with the rest of the modules

    return domains