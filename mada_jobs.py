import requests
from bs4 import BeautifulSoup


def parse_job(url):
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, "html5lib")

    job_aside = soup.findAll("aside", class_="contenu_annonce")
    
    if job_aside:
        for job_description in job_aside:
            job_title = job_description.find("strong").text
            entreprise = job_description.find("h4").text
            contract_type = job_description.find("h5").text
            a_tag = job_description.findAll("a")
            description_href = a_tag[-1]['href']

            print(f"Entreprise: {entreprise}\nPoste: {job_title}\nType de contrat: {contract_type}\nDetail: {description_href}")
            print("\n")


def get_pages(nb_pages):
    urls = []
    page_number = 1

    for _ in range(nb_pages):
        if page_number == 1:
            url = "https://www.portaljob-madagascar.com/emploi/liste"
            page_number += 1
            urls.append(url)
        else:
            url = f"https://www.portaljob-madagascar.com/emploi/liste/page/{page_number}"
            page_number += 1
            urls.append(url)

    return urls


if __name__ == "__main__":
    urls = get_pages(10)
    page_number = 1

    for url in urls:
        print(f"---------- Page {page_number} ----------")
        parse_job(url)
        page_number += 1
