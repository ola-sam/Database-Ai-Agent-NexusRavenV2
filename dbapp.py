import streamlit as st
import sqlite3
import random


# Streamlit app configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Title of the app
st.title("Database AI Chatbot")


# User input text box

def query(payload):
    """
    Sends a payload to a TGI endpoint.
    """
    API_URL = "http://nexusraven.nexusflow.ai"
    headers = {
        "Content-Type": "application/json"
    }
    import requests
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def query_raven(prompt):
    """
    This function sends a request to the TGI endpoint to get Raven's function call.
    This will not generate Raven's justification and reasoning for the call, to save on latency.
    """
    import requests
    output = query({
        "inputs": prompt,
        "parameters" : {"temperature" : 0.001, "stop" : ["<bot_end>"], "do_sample" : False, "max_new_tokens" : 2048, "return_full_text" : False}})
    call = output[0]["generated_text"].replace("Call:", "").strip()
    return call

def query_raven_with_reasoning(prompt):
    """
    This function sends a request to the TGI endpoint to get Raven's function call AND justification for the call
    """
    import requests
    output = query({
        "inputs": prompt,
        "parameters" : {"temperature" : 0.001, "do_sample" : False, "max_new_tokens" : 2000}})
    call = output[0]["generated_text"].replace("Call:", "").strip()
    return call

def execute_sql(sql_code : str):
    import sqlite3
    
    # Connect to the database
    conn = sqlite3.connect('toy_database.db')
    cursor = conn.cursor()
    
    cursor.execute('PRAGMA table_info(toys)')
    columns = [info[1] for info in cursor.fetchall()]  # Extracting the column names
    
    # Query to select all data
    cursor.execute(sql_code)
    rows = cursor.fetchall()
    
    return_string = " ".join(columns)
    for idx, row in enumerate(rows):
        row = (idx, *row)
        return_string += "\n" + str(row)
    
    # Close the connection
    conn.close()
    return return_string

# def create_random_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('toy_database.db')
    
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS toys
                   (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    
    # Define some random prefixes and suffixes for toy names
    prefixes = ['Magic', 'Super', 'Wonder', 'Mighty', 'Happy', 'Crazy']
    suffixes = ['Bear', 'Car', 'Doll', 'Train', 'Dragon', 'Robot']
    
    # Insert 100 sample data rows with random names
    for i in range(1, 101):
        toy_name = random.choice(prefixes) + ' ' + random.choice(suffixes)
        toy_price = round(random.uniform(5, 20), 2)  # Random price between 5 and 20
        cursor.execute('INSERT INTO toys (name, price) VALUES (?, ?)', (toy_name, toy_price))
    
    # Commit the transaction
    conn.commit()
    
    # Query the database
    cursor.execute('SELECT * FROM toys')
    print("Toys in database:")
    for row in cursor.fetchall():
        print(row)
    
    # Close the connection
    # conn.close()

# Internal database name setting


# create_random_database()
DB_NAME = 'toy_database.db'


@st.cache_resource
# Connect to the database
def connect_db():
    return sqlite3.connect(DB_NAME)

# List all toys
def list_all_toys():
    with connect_db() as conn:
        cursor = conn.execute('SELECT * FROM toys')
        return cursor.fetchall()

def count_all_toys():
    with connect_db() as conn:
        cursor = conn.execute('SELECT COUNT(*) FROM toys')
        return cursor.fetchall()

# Find toy by name prefix
def find_toy_by_prefix(prefix):
    with connect_db() as conn:
        query = 'SELECT * FROM toys WHERE name LIKE ?'
        cursor = conn.execute(query, (prefix + '%',))
        return cursor.fetchall()

# Find toys in a price range
def find_toys_in_price_range(low_price, high_price):
    with connect_db() as conn:
        query = 'SELECT * FROM toys WHERE price BETWEEN ? AND ?'
        cursor = conn.execute(query, (low_price, high_price))
        return cursor.fetchall()

        # Get a random selection of toys

def get_random_toys(count=5):
    with connect_db() as conn:
        cursor = conn.execute('SELECT * FROM toys')
        all_toys = cursor.fetchall()
        return random.sample(all_toys, min(count, len(all_toys)))

# Function to get the most expensive toy
def get_most_expensive_toy(count=1):
    with connect_db() as conn:
        cursor = conn.execute(f'SELECT * FROM toys ORDER BY price DESC LIMIT {count}')
        return cursor.fetchone()

# Function to get the cheapest toy
def get_cheapest_toy(count=1):
    with connect_db() as conn:
        cursor = conn.execute(f'SELECT * FROM toys ORDER BY price ASC LIMIT {count}')
        return cursor.fetchone()


def get_raven_response(question):
    try:
        raven_prompt = \
            f'''
            Function:
            def list_all_toys():
                """
                Retrieves a list of all toys from the database. This function does not take any parameters.
                Returns: A list of tuples, where each tuple represents a toy with all its attributes (id, name, price).
                """

            Function:
            def count_all_toys():
                """
                Retrieves count of all toys from the database. This function does not take any parameters.
                Returns: A count of all items.
                """

            Function:
            def find_toy_by_prefix(prefix):
                """
                Searches for and retrieves toys whose names start with a specified prefix.
                Parameters:
                - prefix (str): The prefix to search for in toy names.
                Returns: A list of tuples, where each tuple represents a toy that matches the prefix criteria.
                """

            Function:
            def find_toys_in_price_range(low_price, high_price):
                """
                Finds and returns toys within a specified price range.
                Parameters:
                - low_price (float): The lower bound of the price range.
                - high_price (float): The upper bound of the price range.
                Returns: A list of tuples, each representing a toy whose price falls within the specified range.
                """

            Function:
            def get_random_toys():
                """
                Selects and returns a random set of toys from the database, simulating a "featured toys" list.

                Returns: A list of tuples, each representing a randomly selected toy. The number of toys returned is up to the specified count.
                """

            Function:
            def get_most_expensive_toy(count : int):
                """
                Retrieves the most expensive toy from the database.
                This function does not take any parameters.

                Returns: A tuple representing the most expensive toy, including its id, name, and price.
                """

            Function:
            def get_cheapest_toy(count : int):
                """
                Finds and retrieves the cheapest toy in the database.
                This function does not take any parameters.

                Returns: A tuple representing the cheapest toy, including its id, name, and price.
                """

            Function:
            def no_relevant_function(user_query : str):
                """
                Call this when no other provided function can be called to answer the user query.

                Args:
                    user_query: The user_query that cannot be answered by any other function calls.
                """


            User Query: {question}<human_end>

            '''


        output = query_raven(raven_prompt)
        # print (f"LLM's function call: {output}")
        database_result = eval(output)

        full_prompt = \
        f"""
        <s> [INST]
        {database_result}

        Use the information above to answer the following question in a single sentence.

        Question:
        {question} [/INST]
        """
        # Make a request to the raven api for generating a response
        grounded_response = query_raven(full_prompt)
        return grounded_response
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize the session state for the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Message Database AI Assistant!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        question = st.session_state.messages[-1]["content"]

        answer = get_raven_response(question)
        # translated_answer = .... 
        response = st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})  


