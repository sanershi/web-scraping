import requests
from bs4 import BeautifulSoup
import time

def get_links_from_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        "Content-Type": "text/html; charset=UTF-8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": "__Secure-ENID=14.SE=mFdiWhSldkn-ZzPEtey1FJjPApTUluBSfJcYK2VnzSmEQTKumMywxK3G1HFVP5GOS_WghlKG4UKHbztfED2EQJzt9RrmcJU_YuG7f9DXOehOToqFtrLMR0L1Nr3KbgvI8MKTL2HQraJiKF8LHCBHbe1iSo8wN1aJlv72dXsaG_H6y7nRDCY8w_IODq9NWCe0s_L7it9CrkvuVlB41XEOAGc1zGkcvzyiQLkTf3PSs72JBFKDLgpfJiGKmMDtf9YMLB48; OTZ=7156781_44_48_123900_44_436380; SEARCH_SAMESITE=CgQIg5kB; OGPC=19022552-1:19024362-1:; SID=aQjMKwXEcphjA1aEo6nZiqcKjRsw98snl-V9y0h3EFFvnPmjOxk3H4aeAguV-7vTzOMk4w.; __Secure-1PSID=aQjMKwXEcphjA1aEo6nZiqcKjRsw98snl-V9y0h3EFFvnPmjeXG8RoL9s9q03-jFWoPDpg.; __Secure-3PSID=aQjMKwXEcphjA1aEo6nZiqcKjRsw98snl-V9y0h3EFFvnPmjaEkUSYXlPVC3Z2hrY95YtQ.; HSID=ABjAlmZxNc3m9tsWm; SSID=A8fwxrxmwxqBZos7U; APISID=6noJSFQIY_T2-Rko/A5MtYIctrnqSdD7rI; SAPISID=jIFXvtEz5bHuWd2R/AYv2-BpknSZdh8am4; __Secure-1PAPISID=jIFXvtEz5bHuWd2R/AYv2-BpknSZdh8am4; __Secure-3PAPISID=jIFXvtEz5bHuWd2R/AYv2-BpknSZdh8am4; AEC=Ad49MVFHDOL_-mrSBhwU5lwP5bXwr9QfrjoTGs1jBprbPISnuLmH6CS9Cw; NID=511=CO38ovLCcAW_RHeLhviNb4BhHvtxi-PjWWDc_qJeDPmcwdVD6ZLn302ptIpQE7Pg0kZP3WZeXbc7fnio4gxdTvBqdK3IerUUXIbbeLgezp1IT5RZTAhtQvhk1aFftBtdv3TvWvLI-xvX4QDb_sJZT-dpYdQXWanSlpg521jRzMvlC92T3wSyKjMQQ9jB-UOsYJp3pqsuSFMtnzlVMFlPkC0f8Fy4YCavpbMwqATabBvYodsM5FFJai0wOjX7m469eRXOI8oNTOCtWTLiKuJpYQ1nmkaf8rAfqMYbMWGPQWJ2SBtPl5SspvKcIgxwogRde4HKLZ5p23iP76eKpnH1KgidnXXYYXPwhxkNF1vRAWw42NO1cbNY; __Secure-1PSIDTS=sidts-CjEBSAxbGWiRKyDV_m32frvl0hxkqcfWSTnZt0ZOH5435fih6LJ3BR_GXRmGwWFXiZ0NEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGWiRKyDV_m32frvl0hxkqcfWSTnZt0ZOH5435fih6LJ3BR_GXRmGwWFXiZ0NEAA; GOOGLE_ABUSE_EXEMPTION=ID=754220912f802d05:TM=1693531623:C=r:IP=176.240.109.81-:S=dPEh-ivchGJPGbboY-hqHbA; 1P_JAR=2023-09-01-01; DV=45acoWmBQHtmIBy4P1MyROuwNqflpFjs8hEqnbr1iAEAAAAifm2YC1-e7QAAACiFq6AsToMGPAAAAFqMijrty6F2FAAAAIc7I0Uz1kFWwQkBAA; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjkzNTMxNjY2MzUyMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDQwOTgwMTcwNwogIGxvbmdpdHVkZV9lNzogMjc1MjIwNTQ3Cn0KcmFkaXVzOiAzMjk5Nzk3Ljg1NjcyODk0MjYKcHJvdmVuYW5jZTogNgo=; SIDCC=APoG2W8OcL_Uhs_WgVhjX8f_Xdw8IALIR1y9cSYRkHk49saIMxdnM-_7LZ_3_1YGmBC6gjJdhvAS; __Secure-1PSIDCC=APoG2W-CJZmohEJDeaKfc9QJ3oY0OwRrkcc9Z4WfDt3vVfMIK3l0HrCEklD7SxUcPsvtovGZcLk; __Secure-3PSIDCC=APoG2W9bR_y4e3TFRrCJnq3xyqf_Fe6BJi70WxtLBbwjCmLjOc_9U7hMFfRIu7NuQ-OI0-jOcQ",
    }
    response = requests.Session().get(url, headers=headers)
    h = BeautifulSoup(response.text, 'html.parser')
    jscontroller_links = h.find_all('a', attrs={'jscontroller': 'M9mgyc'})
    return jscontroller_links

def filter_links(links):
    filtered_links = []
    for link in links:
        href = link.get('href')
        text = link.get_text()
        if "google" not in href and "github" not in href:
            filtered_links.append((href, text))
    return filtered_links

def save_links_to_file(links, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for index, (href, text) in enumerate(links, start=1):
            file.write(f"Link {index}:\n")
            file.write(f"Bağlantı: {href}\n")
            file.write(f"Metin: {text}\n")
            file.write("=" * 30 + "\n")

def save_links_file(links, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for index, (href, text) in enumerate(links, start=1):
            cleaned_href = href.replace('/login.php', '')
            file.write(f"{cleaned_href}\n")


def print_links(links):
    for index, (href, text) in enumerate(links, start=1):
        print(f"Link {index}:\n")
        print(f"Bağlantı: {href}\n")
        print(f"Metin: {text}\n")
        print("=" * 30 + "\n")

dork = 'inurl:com.tr'
base_url = f'https://www.google.com/search?q={dork}'
page_size = 10
total_pages = 3

all_links = []

for page in range(total_pages):
    start_index = page * page_size
    site_url = f"{base_url}&start={start_index}"
    page_links = get_links_from_page(site_url)
    filtered_page_links = filter_links(page_links)
    all_links.extend(filtered_page_links)

save_links_to_file(all_links, 'links.txt')
save_links_file(all_links, 'results.txt')
print_links(all_links)
print("Tüm linkler 'links.txt' dosyasına kaydedildi.")
