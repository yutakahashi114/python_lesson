import urllib.request
from bs4 import BeautifulSoup
from urllib.error import URLError
import re

class Scraper:
    def scrape(self, url):
        headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        # リクエストを設定
        encode_url = urllib.parse.quote(url, safe='/:?+=&')
        request = urllib.request.Request(url=encode_url, headers=headers)
        # レスポンスを取得
        response = urllib.request.urlopen(request)
        # HTMLを取得
        html = response.read()
        # BeautifulSoupに読み込ませる
        parser = "html.parser"
        soup = BeautifulSoup(html, parser)

        # 検索結果が存在するか確認
        if not self.isExistSearchResult(soup):
            # なければ空のリストを返却
            return []
        # 検索結果を取得
        return self.getSearchResult(soup)

    # 検索結果が存在するか確認
    def isExistSearchResult(self, soup):
        topstuff = soup.find(id="topstuff")
        print(topstuff)
        message = topstuff.select('.e.obp')
        print(message)
        return len(message) == 0

    # 検索結果を取得
    def getSearchResult(self, soup):
        search_result = soup.find_all("h3", class_="r dO0Ag")
        print(search_result)
        result_list = []
        for tag in search_result:
            url = tag.find("a").get("href")
            title = tag.find("a").string
            if url is None or title is None:
                continue
            result = {
                "url": url,
                "title": title
            }
            result_list.append(result)
        return result_list

    def getPageBody(self, url):
        headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        # リクエストを設定
        request = urllib.request.Request(url=url, headers=headers)
        # レスポンスを取得
        # response = urllib.request.urlopen(request)
        try:
            response = urllib.request.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            return ""
        else:
            # HTMLを取得
            html = response.read()
            # BeautifulSoupに読み込ませる
            parser = "html.parser"
            soup = BeautifulSoup(html, parser)
            body = soup.find("body")
            if body is None:
                return ""
            return body.text

    def getPageTitle(self, url):
        headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        # リクエストを設定
        request = urllib.request.Request(url=url, headers=headers)
        # レスポンスを取得
        # response = urllib.request.urlopen(request)
        try:
            response = urllib.request.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            return ""
        else:
            # HTMLを取得
            html = response.read()
            # BeautifulSoupに読み込ませる
            parser = "html.parser"
            soup = BeautifulSoup(html, parser)
            result_title = ''
            titles = soup.find_all("title")
            for title in titles:
                result_title += title.text + ' '
            h_ones = soup.find_all("h1")
            for h_one in h_ones:
                result_title += h_one.text + ' '
            return result_title

    def get30Body(self, url, term):
        headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        # リクエストを設定
        request = urllib.request.Request(url=url, headers=headers)
        # レスポンスを取得
        # response = urllib.request.urlopen(request)
        try:
            response = urllib.request.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            return ""
        else:
            # HTMLを取得
            html = response.read()
            # BeautifulSoupに読み込ませる
            parser = "html.parser"
            soup = BeautifulSoup(html, parser)
            body = soup.find("body")
            if body is None:
                return ""
            r = re.compile("([\s\S]{30})" + term + "([\s\S]{30})")
            match = r.findall(body.text)
            result = ''
            for value in match:
                result += value[0] + ' ' + value[1] + ' '
            print(result)
            return result
