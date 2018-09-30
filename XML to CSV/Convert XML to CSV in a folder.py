
# coding: utf-8

# In[1]:


import os

# To iterate over all files in the folder
import glob

# To create dataframe from all the XML files
import pandas as pd

# To parse XML document
import xml.etree.ElementTree as ET


# #### Function to read xml files in a folder iteratively and return a pandas dataframe with information
# 
# #### The XML structure for the code is (this was done for converting annotated images information in XML to csv):
# 
# ![alt text](sampleXMLstructure.PNG "Sample XML")

# In[2]:


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


# In[3]:


def main():
    xml_df = xml_to_csv('C:/Users/Abhay/Desktop/IMAGE/All XMLs')
    xml_df.to_csv('C:/Users/Abhay/Desktop/IMAGE/image_labels.csv', index=None)
    print('Successfully converted xml to csv.')


main()

