# import requests
# from bs4 import BeautifulSoup

# # Replace with the URL of the webpage you want to scrape
# url = 'https://tax.gov.ae/en/faq.aspx'

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the page content
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all elements that contain the questions and answers
#     questions = soup.find_all('a', {'data-toggle': 'collapse'})
#     answers = soup.find_all('div', class_='faq-body')
    
#     # Iterate through questions and answers
#     for question, answer in zip(questions, answers):
#         # Extract question text
#         question_text = question.get_text(strip=True)
        
#         # Extract answer text, removing unnecessary whitespace
#         answer_text = answer.get_text(separator=' ', strip=True)
        
#         # Print the question and answer
#         print(f"Question: {question_text}")
#         print(f"Answer: {answer_text}")
#         print("-" * 50)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
base_url = 'https://tax.gov.ae/en/faq.aspx'  # Replace with the actual URL

# Start session to maintain cookies and state
session = requests.Session()

# Function to scrape a single page
def scrape_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    questions = soup.find_all('a', {'data-toggle': 'collapse'})
    answers = soup.find_all('div', class_='faq-body')

    data = []
    for question, answer in zip(questions, answers):
        question_text = question.get_text(strip=True)
        answer_text = answer.get_text(separator=' ', strip=True)
        data.append((question_text, answer_text))
    return data

# Function to get form data from the page
def get_form_data(soup):
    form_data = {}
    form_data['__VIEWSTATE'] = soup.find('input', {'id': '__VIEWSTATE'})['value'] if soup.find('input', {'id': '__VIEWSTATE'}) else ''
    form_data['__VIEWSTATEGENERATOR'] = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value'] if soup.find('input', {'id': '__VIEWSTATEGENERATOR'}) else ''
    form_data['__EVENTVALIDATION'] = soup.find('input', {'id': '__EVENTVALIDATION'})['value'] if soup.find('input', {'id': '__EVENTVALIDATION'}) else ''
    return form_data

# Scrape the first page and get initial form data
response = session.get(base_url)
if response.status_code == 200:
    all_data = []
    soup = BeautifulSoup(response.text, 'html.parser')
    form_data = get_form_data(soup)  # Get form data from the initial page
    all_data.extend(scrape_page(response.text))

    # Find the total number of pages from the pagination
    max_page = 22  # Set this to the total number of pages manually

    # Scrape remaining pages
    for page_num in range(2, max_page + 1):
        # Update form data for navigation
        form_data['__EVENTTARGET'] = f'ctl00$ctrlContentArea$NewsList2013724114611$pgList$ctl00$PageButton{page_num}'
        form_data['__EVENTARGUMENT'] = ''

        # Send POST request to navigate to the desired page
        page_response = session.post(base_url, data=form_data)
        if page_response.status_code == 200:
            all_data.extend(scrape_page(page_response.text))
            print(f"Scraped page {page_num}")
            # Update form data for the next request
            soup = BeautifulSoup(page_response.text, 'html.parser')
            form_data.update(get_form_data(soup))
        else:
            print(f"Failed to retrieve page {page_num}. Status code: {page_response.status_code}")

    # Write the collected data to a text file
    with open('scraped_faqs.txt', 'w', encoding='utf-8') as f:
        for question, answer in all_data:
            f.write(f"Question: {question}\n")
            f.write(f"Answer: {answer}\n")
            f.write("-" * 50 + "\n")

    print("Data saved to scraped_faqs.txt")

else:
    print(f"Failed to retrieve the initial page. Status code: {response.status_code}")