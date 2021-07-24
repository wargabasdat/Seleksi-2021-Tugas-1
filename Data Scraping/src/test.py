from base64 import encode
from bs4 import BeautifulSoup
import re


def parsehtml():
    with open('test.html', 'r', encoding='utf-8') as html_file:
        content = html_file.read()
        old_info = BeautifulSoup(content, 'lxml')
        info = old_info.find_all(
            'div', attrs={"class": re.compile(r'(OpportunityInfo-sc)')})

        if (len(info) > 2):
            loc = info[0].text.strip()
            sal = info[1].text.strip()
            exp = info[2].text.strip()
        elif (len(info) == 2):
            loc = info[0].text.strip()
            if ("tahun" in info[1].text.strip()):
                sal = None
                exp = info[1].text.strip()
            else:
                sal = info[1].text.strip()
                exp = None
        else:
            loc = info[0].text.strip()
            sal = None
            exp = None
        return loc, sal, exp


exp = "5 – 10 tahun"


def test(exp):
    temp = [int(s) for s in re.findall(r'\d+', exp)]
    return temp


a = test(exp)
print(a)
