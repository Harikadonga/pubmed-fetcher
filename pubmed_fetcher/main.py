
import argparse
import csv
from .api import fetch_pubmed_ids, fetch_pubmed_details
from .parser import parse_pubmed_xml

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with company-affiliated authors.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    
    args = parser.parse_args()
    
    pmids = fetch_pubmed_ids(args.query, args.debug)
    if not pmids:
        print("No papers found.")
        return

    xml_data = fetch_pubmed_details(pmids, args.debug)
    parsed_data = parse_pubmed_xml(xml_data)

    if args.file:
        with open(args.file, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=parsed_data[0].keys())
            writer.writeheader()
            writer.writerows(parsed_data)
        print(f"Saved to {args.file}")
    else:
        for row in parsed_data:
            print(row)

if __name__ == "__main__":
    main()
