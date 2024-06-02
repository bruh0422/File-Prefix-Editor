import os

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

prefix = input('輸入檔名前綴: ')

index = 1
total = len(os.listdir(folder_path))

for item in os.listdir(folder_path):
    try:
        print(f'({index} / {total}) ', end='')

        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            new = os.path.join(folder_path, f'{prefix}{os.path.basename(item_path)}')
            os.rename(item_path, new)

            print(f'{item_path} -> {new}')
        else:
            print(f'{item_path} 並非一個檔案。')
    except Exception as e:
        print(f'未知錯誤 - ({e})')

    index += 1