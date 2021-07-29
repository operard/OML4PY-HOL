# -*- coding: utf-8 -*-
"""
Created on Thu Jul 01 06:27:39 2021

@author: operard
"""

import cx_Oracle
import keyring
import os
import pandas as pd

os.environ['TNS_ADMIN'] = '/home/opc/adb_virt_env'

# password = keyring.get_password('adw','admin')
# %sql oracle+cx_oracle://admin:$password@domsdb_medium

#connection = cx_Oracle.connect('admin', 'Welcome1#Welcome1#', 'oliadb20210729_medium')

connection = cx_Oracle.connect('OMLUSER', 'Welcome1#Welcome1#', 'oliadb20210729_medium')

cursor = connection.cursor()
rs = cursor.execute("select 'Hello for ADB' from dual")
rs.fetchall()

query = 'SELECT * from user_tables'
data_test = pd.read_sql(query, con=connection)
data_test.head()
print(data_test)

# Close Cursor & Connection
cursor.close()
connection.close()

