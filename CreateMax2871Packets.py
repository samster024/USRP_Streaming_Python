import DestinationEncoding as D1

class Max2870Reg5:

    def Max2870_Reg5(self, Constant_Register5, Destination_Value, Packet2):

        Element_1 = []
        Element_3 = []
        Element_4 = []
        Element_5 = []
        Element_7 = []
        Element_8 = []
        Element_9 = []
        Element_10 = []
        Element_12 = []
        Element_13 = []
        Element_14 = []

        Element_1.append(False)

        Element_2_Temp = []
        Element_2_Rev = []
        Binary = bin(Constant_Register5[0])[2:].zfill(8)
        Str_Binary = [int(a) for a in str(Binary)]
        Str_Binary_Rev = Str_Binary[::-1]
        for x in range(0, 8):
            if Str_Binary_Rev[x] == 1:
                Element_2_Temp.append(True)
            else:
                Element_2_Temp.append(False)
        Element_2_Rev.append(Element_2_Temp[0])
        Element_2_Rev.append(Element_2_Temp[1])
        Element_2 = Element_2_Rev[::-1]

        for x in range(0, 3):
            Element_3.append(False)

        if Constant_Register5[1] == True:
            Element_4.append(True)
        else:
            Element_4.append(False)

        if Constant_Register5[2] == True:
            Element_5.append(True)
        else:
            Element_5.append(False)

        Element_6_Temp = []
        Element_6_Rev = []
        Binary1 = bin(Constant_Register5[3])[2:].zfill(8)
        Str_Binary1 = [int(a) for a in str(Binary1)]
        Str_Binary_Rev1 = Str_Binary1[::-1]
        for x in range(0, 8):
            if Str_Binary_Rev1[x] == 1:
                Element_6_Temp.append(True)
            else:
                Element_6_Temp.append(False)
        Element_6_Rev.append(Element_6_Temp[0])
        Element_6_Rev.append(Element_6_Temp[1])
        Element_6 = Element_6_Rev[::-1]

        for x in range(0, 3):
            Element_7.append(False)

        if Constant_Register5[4] == True:
            Element_8.append(True)
        else:
            Element_8.append(False)

        for x in range(0, 11):
            Element_9.append(False)

        if Constant_Register5[5] == True:
            Element_10.append(True)
        else:
            Element_10.append(False)

        Element_11_Temp = []
        Element_11_Rev = []
        Binary2 = bin(Constant_Register5[6])[2:].zfill(8)
        Str_Binary2 = [int(a) for a in str(Binary2)]
        Str_Binary_Rev2 = Str_Binary2[::-1]
        for x in range(0, 8):
            if Str_Binary_Rev2[x] == 1:
                Element_11_Temp.append(True)
            else:
                Element_11_Temp.append(False)
        Element_11_Rev.append(Element_11_Temp[0])
        Element_11_Rev.append(Element_11_Temp[1])
        Element_11_Rev.append(Element_11_Temp[2])
        Element_11 = Element_11_Rev[::-1]

        if Constant_Register5[7] == True:
            Element_12.append(True)
        else:
            Element_12.append(False)

        if Constant_Register5[8] == True:
            Element_13.append(True)
        else:
            Element_13.append(False)

        if Constant_Register5[9] == True:
            Element_14.append(True)
        else:
            Element_14.append(False)

        Element = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6 + Element_7 + Element_8 + Element_9 + Element_10 + Element_11 + Element_12 + Element_13 + Element_14

        Element_Bin = []
        for x in range(0, 32):
            if Element[x] == True:
                Element_Bin.append(1)
            else:
                Element_Bin.append(0)
        Element_Num = ''.join(str(e) for e in Element_Bin)
        Element_Value = int(Element_Num, 2)

        Packet2.append(Destination_Value)
        Packet2.append(40)
        Packet2.append(Element_Value)

        return (Packet2)

