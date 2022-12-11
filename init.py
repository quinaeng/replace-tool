import yaml

# ターゲットのファイル一覧を取得
def get_file_list():
    file_list = []
    with open('./target.txt') as file:
        for lines in file:
            read_line = lines.replace("\n","")
            file_list.append(read_line)
    return file_list

# ファイルの一覧(global)
file_list = get_file_list()

# params.yamlから置換前と置換後の値を取得
def get_str():
    before_str = []
    after_str = []
    with open('./params.yaml', 'r') as params:
        yaml_content = yaml.safe_load(params)
        for key, value in yaml_content.items():
            before_str.append(f'{key}')
            after_str.append(f'{value}')
        return before_str, after_str
  
# 置換前と置換後のタプル(['key1', 'key2'],['value1', 'value2'],...)
word_list = get_str()
# print(word_list)
    
# ファイルを開いて文字列置換を実行する
def main():
    word_list_len = len(word_list)
    for file_path in file_list:
         print(file_list)
         with open(file_list, encoding="cp932") as file:
             for i in range(0, word_list_len):
                 read_lines = file.read()
             obj = read_lines.replace(word_list[i][0], word_list[i][1])
         with open(file_list, encoding="cp932") as file:
             file.write(obj)
#                print(word_list[i][0])
#                print(word_list)
#                key = '${' + word_list[0][i] + '}'
#                value = word_list[1][i]
#                lines = file.read()
#                lines = lines.replace(key, value)

#main()


# 置換 
#with open('./docker-compose.yaml', encoding="cp932") as file:
#    read_lines = file.read()

#obj = read_lines.replace('${PROXY_IMAGE}', 'aa')

#with open('./docker-compose.yaml', mode="w", encoding="cp932") as file:
#    file.write(obj)
