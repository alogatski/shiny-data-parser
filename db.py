

class ShinyDB:
    def __init__(self):
        self.db = "shiny_db"

    def save_data(self, data: list[dict]) -> None:
        print(f"Success saving in {self.db}")