class Max2870Reg4:

    def Max2870_Reg4(self, Constant_Register4, Destination_Value, Packet3):

        Element_1 = []
        Element_2 = []
        Element_3 = []
        Element_4 = []
        Element_5 = []
        Element_6 = []
        Element_7 = []
        Element_8 = []
        Element_10 = []
        Element_11 = []
        Element_12 = []
        Element_13 = []
        Element_14 = []
        Element_16 = []
        Element_18 = []
        Element_19 = []
        Element_20 = []

        Element_1.append(False)

        Element_2.append(True)

        Element_3.append(True)

        if Constant_Register4[0] == True:
            Element_4.append(True)
        else:
            Element_4.append(False)

        if Constant_Register4[1] == True:
            Element_5.append(True)
        else:
            Element_5.append(False)

        if Constant_Register4[2] == True:
            Element_6.append(True)
        else:
            Element_6.append(False)

        Element_9_Temp = []
        Element_9_Temp1 = []
        Binary_4 = bin(Constant_Register4[5])[2:].zfill(16)
        Str_Binary_4 = [int(a) for a in str(Binary_4)]
        Str_Binary_4_Rev = Str_Binary_4[::-1]
        for x in range(0, 16):
            if Str_Binary_4_Rev[x] == 1:
                Element_9_Temp.append(True)
            else:
                Element_9_Temp.append(False)
        for x in range(0, 10):
            Element_9_Temp1.append(Element_9_Temp[x])
        Str_Binary_Rev_4 = Element_9_Temp1[::-1]
        Element_7.append(Str_Binary_Rev_4[0])
        Element_7.append(Str_Binary_Rev_4[1])

        if Constant_Register4[3] == True:
            Element_8.append(True)
        else:
            Element_8.append(False)

        Element_9_Temp = []
        Element_9_Temp1 = []
        Binary_3 = bin(Constant_Register4[4])[2:].zfill(8)
        Str_Binary_3 = [int(a) for a in str(Binary_3)]
        Str_Binary_3_Rev = Str_Binary_3[::-1]
        for x in range(0, 8):
            if Str_Binary_3_Rev[x] == 1:
                Element_9_Temp.append(True)
            else:
                Element_9_Temp.append(False)
        for x in range(0, 3):
            Element_9_Temp1.append(Element_9_Temp[x])
        Element_9 = Element_9_Temp1[::-1]

        Element_10.append(Str_Binary_Rev_4[2])
        Element_10.append(Str_Binary_Rev_4[3])
        Element_10.append(Str_Binary_Rev_4[4])
        Element_10.append(Str_Binary_Rev_4[5])
        Element_10.append(Str_Binary_Rev_4[6])
        Element_10.append(Str_Binary_Rev_4[7])
        Element_10.append(Str_Binary_Rev_4[8])
        Element_10.append(Str_Binary_Rev_4[9])

        if Constant_Register4[6] == True:
            Element_11.append(True)
        else:
            Element_11.append(False)

        if Constant_Register4[7] == True:
            Element_12.append(True)
        else:
            Element_12.append(False)

        if Constant_Register4[8] == True:
            Element_13.append(True)
        else:
            Element_13.append(False)

        if Constant_Register4[9] == True:
            Element_14.append(True)
        else:
            Element_14.append(False)

        Element_15_Temp = []
        Element_15_Temp1 = []
        Binary_5 = bin(Constant_Register4[10])[2:].zfill(8)
        Str_Binary_5 = [int(a) for a in str(Binary_5)]
        Str_Binary_5_Rev = Str_Binary_5[::-1]
        for x in range(0, 8):
            if Str_Binary_5_Rev[x] == 1:
                Element_15_Temp.append(True)
            else:
                Element_15_Temp.append(False)
        for x in range(0, 2):
            Element_15_Temp1.append(Element_15_Temp[x])
        Element_15 = Element_15_Temp1[::-1]

        if Constant_Register4[11] == True:
            Element_16.append(True)
        else:
            Element_16.append(False)

        Element_17_Temp = []
        Element_17_Temp1 = []
        Binary_6 = bin(Constant_Register4[12])[2:].zfill(8)
        Str_Binary_6 = [int(a) for a in str(Binary_6)]
        Str_Binary_6_Rev = Str_Binary_6[::-1]
        for x in range(0, 8):
            if Str_Binary_6_Rev[x] == 1:
                Element_17_Temp.append(True)
            else:
                Element_17_Temp.append(False)
        for x in range(0, 2):
            Element_17_Temp1.append(Element_17_Temp[x])
        Element_17 = Element_17_Temp1[::-1]

        if Constant_Register4[13] == True:
            Element_18.append(True)
        else:
            Element_18.append(False)

        if Constant_Register4[14] == True:
            Element_19.append(True)
        else:
            Element_19.append(False)

        if Constant_Register4[15] == True:
            Element_20.append(True)
        else:
            Element_20.append(False)

        Element1 = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6 + Element_7 + Element_8 + Element_9 + Element_10 + Element_11 + Element_12 + Element_13 + Element_14 + Element_15 + Element_16 + Element_17 + Element_18 + Element_19 + Element_20

        Element1_Bin = []
        for x in range(0, 32):
            if Element1[x] == True:
                Element1_Bin.append(1)
            else:
                Element1_Bin.append(0)
        Element1_Num = ''.join(str(e) for e in Element1_Bin)
        Element1_Value = int(Element1_Num, 2)

        Packet3.append(Destination_Value)
        Packet3.append(40)
        Packet3.append(Element1_Value)

        return (Packet3)

