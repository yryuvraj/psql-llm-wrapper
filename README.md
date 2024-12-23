# psql-llm-wrapper
This application allows you to generate, execute, and interpret SQL queries using OpenAI's GPT-3.5-turbo model. Below are the steps to set up and run this project locally.

## Prerequisites

- Python 3.7+
- An OpenAI API key
- SQLite3

## Installation

1. Clone the repository or copy the project files to your local machine.
2. Open a terminal and navigate to the project directory.
3. Install the required Python packages:

```bash
pip install openai python-dotenv
```

## Setting Up Environment Variables

1. Create a `.env` file in the root of the project directory.
2. Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Setting Up the SQLite Database

1. Ensure `sqlite3` is installed on your system.
2. Create an SQLite database file named `example.db` in the project directory.
3. Create and populate tables as needed for your queries. For example:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
-- Example To create DB, you can use any DB of your own to test.
-- I have pushed an example.db to help you test the program. 
INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);
```

You can use an SQLite browser or the command-line interface to execute these SQL statements.

## Running the Application

1. Run the Python script:

```bash
python your_script_name.py
```

2. Follow the prompts to enter your query in natural language.
3. Type `exit` to quit the program.

## Example Usage

- Input: `Show all users older than 25.`
- Output: SQL Query, Results, and a Human-Readable Explanation.

---

Enjoy exploring SQL with the power of OpenAI!

