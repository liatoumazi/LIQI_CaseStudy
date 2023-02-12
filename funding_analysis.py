# Objective:
# Prepare a report for the lending manager to help him/her decide whether to approve the short-term (<12 months) funding request 
# from ABC Company
# 
# To do this you have at your disposal:
#   The last filed financial statements as of 12/31/2021
#   Current account transactions during 2022 
#   Any other public data sources you can think of

# Requirements:
# The report must specify as its main output the maximum amount that can be granted to the company (along with the rationale for the choice)


# libraries
import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

df_fs = pd.read_csv("Transactions_CompanyABC.csv")

# load and parse the file
xmlTree = ET.parse('bilancio_test.xml')

elemList = []

for elem in xmlTree.iter():
    elemList.append(elem.tag)

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

with open('bilancio_test.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'lxml')
ls= [] # Create empty list
for tag in elemList:
    for l in soup.find_all(tag):
        ls.append(l.string) # add each element one by one to the list

new_ls = list(filter(None,ls))
is_data = list(zip(*[iter(new_ls)]*6))
print(ls)



# def intr_doc(xml_doc):
#     attr = xml_doc.attrib

#     for tag in elemList:
#         for xml in xml_doc.iter(tag):
#             doc_dict = attr.copy()
#             doc_dict.update(xml.attrib)
#             doc_dict['data'] = xml.text

#             yield doc_dict

# df_current = pd.DataFrame(list(intr_doc(xmlTree.getroot())))

# print(df_current)


# root = tree.getroot()
# list = set()
# for child in root.iter():
#     list.add(child.tag)
# print(list)


# for i in root.findall('xbrl'):
#     item = i.find("context").text
#     print(item)

# for item in root[0]:
#     print(item.tag, item.attrib)
