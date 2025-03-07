import requests
from bs4 import BeautifulSoup

# Hedef URL
url = "https://www.transfermarkt.com.tr/besiktas-jk/kader/verein/114/plus/0/galerie/0?saison_id=2024"
headers = {"User-Agent": "Mozilla/5.0"}

# Sayfa içeriğini al
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Oyuncu satırlarını bul
player_rows = soup.find_all("tr", class_=["odd", "even"])

for row in player_rows:
    try:
        # Forma numarası
        shirt_number_tag = row.find("div", class_="rn_nummer") or row.find("td", class_="rn_nummer")
        shirt_number = shirt_number_tag.text.strip() if shirt_number_tag else "N/A"

        # İsim (a etiketi içinde)
        name_tag = row.find("a", href=True)  # a etiketini href'ye göre buluyoruz
        if name_tag:
            name = name_tag.text.strip()  # Oyuncu ismi
        else:
            name = "N/A"

        # Mevki
        position_tag = row.find_all("td")[4] if len(row.find_all("td")) > 4 else None
        position = position_tag.text.strip() if position_tag else "N/A"

        # Yaş
        age_tag = row.find_all("td")[5] if len(row.find_all("td")) > 5 else None
        age = age_tag.text.strip() if age_tag else "N/A"

        # Uyruk
        nationality_tag = row.find("img", class_="flaggenrahmen")
        nationality = nationality_tag["title"].strip() if nationality_tag else "N/A"

        # Piyasa değeri
        market_value_tag = row.find_all("td")[-1] if row.find_all("td") else None
        market_value = market_value_tag.text.strip() if market_value_tag else "N/A"

        print(f"Forma No: {shirt_number}, İsim: {name}, Mevki: {position}, Yaş: {age}, Uyruk: {nationality}, Piyasa Değeri: {market_value}")

    except Exception as e:
        print(f"Hata oluştu: {e}")
