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


def insert_new_customer(customer_name, region, street_address, city, state, zip_code):
    stmt = text(
        "INSERT INTO CUSTOMER (NAME, REGION, STREET_ADDRESS, CITY, STATE, ZIP) VALUES ("
        ":customer_name, :region, :street_address, :city, :state, :zip_code)"
    )

    result = conn.execute(
        stmt,
        customer_name=customer_name,
        region=region,
        street_address=street_address,
        city=city,
        state=state,
        zip_code=zip_code,
    )
    return rx.just(result.lastrowid)


# Create new customer, emit primary key ID, and query that customer
insert_new_customer(
    "RMS Materials", "Northeast", "5764 Carrier Ln", "Boston", "Massachusetts", "02201"
).pipe(ops.flat_map(lambda i: customer_for_id(i))).subscribe(print)
