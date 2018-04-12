import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse

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


def main():
     # Taking command line arguments from users
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input_xml', help='define the input xml file', type=str, required=True)
    parser.add_argument('-out', '--output_csv', help='define the output file ', type=str, required=True)
    args = parser.parse_args()

    xml_df = xml_to_csv(args.input_xml)
    xml_df.to_csv(args.output_csv, index=None)
    print('Successfully converted xml to csv.')


main()
