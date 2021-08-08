from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import filters as fl
import time
import json
import re
import os

SCROLL = 5  # More than 10 will be very slow, min is 1
URL = 'https://glints.com/id/opportunities/jobs/explore?country=ID&locationName=Indonesia&jobCategories=1&cities=28904'


def cleanData():
    print("Cleaning data...")
    path = "../data"
    files = os.listdir(path)
    list_file = [file for file in files if file.endswith(".json")]
    for file in list_file:
        path_to_file = os.path.join(path, file)
        os.remove(path_to_file)
    print("Data cleaned!")


def getPage(url):
    # Get Page: encode HTML from url
    options = Options()
    options.add_argument('--headless')      # hide chrome window
    options.add_argument('--disable-gpu')   # necessary for headless mode
    options.add_argument('log-level=3')     # ignore most warnings
    # Options to be able to scroll the page
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--start-maximised")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(30)
    driver.get(url)
    print(f'Progress: scrolled [{1}/{SCROLL}]')
    for i in range(1, SCROLL):  # Scroll X times
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)  # loading time for browser to load the url
        print(f'Progress: scrolled [{i+1}/{SCROLL}]')
    html_source = driver.page_source
    driver.quit()
    print("HTML retrieved from web")
    return html_source.encode('utf8')


def writeToFile(index, arr):
    # writeToFile: Write to json file format
    # print(arr)
    d = {
        "title": arr[0],
        "company": arr[1],
        "location": arr[2],
        "currency": arr[3],
        "start_sal": arr[4],
        "end_sal": arr[5],
        "exp_min": arr[6],
        "exp_opt": arr[7],
        "last_updated": arr[8],
        "applicant": arr[9]
    }
    json_object = json.dumps(d, indent=4, ensure_ascii=False)
    with open(f'../data/{index}_job.json', 'w', encoding='utf8') as f:
        f.write(json_object)


def scrapingData(jobs):
    arr = []
    title = fl.findJobTitle(jobs)
    arr += [title]

    company = fl.findJobCompany(jobs)
    arr += [company]

    info = fl.findJobInfo(jobs)
    arr += fl.filterInfo(info)

    last_updated = fl.findJobLastUpdated(jobs)
    arr += fl.filterLastUpdated(last_updated)

    appl = fl.findJobApplicantCount(jobs)
    if (appl != None):  # Case of no info
        arr += [int(appl.text.split()[0])]
    else:
        arr += [None]
    return arr


def main():
    html_text = getPage(URL)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs_cards = soup.find_all(
        'div', attrs={"class": re.compile(r'(CompactJobCard-sc)')})
    print("Web Scraping finished")
    for index, jobs in enumerate(jobs_cards):
        arr = scrapingData(jobs)
        writeToFile(index, arr)
    print("Done writing result to files, check Data Scraping/data")
    print("FINISHED!")


cleanData()
main()
