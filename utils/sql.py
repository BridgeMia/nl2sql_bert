import sqlite3

class SQLParser:
    # SQL mapping:
    op_sql_dict = {0: ">", 1: "<", 2: "==", 3: "!="}
    agg_sql_dict = {0: "", 1: "AVG", 2: "MAX", 3: "MIN", 4: "COUNT", 5: "SUM"}
    conn_sql_dict = {0: "", 1: "and", 2: "or"}
    
    def __init__(self, sql: dict, table: str, db_name: str):
        """
        
        :param sql:
        :param table:
        :param db_name:
        """
        self.agg = sql.get('agg', None)
        self.cond_conn_op = sql.get('cond_conn_op', None)
        self.sel = sql.get('sel', None)
        self.conds = sql.get('conds', None)
        self.table = table
        self.conn = sqlite3.connect(r'data/nl2sql_{db_name}_20190618/{db_name}.db'.format(db_name=db_name))
        
    def _transfer_single_cond(self, col, op, val):
        
        return
    def _parse(self):
        condition_str = \
            """
            WHERE {conditions}
            """.format(
                conditions=self.cond_conn_op.join()
            )
        sql_cmd = \
            """
            SELECT {agg} {columns} FROM {table}
            WHERE
            """.\
                format(agg=self.agg,
                       columns=','.join(self.sel),
                       table=self.table
                       )
        

if __name__ == '__main__':
    sql_sample = {
        'agg': [5],
        'cond_conn_op': 2,
        'sel': [2],
        'conds': [[0, 2, '大黄蜂'], [0, 2, '密室逃生']]
    }
    
