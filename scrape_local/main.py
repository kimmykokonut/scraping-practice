from bs4 import BeautifulSoup
#import bs, specify html file, 'read'
with open('home.html', 'r') as html_file:
  #save scraped content as variable content
  content = html_file.read()
  #print(content)
  #bs will prettify html
  soup = BeautifulSoup(content, 'lxml')
  #print(soup.prettify())
  ### finds all h5 tags
  # courses_html_tags = soup.find_all('h5')
  # #returns all h5 tags
  # #print(courses_html_tags)

  # for course in courses_html_tags:
  #   print(course.text)

  #now find and return specific button text inside a div
  course_cards = soup.find_all('div', class_='card')

  for course in course_cards:
    #print(course.h5)
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]
    #print(course_name)
    #print(course_price)

    print(f'{course_name} costs {course_price}')