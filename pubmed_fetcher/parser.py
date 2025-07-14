
import xml.etree.ElementTree as ET
from typing import Dict, List
from .utils import extract_company_info
import re

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        emails = []
        affiliations = []

        for aff in article.findall(".//AffiliationInfo"):
            aff_text = aff.findtext("Affiliation")
            if aff_text:
                affiliations.append(aff_text)
                emails.extend(extract_emails(aff_text))

        non_academic_authors, companies = extract_company_info(affiliations)

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(non_academic_authors),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": "; ".join(set(emails))
        })

    return results

def extract_emails(text: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
