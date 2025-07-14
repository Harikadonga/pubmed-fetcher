
# PubMed Fetcher

A Python command-line tool that fetches research papers from PubMed based on a user-specified search query and filters for papers with authors affiliated with pharmaceutical or biotech companies. Results are exported as a CSV file with essential metadata.

---

##  Features

-  **PubMed Search**: Search PubMed using full query syntax
-  **Pharma/Biotech Detection**: Identify non-academic affiliations using company and industry keywords
-  **Metadata Extraction**: Extract paper title, authors, publication date, affiliations, and more
-  **CSV Export**: Save structured results as CSV
-  **Rate Limiting**: Built-in delays to respect NCBI usage policies
-  **Command-line Options**: Flexible search and output settings

---

##  Installation

### Clone the repo

```bash
git clone https://github.com/Harikadonga/pubmed-fetcher.git
cd pubmed-fetcher
```

### Install dependencies

Using Poetry (recommended):

```bash
poetry install
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

##  Usage

### Basic Example

```bash
poetry run get-papers-list "your search query"
```

### With CSV output

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv --debug
```

---

##  Command Line Options

| Option           | Description                                      |
|------------------|--------------------------------------------------|
| `-q` / `<query>` | PubMed search query (positional, required)       |
| `-f` / `--file`  | Output CSV file name (optional)                  |
| `-d` / `--debug` | Print debug logs during execution (optional)     |

---

##  Output Format

The generated CSV file contains:

- `PubmedID`: Unique ID for the paper
- `Title`: Paper title
- `Publication Date`: Year of publication
- `Non-academic Author(s)`: Authors from non-academic affiliations
- `Company Affiliation(s)`: Detected pharma/biotech companies
- `Corresponding Author Email`: Detected email addresses

---

##  Pharma/Biotech Affiliation Detection

### Company Keywords
Pfizer, Novartis, Roche, Johnson & Johnson, Merck, GSK, AstraZeneca, Sanofi, Bayer, AbbVie, Amgen, Biogen, Gilead, Moderna, BioNTech, Regeneron, Eli Lilly, BMS, Takeda, Daiichi Sankyo, Astellas, Boehringer Ingelheim, Genentech, and others.

### Industry Keywords
`pharma`, `biotech`, `biopharma`, `drug`, `medication`, `clinical`, `therapeutics`, `vaccine`, `genomics`, `molecular`, `healthcare`, `CRISPR`, `oncology`, and more.

The tool uses heuristics to identify non-academic institutions by checking for absence of academic keywords like `university`, `institute`, `hospital`, etc.

---

##  Error Handling

The tool gracefully handles:

- ## Invalid or empty search queries
- ## Network or API failures
- ## Missing or malformed emails
- ## Incomplete metadata
- ## Rate limits or API abuse warnings

---

##  Examples

```bash
# Search COVID-19 vaccine papers
poetry run get-papers-list "COVID-19 vaccine" -f covid.csv

# Cancer treatment with 25 results only
poetry run get-papers-list "cancer treatment" -f cancer.csv --debug

# Diabetes papers, print to console
poetry run get-papers-list "diabetes mellitus type 2"
```

---

##  Contributing

Contributions are welcome! You can help by:

- Adding more pharma/biotech companies or keywords
- Improving email and affiliation detection
- Writing more tests
- Enhancing performance or usability

---

##  License

This project is licensed under the MIT License.

---

##  Support

If you encounter issues:

- Ensure your internet connection is stable
- Use a valid email (for NCBI compliance)
- Check if you're hitting API limits (slow down queries)
- Try simplifying your search query

---

##  Project Stats

**Languages:** Python 100%  
**Version:** 0.1.0  
**Status:** In development  

---

## 🔗 Resources

- [NCBI PubMed API Docs](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Poetry Package Manager](https://python-poetry.org/)
