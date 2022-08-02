from sqlalchemy import create_engine, text
import reactivex as rx
from reactivex import operators as ops


engine = create_engine("sqlite:///../resources/rexon_metals.db")
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return rx.from_(conn.execute(stmt))


get_all_customers().pipe(ops.map(lambda r: r[0])).subscribe(print)
