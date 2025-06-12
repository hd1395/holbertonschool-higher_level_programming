import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the response status code,
    and then prints the title of each post if the request was successful.
    """
    try:
        response = requests.get(URL)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post["title"])

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder, and if successful, structures the
    data into a list of dictionaries (id, title, body) and writes it to
    a CSV file named 'posts.csv'.
    """
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            posts_data = response.json()
            posts_list = []
            for post in posts_data:
                posts_list.append({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })

            csv_file_name = 'posts.csv'
            fieldnames = ['id', 'title', 'body']

            with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(posts_list)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request for saving posts: {e}")
    except IOError as e:
        print(f"An I/O error occurred while writing the CSV file: {e}")
