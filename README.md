# simple_search_engine
一个简单的站内搜索引擎

数据库：人民日报英文网1157条新闻

文本标准化：基于Python-NLTK

构建倒排索引：Mapreduce，这里在Azure云上的HDInsight实现

TF-IDF：Mapreduce，这里在Azure云上的HDInsight实现

搜索：哈希树搜索，没有实现模糊搜索，想要实现模糊搜索可以使用trier树~

网页框架：flask，app中的application.py为主函数

部署：Azure云 appservice

# cloudproject
(1)mapperword.py：mapreduce 构建倒排索引

(2)reducerword.py：mapreduce 构建倒排索引

(3)reducertf.py: mapreduce 计算tf

(4)people.py：人民日报爬虫

(5)standardize.py：文本标准化

(6)to_html.py：将新闻转换为网页

# app
(1) application.py: flask主函数

(2) search_engine.py: 搜索引擎实现

(3) count.json:词语在各文章中的出现次数

(4) nwcount.json:各文章总词数

(5) idf.json:各词语idf值

(6) record.json:倒排索引列表

# 演示：
  进入/app文件夹，安装flask框架后运行application.py
