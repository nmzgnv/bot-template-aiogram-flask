import asyncio
from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')


async def close_connection():
    await db.pop_bind().close()


async def main():
    await db.set_bind('asyncpg://admin:admin@localhost/BotTemplate')
    await db.gino.create_all()

    user = await User.get(1)
    print(user.nickname)

    await close_connection()


asyncio.get_event_loop().run_until_complete(main())
