from datetime import datetime as dt

from telegram import User

from database.db_api import commit_user_to_db


def prepare_user_data_for_commit(user: User) -> None:
    user = {
        'chat_id': user.id, 'username': user.username,
        'first_name': user.first_name,'created_at': dt.now(),
    }
    commit_user_to_db(user)
