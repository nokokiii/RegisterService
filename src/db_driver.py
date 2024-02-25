from surrealdb import Surreal
from dotenv import dotenv_values
from faker import Faker
from faker.providers import DynamicProvider

DB_CONFIG = dotenv_values(".env")


async def connection(query: str):
    """
    This function is connecting to the database and execute query
    """
    async with Surreal("ws://localhost:9000/rpc") as database:
        await database.signin({"user": DB_CONFIG["USER"], "pass": DB_CONFIG["PASSWORD"]})
        await database.use(DB_CONFIG["NAMESPACE"], DB_CONFIG["DATABASE"])

        response = await database.query(query)

    return response[0]["result"]


async def init_db() -> None:
    """
    This function is initializing the database with the table and some data
    """
    async with Surreal("ws://localhost:9000/rpc") as database:
        await database.signin({"user": DB_CONFIG["USER"], "pass": DB_CONFIG["PASSWORD"]})
        await database.use(DB_CONFIG["NAMESPACE"], DB_CONFIG["DATABASE"])

        table_query = ("DEFINE TABLE Users SCHEMAFULL;"
                       "DEFINE FIELD firstName ON Users type string;"
                       "DEFINE FIELD lastName ON Users type string;"
                       "DEFINE FIELD birthYear ON Users type int;"
                       "DEFINE FIELD group ON Users type string;")

        await database.query(table_query)

        fake = Faker()
        group_name = DynamicProvider(
            provider_name="group_name",
            elements=["user", "premium", "admin"]
        )
        fake.add_provider(group_name)

        for _ in range(100):
            user_query = (f'CREATE Users SET firstName = "{fake.first_name()}", lastName = "{fake.last_name()}", birthYear = {fake.year()}, group = "{fake.group_name()}";')
            await database.query(user_query)
