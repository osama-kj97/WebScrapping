# The course link is: https://www.youtube.com/watch?v=awoEELnQzVg

import requests
from bs4 import BeautifulSoup
import pandas as pd

# main_link = 'https://11001.portal.athenahealth.com/'

def get_patient_portal_name(clinic_id):
    response = requests.get(f'https://{clinic_id}.portal.athenahealth.com/')

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    h1ns = soup.find_all('h1')
    patient_portal_name = h1ns[-1].text.strip()

    return patient_portal_name

# response = requests.get(f'https://{13}.portal.athenahealth.com/')

# html = response.text

# soup = BeautifulSoup(html, 'html.parser')

# h1ns = soup.find_all('h1')
# print(h1ns)

master_list = []

for i in range(20):
    
    # My ifs 
    # if 'Sorry' not in get_patient_portal_name(i):
    #     if 'Payment Confirmation' not in get_patient_portal_name(i):
            data_dict = {}
            data_dict['clinic_id'] = i
            data_dict['clinic_name'] = get_patient_portal_name(i)
            master_list.append(data_dict)
    # print(get_patient_portal_name(i), ' ', i)
print("Done, man.")
print(master_list)

df = pd.DataFrame(master_list)
df.to_csv('clinic_data.csv', index=False)
