from django.contrib.auth.models import User
from blog.models import Article

# Create users
user1 = User.objects.create_user(username='alice', password='password123')
user2 = User.objects.create_user(username='bob', password='password123')
user3 = User.objects.create_user(username='charlie', password='password123')

print(f"Created users: {user1.username}, {user2.username}, {user3.username}")

# Create articles for alice
Article.objects.create(
    title="Getting Started with Django",
    content="Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's perfect for building web applications quickly.",
    author=user1
)

Article.objects.create(
    title="Python Best Practices",
    content="Writing clean Python code is essential. Always follow PEP 8, use meaningful variable names, and write docstrings for your functions.",
    author=user1
)

Article.objects.create(
    title="Understanding Django Models",
    content="Models in Django are the single, definitive source of information about your data. They contain the essential fields and behaviors of the data you're storing.",
    author=user1
)

# Create articles for bob
Article.objects.create(
    title="Web Development Trends 2026",
    content="The web development landscape is constantly evolving. This year we're seeing increased adoption of AI tools, better performance optimization, and improved accessibility standards.",
    author=user2
)

Article.objects.create(
    title="Database Design Tips",
    content="Good database design is crucial for application performance. Always normalize your data, use appropriate indexes, and plan for scalability from the start.",
    author=user2
)

# Create articles for charlie
Article.objects.create(
    title="Introduction to REST APIs",
    content="REST APIs are the backbone of modern web applications. They provide a standardized way for different systems to communicate over HTTP.",
    author=user3
)

Article.objects.create(
    title="Testing Your Django Apps",
    content="Testing is not optional. Write unit tests for your models, integration tests for your views, and end-to-end tests for critical user flows.",
    author=user3
)

Article.objects.create(
    title="Deployment Strategies",
    content="Deploying a Django application requires careful planning. Consider using containerization with Docker, setting up proper CI/CD pipelines, and monitoring your application in production.",
    author=user3
)

print(f"\nCreated {Article.objects.count()} articles")
print("\nArticles by user:")
for user in User.objects.all():
    count = user.articles.count()
    print(f"  {user.username}: {count} articles")
