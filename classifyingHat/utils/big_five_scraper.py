import requests

from bs4 import BeautifulSoup

import re


def get_test_results(results_id):
    if not re.match(r'^[a-zA-Z0-9]*$', results_id):
        raise TypeError("Invalid results ID")
    results_url = f"https://bigfive-test.com/en/result/{results_id}"
    req = requests.get(results_url)

    soup = BeautifulSoup(req.content, 'html.parser')

    domains = {
        "extraversion": "",
        "neuroticism": "",
        "openness": "",
        "agreeableness": "",
        "conscientiousness": ""
    }

    try:
        hydration_scripts = ""
        for script in soup.findAll('script'):
            if script.string and "self.__next_f.push" in script.string:
                hydration_scripts += script.string

        for key in domains.keys():
            domain_dict = re.search(
                r'{[^{]*\\"domain\\":\\"'+key[0].upper()+r'\\".*?}', hydration_scripts).group()  # The \ are because the json is escaped like that
            domains[key] = int(re.search(
                r'\\"score\\":(\d+),', domain_dict).group(1))  # I do this in a different search just in case the keys aren't in order (better safe than sorry)
    except:
        raise Exception(
            "The id is invalid or there was an error while scraping the page")

    return domains
