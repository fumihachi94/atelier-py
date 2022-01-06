import pandas as pd
import re

filename = "./sampledata.txt"

n = 0
p = r'"(.*?)"'
data = []

with open(filename) as f:
    for line in f:
        if line[0] == "#":
            continue
        else:
            n = n+1
            # 正規表現でlistとして抽出
            r = re.findall(p, line) 
            if n == 1:
                column_list = r
            else:
                data.append(r)
        # if n > 3: break

    # Create pandas data frame and delete VIN duplicate elements. 
    df = pd.DataFrame(data, columns=column_list).drop_duplicates()
    print(df['ＶＩＮ／プレート打刻情報'])