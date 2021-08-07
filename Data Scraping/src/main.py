from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json
import re
import os

SCROLL = 3  # More than 10 will be very slow, min is 1
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


def parseExp(old_exp):
    # Handling experience info (separate them into min exp and optimal exp)
    exp = str(old_exp)
    if ("Kurang" in exp):  # Case of less than 1 year exp needed
        return [0, 1]
    elif (exp == ""):  # Case of no experience needed, or no info
        return [None, None]
    else:  # Case of certain range of experience is needed
        return [int(s) for s in re.findall(r'\d+', exp)]


def parseSalary(old_salary):
    sal = str(old_salary)
    if ("Login" in sal):
        return [None, None, None]  # Currency, start_sal, end_sal
    else:
        sal_split = sal.split()
        curr = sal_split[0]
        if (len(sal_split) < 4):
            return [curr, sal_split[1], None]
        else:
            return [curr, int(sal_split[1].replace('.', '').replace(',', '')), int(sal_split[3].replace('.', '').replace(',', ''))]


def parseInfo(old_info):
    # Separate info into location, salary, and experience (still in string form)
    info = old_info.find_all(
        'div', attrs={"class": re.compile(r'(OpportunityInfo-sc)')})
    if (len(info) > 2):  # Case of full info
        loc = info[0].text.strip()
        sal = parseSalary(info[1].text.strip())
        temp = parseExp(info[2].text.strip())
    elif (len(info) == 2):  # Case of missing 1 info
        loc = info[0].text.strip()
        sal = [None, None, None]
        if ("tahun" in info[1].text.strip()):  # Case of no salary info
            temp = parseExp(info[1].text.strip())
        elif (info[1].text.strip() == ""):  # Case of no both info but counted as 2
            temp = [None, None]
        else:   # Case of no experience info
            sal = parseSalary(info[1].text.strip())
            temp = [None, None]
    elif (len(info) == 1):  # Case of no salary and experience info
        loc = info[0].text.strip()
        sal = [None, None, None]
        temp = [None, None]
    else:  # Case of no info at all
        return [None, None, None, None, None, None]
    return ([loc] + sal + temp)


def main():
    html_text = getPage(URL)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs_cards = soup.find_all(
        'div', attrs={"class": re.compile(r'(CompactJobCard-sc)')})
    print("Web Scraping finished")
    for index, jobs in enumerate(jobs_cards):
        arr = []
        # JOB TITLE #
        title = jobs.find(
            'h3', attrs={"class": re.compile(r'(JobTitle)')}).text
        arr += [title]

        # JOB COMPANY #
        company = jobs.find(
            'span', attrs={"class": re.compile(r'(CompanyLinkContainer)')}).text
        arr += [company]

        # JOB INFO # location, salary, experience
        info = jobs.find(
            'div', attrs={"class": re.compile(r'(OpportunityInfoContainer)')})
        arr += parseInfo(info)

        # JOB LAST UPDATED #
        last_updated = jobs.find(
            'span', attrs={"class": re.compile(r'(UpdatedAtMessage)')}).text.strip()[11:]
        arr += [last_updated]

        # JOB APPLICANT COUNT #
        appl = jobs.find(
            'div', attrs={"class": re.compile(r'(ApplicantCount)')})
        if (appl != None):  # Case of no info
            arr += [int(appl.text.split()[0])]
        else:
            arr += [None]

        writeToFile(index, arr)
    print("Done writing result to files, check Data Scraping/data")
    print("FINISHED!")


cleanData()
main()
