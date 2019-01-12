from Url import Url
from Scraper import Scraper
from SearchList import SearchList
from time import sleep
import csv
import random

if __name__ == "__main__":
    # 検索条件
    search_list = SearchList()
    category_list = search_list.getCategoryList()
    term_list = search_list.getTermList()
    exclusion_list = search_list.getExclusionList()

    url = Url()
    scraper = Scraper()

    with open('test.csv', 'w', encoding='CP932', errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow([ "カテゴリー", "用語", "URL", "タイトル" ])
        # for category in category_list:
        for term in term_list:
            # 検索するurlを取得
            search_url = url.getUrl(term, exclusion_list)
            print(search_url)
            # 検索結果を取得
            search_result = scraper.scrape(search_url)
            sleep(2)
            # sleep(random.randrange(5, 10))
            add_result = [[] for i in range(len(category_list))]

            for value in search_result:
                get_url = value['url']
                print("url",get_url)
                body = scraper.get30Body(get_url, term)
                # body = scraper.getPageTitle(get_url)
                # body = scraper.getPageBody(get_url)
                sleep(2)

                # print(body)
                for index, category in enumerate(category_list):
                    if category in body:
                        print([category, term, value['url'], value['title']])
                        add_list = [category, term, value['url'], value['title']]
                        add_result[index].append(add_list)

            # CSVファイルに出力
            for results in add_result:
                for result in results:
                    writer.writerow(result)
            print(add_result)
