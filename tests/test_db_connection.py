from ags.db.io import get_connection


def test_db_connection():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT 1;")
        result = cur.fetchone()
    conn.close()
    assert result[0] == 1
