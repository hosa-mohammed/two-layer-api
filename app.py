import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_titles =[]
company_names = []
locations = []
links=[]
jop_skills = []
salary = []


result = requests.get("https://wuzzuf.net/search/jobs?q=python&a=hpb")

src = result.content
#print (src)

soup = BeautifulSoup(src, "lxml")

jop_titles_a = soup.find_all("h2",{"class":"css-193uk2c"})
#print(jop_titles)
company_names_a = soup.find_all("a", {"class":"css-ipsyv7"})
#print(company_names)
locations_a = soup.find_all("span",{"class":"css-16x61xq"})
#print(locations)
jop_skills_a = soup.find_all("div",{"class":"css-pkv5jc"})
#print(jop_skills)



for i in range(len(jop_titles_a)):
    jop_titles.append(jop_titles_a[i].text)
    links.append("https://wuzzuf.net" + jop_titles_a[i].find("a").attrs['href'])
    company_names.append(company_names_a[i].text)
    locations.append(locations_a[i].text)
    jop_skills.append(jop_skills_a[i].text)



for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")

    salaries = soup.find("div", {"class": "css-1lqavbg"})
    
    if salaries:
        salary.append(salaries.text.strip())
    else:
        salary.append("Not Mentioned")


file_list = [jop_titles, jop_skills, company_names, locations, links, salary]
exported = zip_longest(*file_list )
with open(r"C:/Users/hp/Desktop/cors/mosa/New folder/jobs.csv", "w", encoding="utf-8", newline="") as myjop:
    wr= csv.writer(myjop)
    wr.writerow(["jop title","skills", "company", "locations", "LINKES", "salaries"]) 

    for row in exported:
        wr.writerow(row)
        





