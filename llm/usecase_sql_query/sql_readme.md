## Overview
SQL-Powered  Data Retrieval Assistant
### Flow Diagram

UI Client (Streamlit) >(query in Eng lang)> LLM (Euriai/Openai) >> SQL Query (meta) >> SQL DB >> Output UI

### Database Examples
- PlanetScale (Sql) https://planetscale.com/
- Neon (Postgres) https://neon.com/
- Supabase (Postgres) https://supabase.com/
- Render https://render.com/
- Railway https://railway.com/
- Azure/ AWS/ GCP

Note: Using Neon for this usecase https://console.neon.tech/app/projects/sparkling-art-71623961

### Steps to use Neon
1. Copy the *connection string* from the Neon by clicking on **Connect**.
2. Navigate to **SQL Editor** to write/run new query and **Tables** to browse the created tables.
3. Write and run a query to create all new tables:
    ```sql
    CREATE TABLE customers (
        customer_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(20),
        city VARCHAR(50)
    );

    CREATE TABLE products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(100),
        category VARCHAR(50),
        price DECIMAL(10, 2)
    );

    CREATE TABLE orders (
        order_id SERIAL PRIMARY KEY,
        customer_id INT REFERENCES customers(customer_id),
        order_date DATE,
        total_amount DECIMAL(10, 2)
    );

    CREATE TABLE order_items (
        item_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(order_id),
        product_id INT REFERENCES products(product_id),
        quantity INT,
        price DECIMAL(10, 2)
    );
    ```
4. Objective is to query from the table, so write and run a query to write some data into all the tables:
    ```sql
    INSERT INTO customers (name, email, phone, city) VALUES
    ('Alice Johnson', 'alice@gmail.com', '999-111-2222', 'New York'),
    ('Bob Smith', 'bob@gmail.com', '888-222-3333', 'Los Angeles'),
    ('Charlie Lee', 'charlie@gmail.com', '777-333-4444', 'Chicago');

    INSERT INTO products (product_name, category, price) VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Headphones', 'Accessories',150.00),
    ('Desk Chair', 'Furniture',300.00);

    INSERT INTO orders (customer_id, order_date, total_amount) VALUES
    (1, '2024-06-01', 1500.00),
    (2, '2024-06-02', 800.00),
    (3, '2024-06-03', 450.00);

    INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
    (1, 1, 1, 1200.00),
    (1, 3, 2, 150.00),
    (2, 2, 1, 800.00),
    (3, 4, 1, 300.00),
    (3, 3, 1, 150.00);
    ```
 
 ### Create supporting files
1. Create **.env** file to store the *LLM api key* and *Neon connection string*.
2. Create **config.py** file to load the environemnt variables and define the model name and LLM url.
3. Create **utils.py** file to define the supporting functions like get_db_schema(), call_euri_llm(), and execute_sql().
4. Create **requirements.txt** file to add the list of libraries required to run the application.
5. Create **prompt_template.txt** file to curate the prompt based on the table schema and user query while passing to the llm.


### Streamlit SQL Assistant Workflow
1. **Page Setup**: Configures app title and wide layout for better user experience.
2. **User Input & Context**: Displays a question box and fetches database schema for context.
3. **Prompt & SQL Generation**: Reads a template, formats it with schema and question, then calls the API to generate SQL.
4. **Display & Execution**: Shows the generated SQL, executes it, and displays results or a message if no data.
5. **Error Handling**: Catches and reports errors during SQL execution.
