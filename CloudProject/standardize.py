import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
import json
import re

def Get_All_News():
    path = "./news_json/"
    news_list = os.listdir(path)
    return news_list

# 清洗word
def clear_word(word):
    return word.strip(",|.|?|!|\'|\"|@|#|$|%|^|&|*|(|)|_|-|=|+|:|;|<|>|/|\\|`|~")

# |1|2|3|4|5|6|7|8|9|0

# 将单词中的字符都变成小写
def sentence_lower(word):
    return word.lower()

# 判断是否为停用词
def is_stop_word(word):
    stop = set(stopwords.words('english'))
    ban_list = ["co","ltd"]
    if str(word) in stop or str(word) in ban_list or str(word).strip() == "":
        return 1
    else:
        return 0

# 单词提取原型
def lemmazitation(word):
    wnl = WordNetLemmatizer()
    return wnl.lemmatize(word)

#---------------------------------------------------------------------------------------------------------
# 标准化文本
def standard_content(page_number,content):
    result = []
    line_index = 1
    for line in content:
        word_list = line.strip().split(" ")

        for word in word_list:
            print(word)
            dword = clear_word(word)
            print(dword)
            dword = sentence_lower(dword)
            print(dword)
            if is_stop_word(dword) == 0:
                dword = lemmazitation(dword)
                print(dword)
                insert_word = dword + "," + str(page_number) + ":" + str(line_index)
                result.append(insert_word)
            else:
                pass
        line_index += 1
    return result

#---------------------------------------------------------------------------------------------------------
def main():
    news_list = Get_All_News()
    news_index = 1
    write_file = open("./result/res.txt","w",encoding="utf-8")
    for news in news_list:
        file = open("./news_json/"+news,'r')
        passage = json.load(file)
        title = passage['title']
        time_author = passage['time_author']
        content = passage['content']

        page_number = news.split(".")[0]

        passage_result = standard_content(page_number,content)
        sentence = ""
        for word_item in passage_result:
            sentence += word_item
            sentence += ";"

        print(sentence)
        write_file.write(sentence+"\n")
        news_index += 1

if __name__ == '__main__':
    # main()
    print(set(stopwords.words('english')))
    sentence = ["Raptors will win the championship, Curry will go home"]
    standard_content(1, sentence)

