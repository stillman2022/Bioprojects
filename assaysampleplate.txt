# Assay and sample assigner.
# Python3, Anthony Stillman. 
import csv, math 

samplelist = []
# original sample csv has samples starting in the second column and second position going down. 
with open('testsampleassay.csv', newline='') as samplelistreader:
    reader = csv.reader(samplelistreader)
    samplelistcsv = list(reader)
# Builind list of samples for CSV.
for i in range(1, len(samplelistcsv)):
    samplelist.append(samplelistcsv[i][1])
# Header for outputted CSV of plate pattern.
headerlist = ['well', 'sample', 'assays']
# Wells for outputted CSV of plate pattern.
wellslist = ['A01', 'A02', 'B01', 'B02', 'C01', 'C02', 'D01', 'D02', 'E01', 'E02', 'F01', 'F02', 'G01', 'G02', 'H01', 'H02', 'I01', 'I02', 'J01', 'J02', 'K01', 'K02', 'L01', 'L02', 'M01', 'M02', 'N01', 'N02', 'O01', 'O02', 'P01', 'P02', 'A03', 'A04', 'B03', 'B04', 'C03', 'C04', 'D03', 'D04', 'E03', 'E04', 'F03', 'F04', 'G03', 'G04', 'H03', 'H04', 'I03', 'I04', 'J03', 'J04', 'K03', 'K04', 'L03', 'L04', 'M03', 'M04', 'N03', 'N04', 'O03', 'O04', 'P03', 'P04', 'A05', 'A06', 'B05', 'B06', 'C05', 'C06', 'D05', 'D06', 'E05', 'E06', 'F05', 'F06', 'G05', 'G06', 'H05', 'H06', 'I05', 'I06', 'J05', 'J06', 'K05', 'K06', 'L05', 'L06', 'M05', 'M06', 'N05', 'N06', 'O05', 'O06', 'P05', 'P06', 'A07', 'A08', 'B07', 'B08', 'C07', 'C08', 'D07', 'D08', 'E07', 'E08', 'F07', 'F08', 'G07', 'G08', 'H07', 'H08', 'I07', 'I08', 'J07', 'J08', 'K07', 'K08', 'L07', 'L08', 'M07', 'M08', 'N07', 'N08', 'O07', 'O08', 'P07', 'P08', 'A09', 'A10', 'B09', 'B10', 'C09', 'C10', 'D09', 'D10', 'E09', 'E10', 'F09', 'F10', 'G09', 'G10', 'H09', 'H10', 'I09', 'I10', 'J09', 'J10', 'K09', 'K10', 'L09', 'L10', 'M09', 'M10', 'N09', 'N10', 'O09', 'O10', 'P09', 'P10', 'A11', 'A12', 'B11', 'B12', 'C11', 'C12', 'D11', 'D12', 'E11', 'E12', 'F11', 'F12', 'G11', 'G12', 'H11', 'H12', 'I11', 'I12', 'J11', 'J12', 'K11', 'K12', 'L11', 'L12', 'M11', 'M12', 'N11', 'N12', 'O11', 'O12', 'P11', 'P12', 'A13', 'A14', 'B13', 'B14', 'C13', 'C14', 'D13', 'D14', 'E13', 'E14', 'F13', 'F14', 'G13', 'G14', 'H13', 'H14', 'I13', 'I14', 'J13', 'J14', 'K13', 'K14', 'L13', 'L14', 'M13', 'M14', 'N13', 'N14', 'O13', 'O14', 'P13', 'P14', 'A15', 'A16', 'B15', 'B16', 'C15', 'C16', 'D15', 'D16', 'E15', 'E16', 'F15', 'F16', 'G15', 'G16', 'H15', 'H16', 'I15', 'I16', 'J15', 'J16', 'K15', 'K16', 'L15', 'L16', 'M15', 'M16', 'N15', 'N16', 'O15', 'O16', 'P15', 'P16', 'A17', 'A18', 'B17', 'B18', 'C17', 'C18', 'D17', 'D18', 'E17', 'E18', 'F17', 'F18', 'G17', 'G18', 'H17', 'H18', 'I17', 'I18', 'J17', 'J18', 'K17', 'K18', 'L17', 'L18', 'M17', 'M18', 'N17', 'N18', 'O17', 'O18', 'P17', 'P18', 'A19', 'A20', 'B19', 'B20', 'C19', 'C20', 'D19', 'D20', 'E19', 'E20', 'F19', 'F20', 'G19', 'G20', 'H19', 'H20', 'I19', 'I20', 'J19', 'J20', 'K19', 'K20', 'L19', 'L20', 'M19', 'M20', 'N19', 'N20', 'O19', 'O20', 'P19', 'P20', 'A21', 'A22', 'B21', 'B22', 'C21', 'C22', 'D21', 'D22', 'E21', 'E22', 'F21', 'F22', 'G21', 'G22', 'H21', 'H22', 'I21', 'I22', 'J21', 'J22', 'K21', 'K22', 'L21', 'L22', 'M21', 'M22', 'N21', 'N22', 'O21', 'O22', 'P21', 'P22', 'A23', 'A24', 'B23', 'B24', 'C23', 'C24', 'D23', 'D24', 'E23', 'E24', 'F23', 'F24', 'G23', 'G24', 'H23', 'H24', 'I23', 'I24', 'J23', 'J24', 'K23', 'K24', 'L23', 'L24', 'M23', 'M24', 'N23', 'N24', 'O23', 'O24', 'P23', 'P24']
# Assays that will be tested by certain types of samples.
M1M2assay = ['assay01', 'assay02', 'assay03', 'assay04', 'assay05', 'assay06', 'assay07', 'assay08', 'assay09', 'assay10', 'assay11', 'assay12', 'assay13']

