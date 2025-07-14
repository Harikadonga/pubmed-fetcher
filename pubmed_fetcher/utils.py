
from typing import Tuple, List
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "center"]
    return not any(word.lower() in affiliation.lower() for word in academic_keywords)

def extract_company_info(affiliations: List[str]) -> Tuple[List[str], List[str]]:
    non_academic_authors = []
    companies = []

    for aff in affiliations:
        if is_non_academic(aff):
            companies.append(aff)
            name_match = re.match(r"(.+?),", aff)
            if name_match:
                non_academic_authors.append(name_match.group(1))
    
    return list(set(non_academic_authors)), list(set(companies))
