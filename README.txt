I work as an electrical and instrumentation engineer at Eastman Chemcial. We have lots of instruments throughout our plants that can be descirbed by their model number. I wrote this program to assist my work.

Purpose:
To take an instrument's information (model number, manufacturer, and device) and output a detail csv (excel) file that explains each letter of the model number.
It should funciton entirely wihtin the command line. This way I can create a front end later.


CSV INSTRUMENT CATALOG/DATASHEET
There is a folder titled 'data_sheets' containing csv files. Each of the CSV files are different instruments and their catalogs. The format of these csv files is very important for the functionality of my program

Lets define some vocabulary:
Spec - This is a descriptor. It describes one of the options that can be speced out for an instrument.
Options - Options contain code/description combinations. All of the code/descirption cobinations describe all of the options for a single spec
Code - A code is the alpha-numeric representation of an option. For instance, model numbers will often use codes like 'A', 'B', and 'C' to describe different options.
Description - The description is a string of characters (also know as a sentence) that explains what a code represents. For instance, code 'A' means this instrument's power spec is 'Wired'

Other Requirments:
- All Specs need to be on their own row without a comma. They should only take up a single cell when viewing a csv in Excel
- All options need to take up exactly 2 columns. This first column is the code and the second is the description
- The CSV file should be ordered as (Spec1, Options1, Spec2, Options2) 

Example:
Model
3051S, Scalable Pressure Transmitter
Performance class
1, Ultra: 0.025% span accuracy - 200:1 rangedown - 15-year stability - 15-year limited warranty 
2, Classic: 0.035% span accuracy - 150:1 rangedown - 15-year stability
3, Ultra for Flow: 0.04% reading accuracy - 200:1 turndown - 15-year stability - 15-year limited warranty 
Connection type
C, Coplanar
Measurement type
D, Differential 
G, Gage
A, Absolute 
...

- The CSV's final row should be a single column that says "END" (no comma)
- The CSV's file name should be: MANUFACTURER_DEVICE.csv (ROSEMOUNT_3051S-COPLANAR.csv or JMS_RTD.csv)
- an '_' underscore should seperate the manufactuer and device. Use a '/' or '-' to show spaces if two words are needed


MAIN.py
To run this program, execture main.py. This is where I connected all of the parts to build the final product.


MANUFAC_AND_DEVICES.py
This code reads the files located in 'data_sheets' directory. It pulls the files names as strings and stores the available manufacturers and devices.
I wrote it this way intentionally. Using this script we can scale this program with additinoal spec sheets for new instruments. Adding the csv file would automatically integrate into the program 


CSV_TO_DICT.py
This file takes the chosen instrument's spec sheet in csv form. It returns a dictionary of lists holding the Specs, Options, Codes, and Descriptions for said instrument.
