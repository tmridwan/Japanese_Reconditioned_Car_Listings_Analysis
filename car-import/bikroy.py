from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

columns = ["Company", "Model", "Year", "Color", "Engine_Capacity", "Fuel_Type", "Mileage", "Auction_Grade", "Price"]
def details(row):
    cells = row.find_elements(By.TAG_NAME, 'td')
    details = [cell.text.strip() for cell in cells if cell.text.strip()]
    contents = {}
    if len(cells) < 12:
        print(f"Skipping row due to insufficient data (length {len(details)}): {details}")
        return contents
    try:
        contents["Company"] = details[1].split('\n')[0]
        contents["Model"] = details[1].split('\n')[1]
        contents["Year"] = details[4]
        contents["Color"] = details[5] if details[5].isalpha() else "Unknown"
        contents["Engine_Capacity"] = details[6] if details[6].isdigit() else "Unknown"
        contents["Fuel_Type"] = details[7]
        contents["Mileage"] = details[8] if details[8].isdigit() else "Unknown"
        contents["Auction_Grade"] = details[9]
        contents["Price"] = details[10].split()[0].replace(',', '') if details[10] and len(details[10].split()) > 0 and details[10].split()[0].replace(',', '').isdigit() else "Unknown"
    except IndexError as e:
        print(f"Skipping row due to index error: {details} (Error: {e})")
        return contents
    return contents
def main():
    webdriver_path = "venv/Scripts/chromedriver.exe"
    row_contents = []
    for i in range(1, 21):
        service = Service(webdriver_path)
        driver = webdriver.Chrome(service=service)
        url = f"https://gari-import.com.bd/stock-list?page={i}"
        driver.get(url)
        table = driver.find_element(By.CLASS_NAME, 'table')
        tbody = table.find_elements(By.TAG_NAME, 'tbody')
        for idx, row in enumerate(tbody):
            data = details(row)
            if data:
                row_contents.append(data)
        driver.close()

    df = pd.DataFrame(data = row_contents, columns= columns)
    df.to_csv("gari-import.csv", index = False)
    print(len(row_contents))
    return
if __name__ == "__main__":
    main()