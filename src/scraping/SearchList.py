import csv

class SearchList:
    def __init__(self):
        self.file_name_list = {
            "category": "Category.csv",
            "term": "Term.csv",
            "exclusion": "Exclusion.csv"
        }
    def getCategoryList(self):
        return self.read_csv(self.getFilePath(self.file_name_list["category"]))

    def getTermList(self):
        return self.read_csv(self.getFilePath(self.file_name_list["term"]))

    def getExclusionList(self):
        return self.read_csv(self.getFilePath(self.file_name_list["exclusion"]))

    def getFilePath(self, file_name):
        return "Data/" + file_name

    def read_csv(self, file_name):
        data_list = []
        with open(file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                data_list.append(row[0])
        return data_list
