import pandas as pd
import argparse
import Data.machine_learning as male

parser = argparse.ArgumentParser(description="Getting the file from the user")
parser.add_argument('-d','--doc', required=True, type=str, help='Insert the name of the excel file being used')
args = parser.parse_args()
parser.print_help()
workbook="%s.xlsx" % args.doc
book='Prediction.xlsx'
cube=pd.read_excel(workbook,sheet_name="Sheet1")
#y_accuracy=male.mach(cube)

new_cube=pd.read_excel(workbook,sheet_name="Sheet2")
y_predic=male.mach(cube,new_cube)


new_cube['Powder load']=y_predic
# Create a Pandas dataframe from the data.
df = pd.DataFrame(new_cube)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(book, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']


writer.save()
