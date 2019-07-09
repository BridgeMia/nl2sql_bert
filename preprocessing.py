import os

import pandas as pd
import json

data_sets = ['train', 'valid', 'test']


class RawDataSet:
    def __init__(self, set_name: str):
        self.set_name = set_name
        self.data_set = self._load_data_json()
        
    def _load_data_json(self):
        data_set_dir = r"data/nl2sql_%s_20190618" % self.set_name
        raw_json_fn = os.path.join(data_set_dir, "%s.json" % self.set_name)
        data = []
        with open(raw_json_fn, encoding='utf-8') as fin:
            for line in fin:
                line_data = json.loads(line)
                data.append(line_data)
        return data
    