class Max2870Reg3:

    def Max2870_Reg3(self, Constant_Register3, Destination_Value, Packet4):

        Element_2 = []
        Element_3 = []
        Element_4 = []
        Element_5 = []
        Element_6 = []
        Element_9 = []
        Element_10 = []
        Element_11 = []

        Element_1_Temp = []
        Element_1_Temp1 = []
        Binary_7 = bin(Constant_Register3[0])[2:].zfill(8)
        Str_Binary_7 = [int(a) for a in str(Binary_7)]
        Str_Binary_7_Rev = Str_Binary_7[::-1]
        for x in range(0, 8):
            if Str_Binary_7_Rev[x] == 1:
                Element_1_Temp.append(True)
            else:
                Element_1_Temp.append(False)
        for x in range(0, 6):
            Element_1_Temp1.append(Element_1_Temp[x])
        Element_1 = Element_1_Temp1[::-1]

        if Constant_Register3[1] == True:
            Element_2.append(True)
        else:
            Element_2.append(False)

        for x in range(0, 5):
            Element_3.append(False)

        if Constant_Register3[2] == True:
            Element_4.append(True)
        else:
            Element_4.append(False)

        if Constant_Register3[3] == True:
            Element_5.append(True)
        else:
            Element_5.append(False)

        if Constant_Register3[4] == True:
            Element_6.append(True)
        else:
            Element_6.append(False)

        Element_7_Temp = []
        Element_7_Temp1 = []
        Binary_8 = bin(Constant_Register3[5])[2:].zfill(8)
        Str_Binary_8 = [int(a) for a in str(Binary_8)]
        Str_Binary_8_Rev = Str_Binary_8[::-1]
        for x in range(0, 8):
            if Str_Binary_8_Rev[x] == 1:
                Element_7_Temp.append(True)
            else:
                Element_7_Temp.append(False)
        for x in range(0, 2):
            Element_7_Temp1.append(Element_7_Temp[x])
        Element_7 = Element_7_Temp1[::-1]

        Element_8_Temp = []
        Element_8_Temp1 = []
        Binary_9 = bin(Constant_Register3[6])[2:].zfill(16)
        Str_Binary_9 = [int(a) for a in str(Binary_9)]
        Str_Binary_9_Rev = Str_Binary_9[::-1]
        for x in range(0, 16):
            if Str_Binary_9_Rev[x] == 1:
                Element_8_Temp.append(True)
            else:
                Element_8_Temp.append(False)
        for x in range(0, 12):
            Element_8_Temp1.append(Element_8_Temp[x])
        Element_8 = Element_8_Temp1[::-1]

        if Constant_Register3[7] == True:
            Element_9.append(True)
        else:
            Element_9.append(False)

        if Constant_Register3[8] == True:
            Element_10.append(True)
        else:
            Element_10.append(False)

        if Constant_Register3[9] == True:
            Element_11.append(True)
        else:
            Element_11.append(False)

        Element2 = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6 + Element_7 + Element_8 + Element_9 + Element_10 + Element_11

        Element2_Bin = []
        for x in range(0, 32):
            if Element2[x] == True:
                Element2_Bin.append(1)
            else:
                Element2_Bin.append(0)
        Element2_Num = ''.join(str(e) for e in Element2_Bin)
        Element2_Value = int(Element2_Num, 2)

        Packet4.append(Destination_Value)
        Packet4.append(40)
        Packet4.append(Element2_Value)

        return (Packet4)

