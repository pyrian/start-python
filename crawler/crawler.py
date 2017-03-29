import requests
from bs4 import BeautifulSoup


def spy(url, to_page=0):
    result = []

    for page in range(1, to_page+1):
        r = requests.get(url, params={"page": page})

        soup = BeautifulSoup(r.text, "lxml")
        tr_list = soup.select("table tr")
        tr_list = tr_list[3:]

        for tr in tr_list:
            title = tr.select_one(".title a").text
            rate = float(tr.select_one("td .rating_type strong").text)
            href = tr.select_one(".title a").get("href")
            result.append(Webtoon(title, rate, href))

    return result


def get_best_list(webtoons, count=5):
    result = sorted(webtoons, key=lambda webtoon: webtoon.rate, reverse=True)

    return result[:count]


class Webtoon:
    def __init__(self, title, rate, href):
        self.title = title
        self.rate = rate
        self.href = href

    def print(self):
        print("title=%s, rate=%s, href=%s" % (self.title, self.rate, self.href))


if __name__ == '__main__':
    crawled_list = spy("http://comic.naver.com/webtoon/list.nhn?titleId=20853", 5)

    for w in get_best_list(crawled_list):
        w.print()
