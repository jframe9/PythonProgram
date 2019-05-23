import json

file_path = r'D:\Software\Downloadsoft\Down_download\Sp_download\CCKS 2019 Task1\demo.txt'

row_list = []

with open(file_path, 'r') as file_txt:
    # content_json = file_txt.readlines()
    # print(type(content_json[0]))
    # for sw in content_json:
    #     data = json.loads(sw)
    #     print(data)
    for line in file_txt:
        # print(line)
        row_list.append(line)
lists_result = []
result_lists = []
for row in row_list:
    # print(type(row))
    # json_str = json.dumps(row)
    json_result = json.loads(row)
    for sub in json_result['entities']:
        sub_result_dict = dict(label_type=sub['label_type'], entity=json_result['originalText'][int(sub['start_pos']):int(sub['end_pos'])])
        lists_result.append(sub_result_dict)
    result_lists.append(lists_result)
    lists_result = []
print(result_lists)
