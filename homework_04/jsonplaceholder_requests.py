"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


# Declare async function for get responce from JSONPlaceholder
async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


# Declare async function for get users -> JSON
async def get_users_data():
    users_data = await fetch_json(USERS_DATA_URL)
    return users_data


# Declare async function for get posts -> JSON
async def get_posts_data():
    posts_data = await fetch_json(POSTS_DATA_URL)
    return posts_data
