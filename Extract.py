import requests
from bs4 import BeautifulSoup

URL = 'https://www.marocannonces.com/categorie/309/Emploi/Offres-emploi/2.html'
page = requests.get(URL)

#--------------------------print html code-------------------------------
soup = BeautifulSoup(page.content,"html.parser")

#--------print only elements which have as id='ResultsContainer'---------
results = soup.find(id='content')

#in results we search a section elemnts which have as className='card-content'
job_elems = results.find_all('ul', class_='cars-list')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print("*******************************")
