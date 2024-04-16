import requests
import csv
from bs4 import BeautifulSoup
import psycopg2

con = psycopg2.connect(
database="postgres",
user="postgres",
password="123456",
host="localhost",
port= '5432'
)
cursor_obj = con.cursor()
def imdb(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        movie_data = []
        for movie_elem in soup.find_all("div", class_="redHightlight"):
            name = movie_elem.find("h3").text.strip()
            movie_data.append({
                "name": name
            })
        return movie_data
    else:
        print("Failed to retrieve data")
        return []

if __name__ == "__main__":
    url = "http://www.picasso.com/"
    movie_data = imdb(url)
    if movie_data:
        for movie in movie_data:
            print(movie)
            cursor_obj.execute("INSERT INTO emp(name) VALUES(%s)", (movie["name"],))
        con.commit()
        cursor_obj.execute("SELECT * FROM emp")
        rows = cursor_obj.fetchall()

        for row in rows:
           print(row)
        csv_file = "brand_data.csv"

        with open(csv_file, 'w', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([desc[0] for desc in cursor_obj.description])
         writer.writerows(rows)  
        cursor_obj.close()
        con.close()   
    else:
        print("No data scraped")
