from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(data):
        xml_file = data.split(".")
        if xml_file[-1] != "xml":
            raise ValueError("Arquivo inválido")
        else:
            with open(data) as file:
                xml_file = ET.parse(file).getroot()
                product_list = []
                for product in xml_file.findall("record"):
                    product_dict = {}
                    for item in product:
                        product_dict[item.tag] = item.text
                    product_list.append(product_dict)
                return product_list

# getroot
# https://stackoverflow.com/questions/647071/python-xml-elementtree-from-a-string-source

# xml.etree
# https://pt.stackoverflow.com/questions/3561/como-criar-e-ler-um-xml-com-python