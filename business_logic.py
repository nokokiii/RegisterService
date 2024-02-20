from surrealdb import Surreal

class Database:
    def __init__(self):
        """
        Here we'll initialize connection to database
        """
        self.db = Surreal("http://localhost:8000")

class Logic:
    def __init__(self):
        """
        Here we'll initialize connection to database
        """
        self.db = Database().db
        await self.db.connect()
        await self.db.signin({"user": "root", "pass": "root"})
        await self.db.use("po", "users")

    def users_list_controller(self) -> tuple[[], int]:
        """
        Return list of all users
        """
        return await self.db.select("users"), 200

    def user_controller(self, id: int) -> tuple[{}, int]:
        """
        Return user by id
        """
        user_id = f'Users:{id}'
        return await self.db.select(user_id), 200

    def create_user_controller(self) -> int:
        """
        Create new user
        """
        try:
            await self.db.create('Users', {
                'name': 'John'})
        except:
            return 400
        return 201

    def update_user_controller(self, id: int) -> int:
        """
        Update user
        """
        try:
            await self.db.update(f'Users:{id}', {
                'name': 'John'})
        except:
            return 400
        return 200

    def delete_user_controller(self, id: int) -> int:
        """
        Delete user
        """
        try:
            await self.db.delete(f'Users:{id}')
        except:
            return 400
        return 200
