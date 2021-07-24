from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json
import re

SCROLL = 3  # More than 10 will be very slow
URL = 'https://glints.com/id/opportunities/jobs/explore?country=ID&locationName=Indonesia&jobCategories=1&cities=28904'

# Get Page: encode HTML from url


def getPage(url):
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
    for i in range(1, SCROLL):  # Scroll X times
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)  # loading time for browser to load the url
        print(f'Progress: scrolled [{i}/{SCROLL}]')
    html_source = driver.page_source
    return html_source.encode('utf8')

# writeToFile: Write to json file format


def writeToFile(index, title, company, loc, sal, expm, expo, last_updated, appl):
    # Somehow exp is saved as "" and not null
    if (type(expm) == str and len(expm) == 0):
        expm = None
        expo = None
    d = {
        "title": title,
        "company": company,
        "location": loc,
        "estimate_salary": sal,
        "exp_min": expm,
        "exp_opt": expo,
        "last_updated": last_updated,
        "applicant": appl
    }
    json_object = json.dumps(d, indent=4, ensure_ascii=False)
    with open(f'../data/{index}_job.json', 'w', encoding='utf8') as f:
        f.write(json_object)


def parseExp(old_exp):
    exp = str(old_exp)
    if ("Kurang" in exp):
        return 0, 1
    else:
        temp = [int(s) for s in re.findall(r'\d+', exp)]
        # somehow temp[0] and temp[1] not working
        expm = temp[1:]
        expo = temp[:1]
        return expm, expo


# Separate info into location, salary, and experience (still in string form)


def parseInfo(old_info):
    info = old_info.find_all(
        'div', attrs={"class": re.compile(r'(OpportunityInfo-sc)')})
    if (len(info) > 2):
        loc = info[0].text.strip()
        sal = info[1].text.strip()
        expm, expo = parseExp(info[2].text.strip())
    elif (len(info) == 2):
        loc = info[0].text.strip()
        if ("tahun" in info[1].text.strip()):
            sal = None
            expm, expo = parseExp(info[1].text.strip())
        else:
            sal = info[1].text.strip()
            expm, expo = None
    else:
        loc = info[0].text.strip()
        sal = None
        expm, expo = None
    return loc, sal, expm, expo


html_text = getPage(URL)
soup = BeautifulSoup(html_text, 'lxml')
jobs_cards = soup.find_all(
    'div', attrs={"class": re.compile(r'(CompactJobCard-sc)')})
for index, jobs in enumerate(jobs_cards):
    # JOB TITLE #
    title = jobs.find(
        'h3', attrs={"class": re.compile(r'(JobTitle)')}).text
    # JOB COMPANY #
    company = jobs.find(
        'span', attrs={"class": re.compile(r'(CompanyLinkContainer)')}).text
    # JOB INFO # location, salary, experience
    info = jobs.find(
        'div', attrs={"class": re.compile(r'(OpportunityInfoContainer)')})
    loc, sal, expm, expo = parseInfo(info)
    # JOB LAST UPDATED #
    last_updated = jobs.find(
        'span', attrs={"class": re.compile(r'(UpdatedAtMessage)')}).text.strip()[11:]
    # JOB APPLICANT COUNT #
    appl = int(jobs.find(
        'div', attrs={"class": re.compile(r'(ApplicantCount)')}).text.split()[0])
    writeToFile(index, title, company, loc, sal,
                expm, expo, last_updated, appl)
    # print(title)
    # print(company)
    # print(loc)
    # print(sal)
    # print(expm)
    # print(expo)
    # print(last_updated)
    # print(appl)
    # print("=============")

print("FINISHED!")
