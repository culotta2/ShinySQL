import pathlib
import sqlparse

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


def main() -> None:
    sql_path = pathlib.Path("raw_queries") / "raw_query.sql"
    sql = read_and_validate_sql_file(sql_path)
    
    print(sql)

if __name__ == "__main__":
    main()
