import requests
from bs4 import BeautifulSoup

def get_page_rankings(page_num):
    url = f'https://www.shanghairanking.cn/rankings/bcur/2023{page_num}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    rankings = []
    rows = soup.select('tbody tr')
    for row in rows:
        rank = row.select_one('td.rank').text.strip()
        school = row.select_one('td.university').text.strip()
        score = row.select_one('td.score').text.strip()
        rankings.append({'rank': rank, 'school': school, 'score': score})
    return rankings

def get_all_rankings():
    all_rankings = []
    for page_num in range(1, 11):
        page_rankings = get_page_rankings(page_num)
        all_rankings.extend(page_rankings)
    return all_rankings

if __name__ == '__main__':
    all_rankings = get_all_rankings()
    for ranking in all_rankings:
        print(f"排名: {ranking['rank']}, 学校: {ranking['school']}, 总分: {ranking['score']}")
