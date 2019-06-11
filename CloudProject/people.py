from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time


def GetUrlList():
    url = "http://en.people.cn/202936/index{}.html"
    # 请求头部，不加无法获取网页信息
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36'
    }
    domain = "http://en.people.cn"
    f = open('C:/Users/10753/Desktop/Cfinal_test/science_result.txt', 'w')

    for index in range(0,30):
        html = requests.get(url.format(index), headers=headers).text
        soup = BeautifulSoup(html, 'lxml')

        passages = soup.find_all('div',{'class':'on1 clear'})
        for passage in passages:
            a = passage.find('a')
            href = domain + a['href'] + "\n"
            print(href)
            f.write(href)

    f.close()

def wrong_list(url,index):
    # 请求头部，不加无法获取网页信息
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36'
    }

    # url = "http://en.people.cn/n3/2019/0508/c90000-9576134.html"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    passage_content = soup.find("div",{'class':'wb_12 clear'})
    passage_des = soup.find("div",{'class':'w980 wb_10 clear'}).text
    passage_title = passage_des.split("\n")[1]
    passage_author = passage_des.split("\n")[2]

    print(passage_title,passage_author)
    p_s = passage_content.find_all('p')
    p_list = []
    for p in p_s:
        # print(p.text)
        p_list.append(p.text)

    pf = open('C:/Users/10753/Desktop/Cfinal_test/news/{}.txt'.format(index), 'w', encoding='utf-8')
    pf.write(passage_title+"\n")
    pf.write(passage_author)
    pf.writelines(p_list)
    pf.close()




def main():
    url_list = []
    # 请求头部，不加无法获取网页信息
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36'
    }
    f = open('C:/Users/10753/Desktop/Cfinal_test/science_result.txt')
    for line in f.readlines():
        url_list.append(line.strip())
    # print(url_list)
    # wrong_list = []
    index = 964
    # BS读取目标网页
    for url in url_list:
        index += 1
        print(index)
        # time.sleep(1)
        print(url)
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        try:
            passage_title = soup.find('span', {'id': 'p_title'}).get_text()
            passage_author_time = soup.find('div', {'class': 'wb_1 clear'}).get_text()
            passage_div = soup.find('div',{"class" : "wb_12 wb_12b clear"})
            p_s = passage_div.find_all('p')

            p_list = []
            for p in p_s:
                p_list.append(p.text)


            pf = open('C:/Users/10753/Desktop/Cfinal_test/news/{}.txt'.format(index), 'w',encoding='utf-8')
            pf.write(passage_title + "\n")
            pf.write(str(passage_author_time))
            pf.writelines(p_list)
            pf.close()

        except:
            wrong_list(url,index)
            # wrong_list.append(url)

    print(wrong_list)

if __name__ == '__main__':
    # GetUrlList()
    # wrong_list()
    # main()
    print(re.search(".py","loadresult.py"))