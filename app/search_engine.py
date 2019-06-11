import json
from nltk.stem import WordNetLemmatizer

# 清洗word
def clear_word(word):
    return word.strip(",|.|?|!|\'|\"|@|#|$|%|^|&|*|(|)|_|-|=|+|:|;|<|>|/|\\|`|~")

# |1|2|3|4|5|6|7|8|9|0

# 将单词中的字符都变成小写
def sentence_lower(word):
    return word.lower()

# 单词提取原型
def lemmazitation(word):
    wnl = WordNetLemmatizer()
    return wnl.lemmatize(word)

def standard_word(word):
    dword = clear_word(word)
    dword = sentence_lower(dword)
    dword = lemmazitation(dword)
    return dword

def search_kws(keywords):
    with open("record.json",'r') as load_f:
        record = json.load(load_f)

        keys = keywords.strip().split(" ")
        result = []

        if len(keys) == 1:
            print(keys)
            keys[0] = standard_word(keys[0])
            try:
                all_position = record[keys[0]]
            except:
                return result

            already_in_page = []
            for pos_item in all_position:
                try:
                    page_number = pos_item.split(':')[0]
                    if page_number not in already_in_page:
                        already_in_page.append(page_number)
                        line_number = int(pos_item.split(':')[1])

                        spe_new_json = open("./news_json/{}.json".format(page_number),"r")
                        new = json.load(spe_new_json)

                        new_dict = {}
                        new_dict['title'] = new['title']
                        print(line_number,new['content'])
                        new_dict['Lcontent'] = new['content'][line_number-1]
                        new_dict['page_number'] = page_number
                        new_dict['tf'] = calc_tf(keys[0],page_number)

                        result.append(new_dict)
                except:
                    pass

        elif len(keys) > 1:
            with open("idf.json", 'r') as load_f:
                idf_dict = json.load(load_f)

            page_list = []
            ti_result = {}
            already_in_page = []
            real_keys = []
            
            tempkeys = []
            for key in keys:
                item = standard_word(key)
                tempkeys.append(item)
            keys = tempkeys
            
            for key in keys:
                if key in record.keys():
                    real_keys.append(key)

            if len(real_keys) == 0:
                return result

            for key in real_keys:
                all_position = record[key]
                for item in all_position:
                    page_number = item.split(":")[0]
                    if page_number not in already_in_page:
                        page_list.append(item)
                        already_in_page.append(page_number)

            for page in page_list:
                try:
                    page_number = page.split(":")[0]
                    tf_idf = 0
                    for key in keys:
                        tf = calc_tf(key,page_number)
                        idf = idf = idf_dict.get(key.strip())
                        tf_idf += tf * idf
                    ti_result[page] = tf_idf
                except:
                    pass

            new_ti_result = sorted(ti_result.items(), key=lambda d: d[1], reverse=True)

            for item in new_ti_result:
                try:
                    print(item)
                    page_number = item[0].split(":")[0]
                    line_number = int(item[0].split(':')[1])
                    spe_new_json = open("./news_json/{}.json".format(page_number), "r")
                    new = json.load(spe_new_json)

                    new_dict = {}
                    new_dict['title'] = new['title']
                    print(line_number, new['content'])
                    new_dict['Lcontent'] = new['content'][line_number - 1]
                    new_dict['page_number'] = page_number
                    new_dict['tf'] = item[1]

                    result.append(new_dict)
                except:
                    pass





    new_result = sorted(result, key=lambda e: e.__getitem__('tf'),reverse=True)
    print(new_result)
    return new_result

def calc_tf(word_name,page_number):
    pwc_json = open("nwcount.json","r") #wenzhangzongcishu
    wc_json = open("count.json", "r")   #dancichuxiangcishu
    wc_dict = json.load(wc_json)
    pwc_dict = json.load(pwc_json)

    wc = wc_dict[word_name].get(str(page_number))
    if wc == None:
        tf = 0
        return tf

    pwc = pwc_dict[str(page_number)]
    tf = wc/pwc
    return tf

def single_rearrange(old_result):
    pass


