import json
import math

news_amount = 1156

def calc_idf():
    file = open("count.json", 'r')
    wfile = open("idf.json","w")
    idf_dict = {}
    words_json = json.load(file)
    for key in words_json:
        idf = math.log((news_amount/len(words_json[key])),10)
        idf_dict[key] = idf

    print(idf_dict)
    json.dump(idf_dict,wfile)

if __name__ == '__main__':
    calc_idf()


