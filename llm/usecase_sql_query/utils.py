import requests
from sqlalchemy import text, MetaData
# from sqlalchemy.engine import Engine
# from sqlalchemy.sql import text
from typing import Tuple, List
from config import EURI_API_KEY, EURI_API_URL, MODEL_NAME


def get_db_schema(engine: Engine) -> str:
    """
    Generates a textual representation of the database schema.

    Args:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine connected to the database.

    Returns:
        str: A formatted string listing all tables and their columns with data types.

    Example:
        schema = get_db_schema(engine)
        print(schema)
    """
    # Create a MetaData instance to hold schema information
    meta = MetaData()
    # Reflect the database schema into MetaData
    meta.reflect(bind=engine)
    schema = ""
    # Iterate over all tables in the schema
    for table in meta.tables.values():
        # Append table name
        schema += f"\nTable: {table.name}\n"
        # Append columns with their data types
        schema += "Columns: " + ', '.join(
            [f"{col.name} ({str(col.type)})" for col in table.columns]
        ) + "\n"
    # Return the schema string without leading/trailing whitespace
    return schema.strip()


def call_euri_llm(prompt: str) -> str:
    """
    Sends a prompt to the EURI language model API and returns the generated response.

    Args:
        prompt (str): The input prompt string to send to the language model.

    Returns:
        str: The generated response content from the model, stripped of leading/trailing whitespace.

    Example:
        response = call_euri_llm("Explain the theory of relativity.")
        print(response)
    """
    headers = {
        "Authorization": f"Bearer {EURI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3,
        "max_tokens": 300
    }

    response = requests.post(EURI_API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raise exception if the request failed
    return response.json()["choices"][0]["message"]["content"].strip()


def execute_sql(engine: Engine, query: str) -> Tuple[List[Tuple], List[str]]:
    """
    Executes a SQL query using the provided SQLAlchemy engine and returns the results.

    Args:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine connected to the database.
        query (str): The SQL query string to execute.

    Returns:
        Tuple[List[Tuple], List[str]]: A tuple containing:
            - A list of tuples representing the fetched rows.
            - A list of column names corresponding to the result set.

    Example:
        rows, columns = execute_sql(engine, "SELECT * FROM users")
        print(columns)
        for row in rows:
            print(row)
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall(), result.keys()
