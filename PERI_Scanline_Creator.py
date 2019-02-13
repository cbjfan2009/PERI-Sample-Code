import csv
import tkMessageBox
def process_complete():
    tkMessageBox.showinfo("Processing Complete!", "File is at: " + save_path + " and has scanlines")
import tkFileDialog



file_path = tkFileDialog.askopenfilename()
save_path = tkFileDialog.asksaveasfilename()
new_file_data = []
scanlines = []
scanlines_with_checkdigit = []
annual = "00002000" #annual represents $20.00, /
# right justified, left-filled with 0's to be 8 digits long
life_time = "00020000" #life_time represents $200.00 right justified, left-filled /
# with 0's to be 8 digits long
with open(file_path, "r") as peri:
    reader = csv.reader(peri)
    for row in reader:
        new_file_data.append(row) #loops through each row in CSV, holds values in memory


header = new_file_data.pop(0) #removes csv header from new_file_data to avoid conflict while iterating over scanlines


for row in new_file_data:
        scanlines.append("0" + row[0] + annual + life_time)#loops through and give the first column with annual and lifetime numbers concatenated (25 digits)

for number in scanlines: #number crunching for calculating the checkdigit
    pos1 = int(number[0]) * 3
    pos2 = int(number[1]) * 7
    pos3 = int(number[2]) * 1
    pos4 = int(number[3]) * 3
    pos5 = int(number[4]) * 7
    pos6 = int(number[5]) * 1
    pos7 = int(number[6]) * 3
    pos8 = int(number[7]) * 7
    pos9 = int(number[8]) * 1
    pos10 = int(number[9]) * 3
    pos11 = int(number[10]) * 7
    pos12 = int(number[11]) * 1
    pos13 = int(number[12]) * 3
    pos14 = int(number[13]) * 7
    pos15 = int(number[14]) * 1
    pos16 = int(number[15]) * 3
    pos17 = int(number[16]) * 7
    pos18 = int(number[17]) * 1
    pos19 = int(number[18]) * 3
    pos20 = int(number[19]) * 3
    pos21 = int(number[20]) * 1
    pos22 = int(number[21]) * 3
    pos23 = int(number[22]) * 7
    pos24 = int(number[23]) * 1
    pos25 = int(number[24]) * 3
    sum_1 = int(pos1 + pos2 + pos3 + pos4 + pos5 + pos6 + pos7 + pos8 + pos9 + pos10 + pos11 + pos12 + pos13 + pos14 + pos15 + pos16 + pos17 + pos18 + pos19 + pos20 + pos21 + pos22 + pos23 + pos24 + pos25)

    checkdigit = 10 - (sum_1 % 10)

    if checkdigit > 9: #adds a 0 checkdigit if it's > 9, adds checkdigit if <=9
        scanlines_with_checkdigit.append(str(number) + "0")
    else:
        scanlines_with_checkdigit.append(str(number) + str(checkdigit))


scanlines_with_checkdigit_list = [] #list of string scanlines_with_checkdigit turned into a list of lists


for numbers in scanlines_with_checkdigit: #append string-scanlines to list above
    scanlines_with_checkdigit_list.append([numbers])

final_list = []

for i in range(len(scanlines_with_checkdigit_list)):
    final_list.append([new_file_data[i][0]] + scanlines_with_checkdigit_list[i] + new_file_data[i][2:])


with open(save_path, "wb") as peri_with_scanlines:
    writer = csv.writer(peri_with_scanlines, delimiter=',')
    writer.writerows([header])
    writer.writerows(final_list)

process_complete()


