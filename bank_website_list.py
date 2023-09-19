import requests, csv
from bs4 import BeautifulSoup

URL = "https://www.rbi.org.in/scripts/banklinks.aspx"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the table rows with bank names and website links
tables = soup.find_all("table")

# Create a list to store the bank names and website links
bank_data = []
bank_type_list = []
bank_type_code_dict = {
                        'Private Sector Banks': 'PVTBANK',
                        'Local Area Banks (LAB)': 'LCLBANK',
                        'Small Finance Banks (SFB)': 'SMLFINBANK',
                        'Payments Banks (PB)': 'PYMBANK',
                        'Public Sector Banks': 'PBCSECBANK',
                        'Financial Institutions': 'FININS',
                        'Regional Rural Banks': "RGNRRLBANK",
                        'foreign banks': 'FORBANK'}

for table in tables:
    table_rows = table.find_all('tr')

    # Iterate over the table rows and extract the bank names and website links
    for table_row in table_rows:
        table_row_th = table_row.find('th', {'colspan': '2', 'align': 'left'})
        if table_row_th:
            bank_type = table_row_th.get_text(strip=True).replace("    ", " ").replace("List of ", "").replace("in India", "").replace("  ", " ").replace(" having banking presence", "").strip()
            bank_type_list.append(bank_type)
       
        try:
            bank_name = table_row.find("a").text.replace("    ", " ")
            website_link = table_row.find("a")["href"]
            bank_type = bank_type_list[-1]
            bank_code = bank_type_code_dict.get(bank_type)
            bank_data.append((bank_name, website_link, bank_type, bank_code))
            
        except AttributeError:
            pass

# Define the CSV file name
csv_filename = "bank_data.csv"

# Write the data to a CSV file
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter="|")
    
    # Write the header row
    writer.writerow(["Bank Name", "Website Link", "Bank Type", "Bank Type Code"])
    
    # Write the data rows
    for bank_name, website_link, bank_type, bank_code in bank_data:
        writer.writerow([bank_name, website_link, bank_type, bank_code])

print(f"Data has been saved to {csv_filename}")

