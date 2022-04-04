import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(csl, file, report_type):
        file_type = file.split(".")

        if file_type[-1] == "csv":
            with open(file, 'r') as file:
                reader_csv = csv.DictReader(file, delimiter=",", quotechar='"')
                list_csv = [row_csv for row_csv in reader_csv]
                return Inventory.conditional_type(list_csv, report_type)

    def conditional_type(file, report_type):
        if report_type == "simples":
            return SimpleReport.generate(file)
        else:
            return CompleteReport.generate(file)
