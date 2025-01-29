from data_source import nasa_data_source, dog_data_source, meteo_data_source
from db import ShinyDB


def main():
    print("Starting data collection")
    db = ShinyDB()
    sources = (nasa_data_source, dog_data_source, meteo_data_source)
    for source in sources:
        data = source()
        db.save_data(data)

    print("Finished data collection")


if __name__ == "__main__":
    main()