class Max2870Reg2:

    def Max2870_Reg2(self, Constant_Register2, Destination_Value, Packet5):

        Element_1 = []
        Element_4 = []
        Element_5 = []
        Element_7 = []
        Element_9 = []
        Element_10 = []
        Element_11 = []
        Element_12 = []
        Element_13 = []
        Element_14 = []
        Element_15 = []
        Element_16 = []
        Element_17 = []

        if Constant_Register2[0] == True:
            Element_1.append(True)
        else:
            Element_1.append(False)

        Element_2_Temp = []
        Element_2_Temp1 = []
        Binary_10 = bin(Constant_Register2[1])[2:].zfill(8)
        Str_Binary_10 = [int(a) for a in str(Binary_10)]
        Str_Binary_10_Rev = Str_Binary_10[::-1]
        for x in range(0, 8):
            if Str_Binary_10_Rev[x] == 1:
                Element_2_Temp.append(True)
            else:
                Element_2_Temp.append(False)
        for x in range(0, 2):
            Element_2_Temp1.append(Element_2_Temp[x])
        Element_2 = Element_2_Temp1[::-1]

        Element_3_Temp = []
        Element_3_Temp1 = []
        Binary_11 = bin(Constant_Register2[2])[2:].zfill(8)
        Str_Binary_11 = [int(a) for a in str(Binary_11)]
        Str_Binary_11_Rev = Str_Binary_11[::-1]
        for x in range(0, 8):
            if Str_Binary_11_Rev[x] == 1:
                Element_3_Temp.append(True)
            else:
                Element_3_Temp.append(False)
        for x in range(0, 3):
            Element_3_Temp1.append(Element_3_Temp[x])
        Element_3 = Element_3_Temp1[::-1]

        if Constant_Register2[3] == True:
            Element_4.append(True)
        else:
            Element_4.append(False)

        if Constant_Register2[4] == True:
            Element_5.append(True)
        else:
            Element_5.append(False)

        Element_6_Temp = []
        Element_6_Temp1 = []
        Binary_12 = bin(Constant_Register2[5])[2:].zfill(16)
        Str_Binary_12 = [int(a) for a in str(Binary_12)]
        Str_Binary_12_Rev = Str_Binary_12[::-1]
        for x in range(0, 16):
            if Str_Binary_12_Rev[x] == 1:
                Element_6_Temp.append(True)
            else:
                Element_6_Temp.append(False)
        for x in range(0, 10):
            Element_6_Temp1.append(Element_6_Temp[x])
        Element_6 = Element_6_Temp1[::-1]

        if Constant_Register2[6] == True:
            Element_7.append(True)
        else:
            Element_7.append(False)

        Element_8_Temp = []
        Element_8_Temp1 = []
        Binary_13 = bin(Constant_Register2[7])[2:].zfill(8)
        Str_Binary_13 = [int(a) for a in str(Binary_13)]
        Str_Binary_13_Rev = Str_Binary_13[::-1]
        for x in range(0, 8):
            if Str_Binary_13_Rev[x] == 1:
                Element_8_Temp.append(True)
            else:
                Element_8_Temp.append(False)
        for x in range(0, 4):
            Element_8_Temp1.append(Element_8_Temp[x])
        Element_8 = Element_8_Temp1[::-1]

        if Constant_Register2[8] == True:
            Element_9.append(True)
        else:
            Element_9.append(False)

        if Constant_Register2[9] == True:
            Element_10.append(True)
        else:
            Element_10.append(False)

        if Constant_Register2[10] == True:
            Element_11.append(True)
        else:
            Element_11.append(False)

        if Constant_Register2[11] == True:
            Element_12.append(True)
        else:
            Element_12.append(False)

        if Constant_Register2[12] == True:
            Element_13.append(True)
        else:
            Element_13.append(False)

        if Constant_Register2[13] == True:
            Element_14.append(True)
        else:
            Element_14.append(False)

        if Constant_Register2[14] == True:
            Element_15.append(True)
        else:
            Element_15.append(False)

        if Constant_Register2[15] == True:
            Element_16.append(True)
        else:
            Element_16.append(False)

        if Constant_Register2[16] == True:
            Element_17.append(True)
        else:
            Element_17.append(False)

        Element3 = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6 + Element_7 + Element_8 + Element_9 + Element_10 + Element_11 + Element_12 + Element_13 + Element_14 + Element_15 + Element_16 + Element_17

        Element3_Bin = []
        for x in range(0, 32):
            if Element3[x] == True:
                Element3_Bin.append(1)
            else:
                Element3_Bin.append(0)
        Element3_Num = ''.join(str(e) for e in Element3_Bin)
        Element3_Value = int(Element3_Num, 2)

        Packet5.append(Destination_Value)
        Packet5.append(40)
        Packet5.append(Element3_Value)

        return (Packet5)

