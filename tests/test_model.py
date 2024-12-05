from sqlalchemy import text


def test_example(db_session):
    # Example: Add and query something from the database
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1