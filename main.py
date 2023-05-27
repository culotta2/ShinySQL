import pathlib
import sqlparse

# from sql_metadata import Parser

PARSER_MAP = {
    'CREATE OR REPLACE': 'CREATE',
    'TEMPORARY': None,
    'TEMP': None,
}

def read_and_validate_sql_file(sql_path: pathlib.Path) -> str:
    """
    Checks that the sql file exists and returns the sql statement.

    Args
    sql_file_path: str - path to the raw SQL file

    Errors:
        FileNotFoundError - if the file does not exist

    Returns: str - SQL statement that was passed in
    """
    if sql_path.is_file():
        with open(sql_path) as sql_file:
            sql = sql_file.read()
    else:
        raise FileNotFoundError("SQL file not found")
    return sql


def remove_unnecessary_sql(sql_statement: sqlparse.sql.Statement) -> sqlparse.sql.TokenList:
    """
    Returns a dictionary of all columns selected for a statement. 

    Args
    sql_statement: sqlparse.sql.Statement - A proper SQL statement that contains a select statement

    Returns: dict - A dictionary of all columns selected by table for a statement
    """

    token_list = []

    for token in sql_statement.tokens:
        if token.ttype == sqlparse.tokens.DDL and token.value == 'CREATE OR REPLACE':
            token.value = PARSER_MAP['CREATE OR REPLACE']
            token_list.append(token)
            # print(sqlparse.sql.Token(token.ttype, PARSER_MAP['CREATE OR REPLACE']))
        elif token.ttype == sqlparse.tokens.Keyword and token.value == 'TEMPORARY':
            continue
        elif token.ttype == sqlparse.tokens.Keyword and token.value == 'TEMP':
            continue
        elif '--' in token.value:
            continue
        else:
            token_list.append(token)

    return sqlparse.sql.TokenList(token_list)

def get_columns_by_table(cleaned_token_list: sqlparse.sql.TokenList) -> dict:
    """
    This function returns a dictionary of all the column names associated with a table.

    Args
    cleaned_token_list: sqlparse.sql.TokenList - A cleaned token list of a SQL statement from remove_unnecessary_sql 

    Returns: dict - The tables are the keys and the columns selected are the values
    """
    pass




def main() -> None:
    sql_path = pathlib.Path("raw_queries") / "raw_query.sql"
    sql = read_and_validate_sql_file(sql_path)

    for stmt in sqlparse.parse(sql):
        res = remove_unnecessary_sql(stmt)
        print(res)
        print("\n")

    
if __name__ == "__main__":
    main()
