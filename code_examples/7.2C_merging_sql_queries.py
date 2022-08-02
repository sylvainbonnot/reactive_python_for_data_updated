from sqlalchemy import create_engine, text
import reactivex as rx
from reactivex import operators as ops

rootdir = "FULL_PATH_TO_REXON_METALS_DB"
sqlite_prefix = "sqlite:////"
engine = create_engine(sqlite_prefix + rootdir)
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return rx.from_(conn.execute(stmt))


def customer_for_id(customer_id):
    stmt = text("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = :id")
    return rx.from_(conn.execute(stmt, id=customer_id))


# Query customers with IDs 1, 3, and 5
rx.from_([1, 3, 5]).pipe(ops.flat_map(lambda id: customer_for_id(id))).subscribe(
    lambda r: print(r)
)
