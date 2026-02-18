#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and print/save them."""

import requests
import csv
import json


def fetch_and_print_posts():
    """Fetch posts and print the status code and titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for d in data:
            print(d["title"])


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)


fetch_and_print_posts()
fetch_and_save_posts()
