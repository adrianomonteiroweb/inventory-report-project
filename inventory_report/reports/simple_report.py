from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        manufactoring_dates = []
        expiration_dates = []
        companies = []

        for product in inventory:
            manufactoring_dates.append(product['data_de_fabricacao'])

            if product['data_de_validade'] > str(datetime.now().today()):
                expiration_dates.append(product['data_de_validade'])

            companies.append(product['nome_da_empresa'])

        return f'Data de fabricação mais antiga: {min(manufactoring_dates)}\n' + f'Data de validade mais próxima: {min(expiration_dates)}\n' + f'''Empresa com maior quantidade de produtos estocados: {
            Counter(companies).most_common()[0][0]
        }\n'''

        # https://www.codegrepper.com/code-examples/whatever/most_common+in+python
        # http://pythonclub.com.br/python-generators.html
