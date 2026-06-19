from extract import extract
from transform import transform
from load import create_table, load
def run(engine):
    print("Extract...")
    raw = extract()

    print("Transform...")
    rows = transform(raw)

    print("Load...")
    create_table(engine)
    load(engine, rows)

    print("Pipeline done!")

if __name__ == "__main__":
    run()
