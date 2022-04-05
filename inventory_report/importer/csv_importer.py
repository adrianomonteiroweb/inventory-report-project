from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(data):
        csv_file = data.split(".")
        if csv_file[-1] != "csv":
            raise ValueError("Arquivo inválido")
        else:
            with open(data) as file:
                csv_file = csv.DictReader(file)
                return list(csv_file)
