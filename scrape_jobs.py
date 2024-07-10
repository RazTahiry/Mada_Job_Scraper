import requests
from bs4 import BeautifulSoup
import argparse
import csv


def parse_job(url, csv_writer=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html5lib")

    job_asides = soup.find_all("aside", class_="contenu_annonce")
    
    if job_asides:
        for job_description in job_asides:
            job_title = job_description.find("strong").get_text(strip=True)
            entreprise = job_description.find("h4").get_text(strip=True)
            contract_type = job_description.find("h5").get_text(strip=True)
            a_tags = job_description.find_all("a")
            date_limit = job_description.find('i', class_="date_lim")
            date_limit_value = date_limit.get_text(strip=True) if date_limit else "Date limite : -"
            description_href = a_tags[-1]['href'] if a_tags else "Non disponible."

            if csv_writer:
                date_limit_value = date_limit_value.replace("Date limite : ", "")
                csv_writer.writerow([entreprise, job_title, contract_type, date_limit_value, description_href])
            else:
                print(f"Entreprise : {entreprise}")
                print(f"Poste : {job_title}")
                print(f"Type de contrat : {contract_type}")
                print(f"{date_limit_value}")
                print(f"Detail : {description_href}\n")


def get_pages(pages_quantity):
    base_url = "https://www.portaljob-madagascar.com/emploi/liste"
    return [base_url] + [f"{base_url}/page/{page_number}" for page_number in range(2, pages_quantity + 1)]


def arguments_parser():
    parser = argparse.ArgumentParser(description='Scrape jobs from portaljob-madagascar.com')
    parser.add_argument('pages_quantity', metavar='N', type=int, choices=range(1, 481), 
                            help='Quantity of paginations to display')
    parser.add_argument('--csv', dest='csv_file', help='CSV file to save the job descriptions')
    return parser.parse_args()


if __name__ == "__main__":
    args = arguments_parser()
    pages_quantity = args.pages_quantity
    csv_file = args.csv_file
    urls = get_pages(pages_quantity)

    csv_writer = None
    if csv_file:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Entreprise', 'Poste', 'Type de contrat', 'Date limite', 'Detail'])
            
            print("Wait! Writing jobs to csv file...")
            for index, url in enumerate(urls, start=1):
                parse_job(url, csv_writer)

        csv_file.close()
        print("Done!")
    else:
        title_description = "from the first page." if pages_quantity == 1 else f"from page 1 to {pages_quantity}."
        print(f"Displaying jobs {title_description}\n")

        for index, url in enumerate(urls, start=1):
            print(f"------------------------------ Page {index} ------------------------------\n")
            parse_job(url)
            