import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()
currency_dict = {}


for valute in root.findall('Valute'):
    num_code = valute.find('NumCode').text
    char_code = valute.find('CharCode').text
    currency_dict[num_code] = char_code


print(currency_dict)