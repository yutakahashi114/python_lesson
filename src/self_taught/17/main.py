import re
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - -let 's do more of those!"""

matches = re.findall("^If", zen, re.MULTILINE)

print(matches)

string = "Two too."
matches = re.findall("t[wo]o", string, re.IGNORECASE)
print(matches)

line = "123 hi 34 hello."
matches = re.findall("\d", line, re.IGNORECASE)
print(matches)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

text = """キリンは昔から__複数名詞__の興味の対象でした。
キリンは__複数名詞__の中で一番背が高いですが、
科学者たちはそのような長い__体の一部__をどうやって獲得したのか説明できません。
キリンの身長は__数値__ __単位__ 近くあり、
その高さの殆どは足と__体の一部__によるものです。"""

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{0} を入力：".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Invalid input")

# mad_libs(text)

line = "I love $"
m = re.findall("\$", line, re.IGNORECASE)
print(m)