M3assay = ['assay01', 'assay02', 'assay04', 'assay05', 'assay06', 'assay07', 'assay08', 'assay09', 'assay10']
# Lists to be filled by code.
sampleassay = []

fullassaylist = []

fullsamplelist = []
# Assigning samples their assays based on the sample type (indicated by the initial suffix). If sample has replicates, the assays will be evenly destrubed between the sample replicates.
for i in range(len(samplelist)):
    if samplelist[i][0:2] == 'M1':
        samplecount = samplelist.count(samplelist[i])
        assaylen = len(M1M2assay)
        assayper = assaylen/samplecount
        assayasign = round(assayper)
        samplebeforecount = samplelist[:i].count(samplelist[i])
        sampleaftercount = samplelist[i:].count(samplelist[i])
        sampleassay.append(M1M2assay[samplebeforecount::samplecount])
                
    elif samplelist[i][0:2] == 'M2':
        samplecount = samplelist.count(samplelist[i])
        assaylen = len(M1M2assay)
        assayper = assaylen/samplecount
        assayasign = round(assayper)
        samplebeforecount = samplelist[:i].count(samplelist[i])
        sampleaftercount = samplelist[i:].count(samplelist[i])
        sampleassay.append(M1M2assay[samplebeforecount::samplecount])
        
    elif samplelist[i][0:3] == 'M3':
        samplecount = samplelist.count(samplelist[i])
        assaylen = len(M3assay)
        assayper = assaylen/samplecount
        assayasign = round(assayper)
        samplebeforecount = samplelist[:i].count(samplelist[i])
        sampleaftercount = samplelist[i:].count(samplelist[i])
        sampleassay.append(M3assay[samplebeforecount::samplecount])

    elif samplelist[i][0:1] == '':
        sampleassay.append([])

    else:
        sampleassay.append(['ERROR'])
# Determining the maximum assays given to one sample for late use.
listlength = len(max(sampleassay, key=len))
# Making all samples have the same amount of assays spots by assigning blanks, this is imoprtant for creating platepattern CSV.
for i in range(len(sampleassay)):
    for x in range(listlength - len(sampleassay[i])):
        sampleassay[i].append("")
# Assigning how many times a sample will be tested for an assay.   
for i in range(len(max(sampleassay, key=len))):
    for x in range(len(sampleassay)):
        for y in range(4):
            fullassaylist.append(sampleassay[x][i])
# Creating sample list that matches with the amount of time a sample is tested for an assay. the 'for y in range(4):' in previouse code should match amount of times 'fullsamplelist' is appended.
for sample in samplelist:
    fullsamplelist.append(sample)
    fullsamplelist.append(sample)
    fullsamplelist.append(sample)
    fullsamplelist.append(sample)
# Determining how many plate patterns are needed for the task.
numplatepattern = math.ceil(len(fullassaylist)/384)
# Creating name for plate patterns and creating plate patterns based on the assay and sample list created.
for i in range(numplatepattern):
    name = str(i) + '-sampleassayplatepattern.csv'
    
    with open(name, 'w', newline='') as sampleassayplatepattern:
        write = csv.writer(sampleassayplatepattern)

        write.writerow(headerlist)

        for x in range(384):
            write.writerow([wellslist[x], fullsamplelist[x], fullassaylist[x-(384*i)]])

        sampleassayplatepattern.close()

