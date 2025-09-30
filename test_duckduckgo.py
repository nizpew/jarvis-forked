# test_duckduckgo_search.py
import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    try:
        url = "https://html.duckduckgo.com/html/"
        params = {"q": query}
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.post(url, data=params, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"Erro na pesquisa: status {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("a", {"class": "result__a"}, limit=3)  # pega os 3 primeiros resultados
        if not results:
            return "Nenhum resultado encontrado."

        output = "Resultados do DuckDuckGo:\n"
        for idx, link in enumerate(results, start=1):
            title = link.get_text()
            href = link.get("href")
            output += f"{idx}. {title} -> {href}\n"
        return output

    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar no DuckDuckGo: {e}"

if __name__ == "__main__":
    query = input("Digite o que deseja pesquisar no DuckDuckGo: ")
    print(duckduckgo_search(query))

