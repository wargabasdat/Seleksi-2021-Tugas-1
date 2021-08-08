import re


def filterLastUpdated(old_up):
    lu = str(old_up)
    if ("kemarin" in lu):
        return [1]
    elif ("hari" in lu):
        return [int(lu.split()[0])]
    elif ("bulan" in lu):
        return [int(lu.split()[0]) * 30]
    else:
        return [None]


def filterExp(old_exp):
    # Handling experience info (separate them into min exp and optimal exp)
    exp = str(old_exp)
    if ("Kurang" in exp):  # Case of less than 1 year exp needed
        return [0, 1]
    elif (exp == ""):  # Case of no experience needed, or no info
        return [None, None]
    else:  # Case of certain range of experience is needed
        return [int(s) for s in re.findall(r'\d+', exp)]


def filterSalary(old_salary):
    sal = str(old_salary)
    if ("Login" in sal):
        return [None, None, None]  # Currency, start_sal, end_sal
    else:
        sal_split = sal.split()
        curr = sal_split[0]
        if (len(sal_split) < 4):
            return [curr, sal_split[1], None]
        else:
            return [curr, int(sal_split[1].replace('.', '')), int(sal_split[3].replace('.', '').replace(',', ''))]


def filterInfo(old_info):
    # Separate info into location, salary, and experience (still in string form)
    info = old_info.find_all(
        'div', attrs={"class": re.compile(r'(OpportunityInfo-sc)')})
    if (len(info) > 2):  # Case of full info
        loc = info[0].text.strip()
        sal = filterSalary(info[1].text.strip())
        temp = filterExp(info[2].text.strip())
    elif (len(info) == 2):  # Case of missing 1 info
        loc = info[0].text.strip()
        sal = [None, None, None]
        if ("tahun" in info[1].text.strip()):  # Case of no salary info
            temp = filterExp(info[1].text.strip())
        elif (info[1].text.strip() == ""):  # Case of no both info but counted as 2
            temp = [None, None]
        else:   # Case of no experience info
            sal = filterSalary(info[1].text.strip())
            temp = [None, None]
    elif (len(info) == 1):  # Case of no salary and experience info
        loc = info[0].text.strip()
        sal = [None, None, None]
        temp = [None, None]
    else:  # Case of no info at all
        return [None, None, None, None, None, None]
    return ([loc] + sal + temp)


def findJobTitle(jobs):
    return jobs.find('h3', attrs={"class": re.compile(r'(JobTitle)')}).text


def findJobCompany(jobs):
    return jobs.find('span', attrs={"class": re.compile(r'(CompanyLinkContainer)')}).text.strip()


def findJobInfo(jobs):
    return jobs.find('div', attrs={"class": re.compile(r'(OpportunityInfoContainer)')})


def findJobLastUpdated(jobs):
    return jobs.find('span', attrs={"class": re.compile(r'(UpdatedAtMessage)')}).text.strip()[11:]


def findJobApplicantCount(jobs):
    return jobs.find('div', attrs={"class": re.compile(r'(ApplicantCount)')})
