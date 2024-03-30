from telegram import User

from database.db_api import commit_user_to_db


def prepare_user_data_for_commit(user: User) -> None:
    user = {
        'chat_id': user.id,
        'username': user.username,
        'first_name': user.first_name
    }
    commit_user_to_db(user)
