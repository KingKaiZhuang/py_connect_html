import json

# 初始化 num 變數
num = 42

# 定義一個函數來更新 JSON 檔案
def update_json_file():
    # 創建一個字典
    data = {'num': num}

    # 將字典轉換為 JSON 格式
    json_data = json.dumps(data)

    # 寫入 JSON 檔案
    with open('file.json', 'w') as file:
        file.write(json_data)

# 初次創建 JSON 檔案
update_json_file()

# 更新 num 變數的值
num = 55

# 自動更新 JSON 檔案
update_json_file()

print('已經成功更新 file.json 中的 num 值！')
