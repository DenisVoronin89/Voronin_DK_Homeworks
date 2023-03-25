"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from jsonplaceholder_requests import get_posts_data, get_users_data

from models import Base, User, Post, Session, engine


# Declare async function for create and drop tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Declare async function for add users
async def add_users_to_db():
    users = await get_users_data()
    async with engine.begin() as conn:
        session = Session()

        for user in users:
            user_object = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
            session.add(user_object)
        await session.commit()
        await session.close()


# Declare async function for add posts
async def add_posts_to_db():
    posts = await get_posts_data()

    async with engine.begin() as conn:
        session = Session()

        for post in posts:
            post_object = Post(id=post['id'], title=post['title'], body=post['body'], user_id=post['userId'])
            session.add(post_object)
        await session.commit()
        await session.close()


# Declare async main function for run all programm
async def async_main():
    async with Session() as session:
        await create_tables()
        users_data, posts_data = await asyncio.gather(
            add_users_to_db(),
            add_posts_to_db(),
        )
        return users_data, posts_data


# run programm
def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == '__main__':
    main()

