import openai
import sqlite3
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

c = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_table_schema():
    """Get schema information for all tables in the database"""
    cn = sqlite3.connect('example.db')
    cur = cn.cursor()
    cur.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    schemas = cur.fetchall()
    cn.close()
    return '\n'.join([schema[0] for schema in schemas if schema[0]])

def run_query(q):
    """Execute SQL query and return results"""
    cn = sqlite3.connect('example.db')
    cur = cn.cursor()
    cur.execute(q)
    r = cur.fetchall()
    cn.close()
    return r

def format_rows_to_text(r):
    """Format SQL results into a readable string"""
    return ' | '.join([str(i) for x in r for i in x])

def generate_sql(q, schema):
    """Generate SQL query using OpenAI with schema context"""
    system_prompt = f"""You are a SQL expert. Respond only with the SQL query, no explanations.
    Database schema:
    {schema}"""
    
    r = c.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Translate this to SQL: {q}"}
        ],
        temperature=0,
        max_tokens=150
    )
    return r.choices[0].message.content.strip()

def generate_response(r):
    """Generate human-readable response from SQL results"""
    res = c.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Convert the given SQL results into a clear, human-readable response. Output only the trivial results of the output, do not give the schema or the structure of the table."},
            {"role": "user", "content": f"Explain these SQL results in natural language: {r}"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return res.choices[0].message.content.strip()

def main():
    print("SQL Query Assistant (type 'exit' to quit)")
    
    # Get schema information once at startup
    schema = get_table_schema()
    print("\nLoaded database schema")
    
    while True:
        u = input("\nEnter your query: ").strip()
        if u.lower() == 'exit':
            break
            
        try:
            print("\nGenerating SQL query...")
            q = generate_sql(u, schema)
            print(f"SQL Query: {q}")
            
            print("\nExecuting query...")
            r = run_query(q)
            f = format_rows_to_text(r)
            
            print("\nGenerating response...")
            fr = generate_response(f)
            
            print("\nResponse:", fr)
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()