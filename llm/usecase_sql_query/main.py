import streamlit as st
from sqlalchemy import create_engine
from config import DATABASE_URI
from utils import get_db_schema, call_euri_llm, execute_sql

# Set the page configuration with a title and wide layout for better display
st.set_page_config(page_title="SQL Assistant", layout="wide")

# Display the main title of the app with an emoji for visual appeal
st.title("🧠 SQL-Powered Data Retrieval Assistant")

# Create a text input box for the user to ask questions in natural language
nl_query = st.text_input("Ask your question (in natural language):")

# streamlit run main.py
if nl_query:
    # Create a SQLAlchemy engine instance connected to the database using the provided URI
    # Applicable to local database, mysql, mssql, oracle, db2, postgres, etc
    engine = create_engine(DATABASE_URI)
    
    # Retrieve the database schema as a formatted string for context in prompt
    schema = get_db_schema(engine)

    # Read the prompt template from a text file
    with open("prompt_template.txt") as f:
        template = f.read()
    
    # Format the prompt by inserting the schema and user's natural language question
    # The prompt guides the AI to convert a user's natural language question into an SQL query using the provided schema,
    # and to respond with only the SQL code, no explanations.
    prompt = template.format(schema=schema, question=nl_query)

    # Show a spinner while calling the language model to generate the SQL query
    with st.spinner("Generating SQL using EURI LLM..."):
        # Call the language model API with the constructed prompt to get the SQL query
        sql_query = call_euri_llm(prompt)

    # Display the generated SQL query in the app with SQL syntax highlighting
    st.code(sql_query, language="sql")

    try:
        # Execute the generated SQL query against the database
        results, columns = execute_sql(engine, sql_query)
        print(results)
        if results:
            # Display the query results in a data table with full width
            st.dataframe(results, use_container_width=True)
        else:
            # Inform the user if the query returned no data
            st.info("Query executed successfully. No data returned.")
    except Exception as e:
        # Show an error message if executing the SQL fails
        st.error(f"Error running query: {e}")
