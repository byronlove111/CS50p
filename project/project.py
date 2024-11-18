import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    try:
        html = requests.get(url)
        html.raise_for_status()
        return html.text
    except requests.exceptions.RequestException:
        return None

def extract_titles(html_content):
    titles = []
    soup = BeautifulSoup(html_content, 'html.parser')
    section_div = soup.find('section')
    list_h3 = section_div.find_all('h3')
    for h3 in list_h3:
        title = h3.find('a').get('title')
        titles.append(title)
    return titles

def scrape_books():
    page = 1
    all_titles = []

    while True:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        html_content = get_page_content(url)

        if html_content is None:
            print("End of program.")
            break

        page_titles = extract_titles(html_content)
        all_titles.extend(page_titles)
        print("Scraping page", page)
        page += 1

    with open("titles.txt", 'a', encoding='utf-8') as f:
        for title in all_titles:
            f.write(title)
            f.write('\n')

def main():
    scrape_books()

if __name__ == "__main__":
    main()
