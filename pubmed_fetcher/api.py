
import requests
from typing import List
import time

EMAIL = "your-email@example.com"

def fetch_pubmed_ids(query: str, debug: bool = False) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100
    }
    response = requests.get(url, params=params)
    data = response.json()
    if debug:
        print(f"[DEBUG] Fetched IDs: {data}")
    return data['esearchresult']['idlist']

def fetch_pubmed_details(pmid_list: List[str], debug: bool = False) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    ids = ",".join(pmid_list)
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml",
        "email": EMAIL
    }
    time.sleep(1)
    response = requests.get(url, params=params)
    if debug:
        print("[DEBUG] Fetched details XML.")
    return response.text
