# nl2sql bert

Code for [首届中文NL2SQL挑战赛](<https://tianchi.aliyun.com/competition/entrance/231716/introduction?spm=5176.12281949.1003.7.4f104c2aJnqzwl>)

## 数据描述

- 原始的数据json:

  ```json
  {
       "table_id": "a1b2c3d4", # 相应表格的id
       "question": "世茂茂悦府新盘容积率大于1，请问它的套均面积是多少？", # 自然语言问句
      "sql":{ # 真实SQL
          "sel": [7], # SQL选择的列 
          "agg": [0], # 选择的列相应的聚合函数, '0'代表无
          "cond_conn_op": 0, # 条件之间的关系
          "conds": [
              [1,2,"世茂茂悦府"], # 条件列, 条件类型, 条件值，col_1 == "世茂茂悦府"
              [6,0,1]
          ]
      }
  }
  ```

- 数据库操作ID映射表：

  ```python
  op_sql_dict = {0:">", 1:"<", 2:"==", 3:"!="}
  agg_sql_dict = {0:"", 1:"AVG", 2:"MAX", 3:"MIN", 4:"COUNT", 5:"SUM"}
  conn_sql_dict = {0:"", 1:"and", 2:"or"}
  ```

- table的json内容: 

  ```json
  {
      "id":"a1b2c3d4", # 表格id
      "name":"Table_a1b2c3d4", # 表格名称
      "title":"表1：2019年新开工预测 ", # 表格标题
      "header":[ # 表格所包含的列名
          "300城市土地出让",
          "规划建筑面积(万㎡)",
          ……
      ],
      "types":[ # 表格列所相应的类型
          "text",
          "real",
          ……
      ],
      "rows":[ # 表格每一行所存储的值
          [
              "2009年7月-2010年6月",
              168212.4,
              ……
          ]
      ]
  }
  ```

  

## 模块设计

1. data_loader

   

2. 