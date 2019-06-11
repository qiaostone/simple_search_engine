import json

write_dict = {}

for i in range(1,1157):
    with open("./news_json/{}.json".format(i),'r') as load_f:
        amount = 0
        load_dict = json.load(load_f)
        content = load_dict['content']

        for string in content:
            words = string.split(" ")
            amount += len(words)

    write_dict[i] = amount

print(write_dict)
write_file = open("wordcount.json","w")
json.dump(write_dict,write_file)
