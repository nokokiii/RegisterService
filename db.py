from surrealdb import Surreal
from dotenv import dotenv_values

DB_CONFIG = dotenv_values(".env")


async def db(query: str) -> None:
    """
    This function is connecting to the database and execute query
    """
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": DB_CONFIG["USER"], "pass": DB_CONFIG["PASSWORD"]})
        await db.use(DB_CONFIG["NAMESPACE"], DB_CONFIG["DATABASE"])

        await db.query(query)
        