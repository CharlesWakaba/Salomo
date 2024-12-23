import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.setup import setup_database, Data
from db.connection import get_db_session

def populate_data():
    setup_database()  # Ensure the database and table are created
    
    sample_data = [
        "Sample data entry 1",
        "Sample data entry 2",
        "Another example of data",
        "Test data for query"
    ]
    
    session = next(get_db_session())
    for content in sample_data:
        data_entry = Data(content=content)
        session.add(data_entry)
    
    session.commit()
    session.close()
    print("Sample data populated successfully.")

if __name__ == "__main__":
    populate_data()
