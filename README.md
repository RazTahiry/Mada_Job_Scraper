## Overview

This script is designed to scrape job listings from the website [portaljob-madagascar.com](https://www.portaljob-madagascar.com) and either display them in the console or save them to a CSV file.

## Features

- Fetch job listings from multiple pages.
- Display job details such as the company name, job title, contract type, application deadline, and job description link.
- Save job details to a CSV file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `argparse` library (standard with Python)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

The script can be run from the command line. It accepts two arguments:
1. The number of pages to scrape (required, an integer between 1 and 480).
2. An optional argument to specify a CSV file to save the job details.

### Command Line Arguments

- `pages_quantity` (required): Number of pages to scrape.
- `--csv` (optional): Path to the CSV file where job details will be saved.

### Examples

1. **Display job details in the console:**

```bash
python job_scraper.py 3
```

This command will scrape job listings from the first 3 pages and display the details in the console.

2. **Save job details to a CSV file:**

```bash
python job_scraper.py 3 --csv jobs.csv
```

This command will scrape job listings from the first 3 pages and save the details to `jobs.csv`.

## Notes

- The script handles up to 480 pages due to the pagination limit on the website.
- Ensure that the website structure remains unchanged; otherwise, the script may need modifications to adapt to any changes.
