import re
import requests
from typing import List, Optional
IPV4_REGEX = r"""\b(?:
    (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}
    (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b""".strip()
def find_ipv4_addresses(text: str) -> List[str]:
    return re.findall(IPV4_REGEX, text, re.VERBOSE)
def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
def fetch_web_content(url: str) -> Optional[str]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при запросе к URL: {e}")
        return None

if __name__ == "__main__":
    # Пользовательский ввод
    user_input = input("Введите текст или путь к файлу: ")
    if user_input.startswith("http"):
        content = fetch_web_content(user_input)
    else:
        try:
            content = read_file(user_input)
        except FileNotFoundError:
            content = user_input

    if content:
        ipv4_addresses = find_ipv4_addresses(content)
        print("Найденные IPv4-адреса:")
        for ip in ipv4_addresses:
            print(ip)



