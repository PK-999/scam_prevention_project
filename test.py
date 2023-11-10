import requests
from bs4 import BeautifulSoup

# Define the search query
search_query = "Axis Bank Ltd."

# Create the URL for the Google Play Store search results page
url = f"https://play.google.com/store/search?q={search_query}&c=apps"

# Send an HTTP GET request to the URL
response = requests.get(url)
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    with open(f'{search_query}.html', mode="w", newline="", encoding="utf-8") as file:
        file.write(str(soup))
    
    # Find the elements that contain the app names and links
    app_elements = soup.find_all("div", class_="VfPpkd-aGsRMb")
    print(app_elements)
    
    if app_elements:
        # Iterate through the app elements and print the names and links
        for app_element in app_elements:
            app_name = app_element.find("span", class_="DdYX5").text
            app_link = "https://play.google.com" + app_element.find("a", class_="Si6A0c Gy4nib")["href"]
            app_author = app_element.find("span", class_="wMUdtb")
            
            print(f"App Name: {app_name}")
            print(f"App Link: {app_link}")
            print(f"App Author: {app_author}")
            print("\n")
    else:
        print("No apps found for the given search query.")
else:
    print("Failed to retrieve the search results. Check your internet connection.")

