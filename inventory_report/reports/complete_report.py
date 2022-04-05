from inventory_report.reports.simple_report import SimpleReport
import json

# open foi utilizado somente para testar os retornos
with open("inventory_report/data/inventory.json") as file:
    data = json.load(file)


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)
        companies_list = {}

        for item in data:
            if item["nome_da_empresa"] not in companies_list:
                companies_list[item["nome_da_empresa"]] = 1
            elif item["nome_da_empresa"] in companies_list:
                companies_list[item["nome_da_empresa"]] += 1

        products_report = ""
        for item in companies_list:
            products_report += f"- {item}: {companies_list[item]}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{products_report}"
        )


# foi utilizado somente para testar os retornos
report = CompleteReport.generate(data)
# print(report)
