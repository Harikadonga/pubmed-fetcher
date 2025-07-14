
from pubmed_fetcher.utils import is_non_academic

def test_non_academic_check():
    assert is_non_academic("Pfizer Inc.") == True
    assert is_non_academic("Harvard University") == False
