import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_titles = []
company_names = []
locations = []
links = []
job_skills = []
salaries = []  # غيرت الاسم إلى salaries (جمع)

# جلب الصفحة الرئيسية
result = requests.get("https://wuzzuf.net/search/jobs?q=python&a=hpb")
soup = BeautifulSoup(result.content, "lxml")

# استخراج العناصر
job_titles_a = soup.find_all("h2", {"class": "css-193uk2c"})
company_names_a = soup.find_all("a", {"class": "css-ipsyv7"})
locations_a = soup.find_all("span", {"class": "css-16x61xq"})
job_skills_a = soup.find_all("div", {"class": "css-pkv5jc"})

# استخراج البيانات الأساسية
for i in range(len(job_titles_a)):
    job_titles.append(job_titles_a[i].text.strip())
    
    # استخراج الرابط (تأكد من إضافة https://wuzzuf.net)
    link = "https://wuzzuf.net" + job_titles_a[i].find("a").attrs['href']
    links.append(link)
    
    company_names.append(company_names_a[i].text.strip())
    locations.append(locations_a[i].text.strip())
    job_skills.append(job_skills_a[i].text.strip())

# جلب الرواتب
for link in links:
    try:
        result = requests.get(link)
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        salary_element = soup.find("span", {"class": "css-iu2m7n"})
        
        # استخراج النص إذا وجد العنصر
        if salary_element:
            salaries.append(salary_element.text.strip())
        else:
            salaries.append("غير متوفر")
            
    except Exception as e:
    
        salaries.append("خطأ في الجلب")

# التأكد من أن جميع القوائم بنفس الطول

# حفظ في CSV
file_list = [job_titles, job_skills, company_names, locations, links, salaries]
exported = zip_longest(*file_list)

with open(r"C:/Users/hp/Desktop/cors/mosa/New folder/jobs.csv", "w", newline='', encoding='utf-8') as myjob:
    wr = csv.writer(myjob)
    wr.writerow(["Job Title", "Skills", "Company", "Location", "Link", "Salary"])
    
    for row in exported:
        # تنظيف البيانات قبل الكتابة
        cleaned_row = []
        for item in row:
            if item:
                cleaned_row.append(str(item).replace('\n', ' ').strip())
            else:
                cleaned_row.append("")
        wr.writerow(cleaned_row)

