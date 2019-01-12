class Url:
    def __init__(self):
        self.search_engine = "https://www.google.co.jp/search"
        # キーワード以外の検索条件
        self.condition = {
            "num": "100",    # 表示件数（最大100件）
            "tbs": "qdr:d",  # 24時間以内
            "tbm": "nws"
        }

    def getUrl(self, term, exclusion_list):
        # 検索条件を追加
        url = self.search_engine + '?q="' + term + '"'
        # 除外検索条件を追加
        for exclusion in exclusion_list:
            url += '+-"' + exclusion + '"'
        # その他の検索条件を追加
        for key, value in self.condition.items():
            url += '&' + key + '=' + value
        return url
