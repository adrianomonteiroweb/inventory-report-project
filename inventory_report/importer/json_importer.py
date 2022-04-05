from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(data):
        json_file = data.split(".")
        if json_file[-1] != "json":
            raise ValueError("Arquivo inválido")
        else:
            with open(data) as file:
                json_file = json.load(file)
                return list(json_file)
