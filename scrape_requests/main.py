import time
from bs4 import BeautifulSoup
import requests
# Youtube tutorial scraping: https://www.timesjobs.com/

#get user input
print('Enter skill you do not have:')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
  # scrape
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
  #print(html_text)

  # make instance of BS
  soup = BeautifulSoup(html_text, 'lxml')

  # put scrape in variable
  jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') #first match if not find_all()
  #print(job)
  #index as counter, for file 
  for index, job in enumerate(jobs):
  #for job in jobs:
    post_date = job.find('span', class_="sim-posted").span.text
    if 'few' in post_date:
      company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
      # skills is long strind div by , filter inside this string
      skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')    
      more_info = job.header.h2.a['href']
      #print(company_name) V1
      #print(skills)
      # print(f''' #V2 issue: includes indentation with multi-line
      #     Company Name: {company_name}
      #     Required Skills: {skills}
      #     Date Posted: {post_date}
      #     ''')
      # print('')
      if unfamiliar_skill not in skills:
        with open(f'posts/{index}.txt', 'w') as f:
          #change print(term) to f.write for txt file
          f.write(f"Company Name: {company_name.strip()} \n")
          f.write(f"Required Skills: {skills.strip()} \n")
          f.write(f"Date Posted: {post_date.strip()} \n")
          f.write(f"More info: {more_info}")
        print(f'File saved: {index}')

if __name__ == '__main__':
  while True:
    find_jobs()
    time_wait = 10
    print(f'Waiting {time_wait} minutes...')
    time.sleep(time_wait * 60) #run ev 10 min
