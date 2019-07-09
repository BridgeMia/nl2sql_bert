import os

import pandas as pd
import json

data_sets = ['train', 'valid', 'test']

for data_set in data_sets:
    data_set_dir = r"data/nl2sql_%s_20190618" % data_set
    raw_json_fn = os.path.join(data_set_dir, "%s.json" % data_set)
    data = []
    with open(raw_json_fn, encoding='utf-8') as fin:
        for line in fin:
            line_data = json.loads(line)
            data.append(line_data)
    sp = data[0]
    
    break
