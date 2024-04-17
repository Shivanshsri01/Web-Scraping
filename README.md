**Web Scraping with Python**

This Python script demonstrates how to perform web scraping using the BeautifulSoup library to extract information from a webpage and store it in a PostgreSQL database and CSV file.

### Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.9.6
- `requests` library (install using `pip install requests`)
- `beautifulsoup4` library (install using `pip install beautifulsoup4`)
- `psycopg2` library (install using `pip install psycopg2`)

### Steps

1. **Import Libraries**: The script imports necessary libraries: `requests`, `csv`, `BeautifulSoup`, and `psycopg2`.
   
  **requests**: This library is used for sending HTTP requests and retrieving data from websites.

   You can install it using pip:

   pip install requests
   
   **Beautiful Soup**: This library is utilized for parsing HTML and XML documents, particularly for web scraping tasks.

   You can install it using pip:

   pip install beautifulsoup4
   
2. **Database Connection**: For interacting with PostgreSQL databases
   
   **psycopg2**: This library is required for connecting to PostgreSQL databases from Python.
   
   You can install using this command:
   
   **pip install psycopg2**
   
   **Run the Script**: Execute the script using Python:

    python script_name.py

4. **Define Scraping Function**: The `imdb` function takes a URL as input, sends a GET request, and extracts movie data using BeautifulSoup.

5. **Scrape Data**: The script specifies a URL to scrape (`http://www.picasso.com/`) and calls the `imdb` function to retrieve movie data.

6. **Store Data in Database**: If data is successfully scraped, it iterates through the movie data, inserts it into the PostgreSQL database, and commits the transaction.

7. **Retrieve Data from Database**: It queries the database to fetch all records from the `emp` table and prints them.

8. **Export Data to CSV**: It exports the fetched data to a CSV file named `brand_data.csv`.

9. **Close Database Connection**: Finally, it closes the cursor and the database connection.

### Note

- If the script fails to retrieve data from the specified URL, it prints "Failed to retrieve data."
- If no data is scraped, it prints "No data scraped."
- The exported CSV file (brand_data.csv) will contain one columns: "name" representing data.

### Author

This script is authored by Shivansh Srivastava .Feel free for any question or improvement.

## License

This project is licensed under the [MIT License](LICENSE). Copyright © 2024 Shivansh Srivastava

