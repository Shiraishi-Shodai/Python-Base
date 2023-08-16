# -*-coding:utf-8-*-

from tqdm import tqdm
import time

# for i in tqdm(range(100)):
#     time.sleep(1)

# for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
#     time.sleep(1)

# for i in tqdm('Time is money!'):
#     time.sleep(1)


# 合計値を設定
bar = tqdm(total=1000)
# 説明文を追加
bar.set_description('Progress rate')
for i in range(100):
# 進捗率を指定
    bar.update(10)
    time.sleep(1)