class Max2870Reg1:

    def Max2870_Reg1(self, Constant_Register1, Destination_Value, Packet6):

        Element_1 = []
        Element_6 = []
        Element_7 = []
        Element_8 = []

        Element_1.append(False)

        Element_2_Temp = []
        Element_2_Temp1 = []
        Binary_14 = bin(Constant_Register1[0])[2:].zfill(8)
        Str_Binary_14 = [int(a) for a in str(Binary_14)]
        Str_Binary_14_Rev = Str_Binary_14[::-1]
        for x in range(0, 8):
            if Str_Binary_14_Rev[x] == 1:
                Element_2_Temp.append(True)
            else:
                Element_2_Temp.append(False)
        for x in range(0, 2):
            Element_2_Temp1.append(Element_2_Temp[x])
        Element_2 = Element_2_Temp1[::-1]

        Element_3_Temp = []
        Element_3_Temp1 = []
        Binary_15 = bin(Constant_Register1[1])[2:].zfill(8)
        Str_Binary_15 = [int(a) for a in str(Binary_15)]
        Str_Binary_15_Rev = Str_Binary_15[::-1]
        for x in range(0, 8):
            if Str_Binary_15_Rev[x] == 1:
                Element_3_Temp.append(True)
            else:
                Element_3_Temp.append(False)
        for x in range(0, 2):
            Element_3_Temp1.append(Element_3_Temp[x])
        Element_3 = Element_3_Temp1[::-1]

        Element_4_Temp = []
        Element_4_Temp1 = []
        Binary_16 = bin(Constant_Register1[2])[2:].zfill(16)
        Str_Binary_16 = [int(a) for a in str(Binary_16)]
        Str_Binary_16_Rev = Str_Binary_16[::-1]
        for x in range(0, 16):
            if Str_Binary_16_Rev[x] == 1:
                Element_4_Temp.append(True)
            else:
                Element_4_Temp.append(False)
        for x in range(0, 12):
            Element_4_Temp1.append(Element_4_Temp[x])
        Element_4 = Element_4_Temp1[::-1]

        Element_5_Temp = []
        Element_5_Temp1 = []
        Binary_17 = bin(Constant_Register1[3])[2:].zfill(16)
        Str_Binary_17 = [int(a) for a in str(Binary_17)]
        Str_Binary_17_Rev = Str_Binary_17[::-1]
        for x in range(0, 16):
            if Str_Binary_17_Rev[x] == 1:
                Element_5_Temp.append(True)
            else:
                Element_5_Temp.append(False)
        for x in range(0, 12):
            Element_5_Temp1.append(Element_5_Temp[x])
        Element_5 = Element_5_Temp1[::-1]

        if Constant_Register1[4] == True:
            Element_6.append(True)
        else:
            Element_6.append(False)

        if Constant_Register1[5] == True:
            Element_7.append(True)
        else:
            Element_7.append(False)

        if Constant_Register1[6] == True:
            Element_8.append(True)
        else:
            Element_8.append(False)

        Element4 = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6 + Element_7 + Element_8

        Element4_Bin = []
        for x in range(0, 32):
            if Element4[x] == True:
                Element4_Bin.append(1)
            else:
                Element4_Bin.append(0)
        Element4_Num = ''.join(str(e) for e in Element4_Bin)
        Element4_Value = int(Element4_Num, 2)

        Packet6.append(Destination_Value)
        Packet6.append(40)
        Packet6.append(Element4_Value)

        return (Packet6)

