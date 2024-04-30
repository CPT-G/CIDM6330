# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent
import pytest

from src.commands import CreateBookmarksTableCommand


class CreateBookmarksTableCommand():
    def test_working(self):
        pass


def test_quit_command():
    pass


@pytest.fixture
def db():
    filename = "test_bookmarks.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()
    os.remove(filename)


def test_create_bookmarks_table_command(db):
    # act and arrange
    commands.CreateBookmarksTableCommand()
    conn = db.connection
    cursor = conn.cursor()

    cursor.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bookmarks' ''')
    # assert
    assert cursor.fetchone()[0] == 1
