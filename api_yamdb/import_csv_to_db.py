import csv
import os

import django

from reviews.models import (
    User, Genre, Category, Title, Review, Comment, GenreTitle
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_yamdb.settings")
django.setup()

path = 'static/data'
os.chdir(path)

with open('users.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = User(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            role=row['role'],
            bio=row['bio'],
            first_name=row['first_name'],
            last_name=row['last_name']
        )
        instance.save()

with open('category.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = Category(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )
        instance.save()

with open('genre.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = Genre(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )
        instance.save()

with open('titles.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = Title(
            id=row['id'],
            name=row['name'],
            year=row['year'],
            category=Category.objects.get(id=row['category'])
        )
        instance.save()

with open('genre_title.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = GenreTitle(
            id=row['id'],
            title=Title.objects.get(id=row['title_id']),
            genre=Genre.objects.get(id=row['genre_id'])
        )
        instance.save()

with open('review.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = Review(
            id=row['id'],
            title=Title.objects.get(id=row['title_id']),
            text=row['text'],
            author=User.objects.get(id=row['author']),
            score=row['score'],
            pub_date=row['pub_date']
        )
        instance.save()

with open('comments.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        instance = Comment(
            id=row['id'],
            review=Review.objects.get(id=row['review_id']),
            text=row['text'],
            author=User.objects.get(id=row['author']),
            pub_date=row['pub_date']
        )
        instance.save()