class Max2870Reg0:

    def Max2870_Reg0(self, Constant_Register0, Destination_Value, Packet7):

        Element_1 = []
        Element_4 = []
        Element_5 = []
        Element_6 = []

        if Constant_Register0[0] == True:
            Element_1.append(True)
        else:
            Element_1.append(False)

        Element_2_Temp = []
        Binary_18 = bin(Constant_Register0[1])[2:].zfill(16)
        Str_Binary_18 = [int(a) for a in str(Binary_18)]
        Str_Binary_18_Rev = Str_Binary_18[::-1]
        for x in range(0, 16):
            if Str_Binary_18_Rev[x] == 1:
                Element_2_Temp.append(True)
            else:
                Element_2_Temp.append(False)
        Element_2 = Element_2_Temp[::-1]

        Element_3_Temp = []
        Element_3_Temp1 = []
        Binary_19 = bin(Constant_Register0[2])[2:].zfill(16)
        Str_Binary_19 = [int(a) for a in str(Binary_19)]
        Str_Binary_19_Rev = Str_Binary_19[::-1]
        for x in range(0, 16):
            if Str_Binary_19_Rev[x] == 1:
                Element_3_Temp.append(True)
            else:
                Element_3_Temp.append(False)
        for x in range(0, 12):
            Element_3_Temp1.append(Element_3_Temp[x])
        Element_3 = Element_3_Temp1[::-1]

        if Constant_Register0[3] == True:
            Element_4.append(True)
        else:
            Element_4.append(False)

        if Constant_Register0[4] == True:
            Element_5.append(True)
        else:
            Element_5.append(False)

        if Constant_Register0[5] == True:
            Element_6.append(True)
        else:
            Element_6.append(False)

        Element5 = Element_1 + Element_2 + Element_3 + Element_4 + Element_5 + Element_6

        Element5_Bin = []
        for x in range(0, 32):
            if Element5[x] == True:
                Element5_Bin.append(1)
            else:
                Element5_Bin.append(0)
        Element5_Num = ''.join(str(e) for e in Element5_Bin)
        Element5_Value = int(Element5_Num, 2)

        Packet7.append(Destination_Value)
        Packet7.append(40)
        Packet7.append(Element5_Value)
        return (Packet7)

def Create_Max_2871_Packets(Constant_Register0, Constant_Register1, Constant_Register2, Constant_Register3, Constant_Register4, Constant_Register5, Device_Sub_Function_TX, Destination):

    Destination_Value = D1.Destinattion(Destination)

    Packet1 = []
    Packet2 = []
    Packet3 = []
    Packet4 = []
    Packet5 = []
    Packet6 = []
    Packet7 = []

    if Device_Sub_Function_TX == 0:
        Or_1 = 1
    else:
        Or_1 = 2

    Or_Function = Or_1 | 1610612736

    Packet1.append(Destination_Value)
    Packet1.append(36)
    Packet1.append(Or_Function)

    Output = []

    O0 = Packet1
    Output.append(O0)

    Reg5 = Max2870Reg5()
    O1 = Reg5.Max2870_Reg5(Constant_Register5, Destination_Value, Packet2)
    Output.append(O1)

    Reg4 = Max2870Reg4()
    O2 = Reg4.Max2870_Reg4(Constant_Register4, Destination_Value, Packet3)
    Output.append(O2)

    Reg3 = Max2870Reg3()
    O3 = Reg3.Max2870_Reg3(Constant_Register3, Destination_Value, Packet4)
    Output.append(O3)

    Reg2 = Max2870Reg2()
    O4 = Reg2.Max2870_Reg2(Constant_Register2, Destination_Value, Packet5)
    Output.append(O4)

    Reg1 = Max2870Reg1()
    O5 = Reg1.Max2870_Reg1(Constant_Register1, Destination_Value, Packet6)
    Output.append(O5)

    Reg0 = Max2870Reg0()
    O6 = Reg0.Max2870_Reg0(Constant_Register0, Destination_Value, Packet7)
    Output.append(O6)

    return (Output)