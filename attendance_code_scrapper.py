# Import Libraries
import requests
from bs4 import BeautifulSoup

# Website for attendance code
url = 'https://www.myskillsfuture.gov.sg/api/take-attendance/RA157867'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

head = soup.find_all('span')
try:
    body = head[-3].get_text().split()
    attendance_code = body[-1].strip(".")
    print(attendance_code)
except:
    print("No attendance code found")




