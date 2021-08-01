from base64 import encode
from bs4 import BeautifulSoup
import re


def parseExp(old_exp):
    exp = str(old_exp)
    if ("Kurang" in exp):
        return 0, 1
    else:
        temp = [int(s) for s in re.findall(r'\d+', exp)]
        return temp


def parsehtml():
    with open('test2.html', 'r', encoding='utf-8') as html_file:
        content = html_file.read()
        old_info = BeautifulSoup(content, 'lxml')
        info = old_info.find_all(
            'div', attrs={"class": re.compile(r'(OpportunityInfo-sc)')})
    if (len(info) > 2):
        loc = info[0].text.strip()
        sal = info[1].text.strip()
        temp = parseExp(info[2].text.strip())
    elif (len(info) == 2):
        loc = info[0].text.strip()
        if ("tahun" in info[1].text.strip()):
            sal = None
            temp = parseExp(info[1].text.strip())
        else:
            sal = info[1].text.strip()
            temp = [None, None]
    else:
        loc = info[0].text.strip()
        sal = None
        temp = [None, None]
    return ([loc, sal] + temp)


temp = parsehtml()
print(temp)
