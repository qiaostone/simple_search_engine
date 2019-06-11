import json

header_template = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>新闻页面</title>
<link rel="stylesheet" href="style.css" type="text/css"/>
</head> 

<body>
<h2>"""

author_template ="""</h2>
<p class="one gray">"""

content_template ="""</p>
<hr/>"""

end_template = """"</body>
</html>"""

for i in range(1,1157):
    with open("./news_json/{}.json".format(i),'r') as load_f:
        load_dict = json.load(load_f)
        title = load_dict['title']
        time_author = load_dict['time_author']
        content = load_dict['content']

        # print(title, time_author, content)

        content_string = ""
        for string in content:
            insert = "<p>" + string + "</p>"
            content_string += insert

        html = header_template + title + author_template + time_author + content_template + content_string + end_template
        html_f = open("./web/{}.html".format(i),"w",encoding="utf-8")
        html_f.writelines(html)


