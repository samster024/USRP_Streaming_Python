import math
import TuneLO_UBX as I1
import FormatRadioCommand as O2
import EncodingStream as O3

class SetLO_UBX:

    def Set_LO_UBX(self, Target_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination):

        if Target_Frequency < 10000000:
            Coerced_Frequency = 10000000
        elif Target_Frequency > 6000000000:
            Coerced_Frequency = 6000000000
        else:
            Coerced_Frequency = Target_Frequency

        if Device_Sub_Function == 0:

            Element = []

            if 2500000000 < Coerced_Frequency <= 6000000000:
                Element.append(True)
            else:
                Element.append(False)

            if 2200000000 < Coerced_Frequency <= 2500000000:
                Element.append(True)
            else:
                Element.append(False)

            if 1000000000 < Coerced_Frequency <= 2200000000:
                Element.append(True)
            else:
                Element.append(False)

            if 800000000 < Coerced_Frequency <= 1000000000:
                Element.append(True)
            else:
                Element.append(False)

            if 500000000 < Coerced_Frequency <= 800000000:
                Element.append(True)
            else:
                Element.append(False)

            if Coerced_Frequency < 500000000:
                Element.append(True)
            else:
                Element.append(False)

            Element_Bin = []
            for x in range(0, 6):
                if Element[x] == True:
                    Element_Bin.append(1)
                else:
                    Element_Bin.append(0)
            Element_Num = ''.join(str(e) for e in Element_Bin)
            Element5_Value = int(Element_Num, 2)

            Selected_band_index = int(math.log(Element5_Value, 2))

        else:

            Element = []

            if 2500000000 < Coerced_Frequency <= 6000000000:
                Element.append(True)
            else:
                Element.append(False)

            if 2200000000 < Coerced_Frequency <= 2500000000:
                Element.append(True)
            else:
                Element.append(False)

            if 1500000000 < Coerced_Frequency <= 2200000000:
                Element.append(True)
            else:
                Element.append(False)

            if 1000000000 < Coerced_Frequency <= 1500000000:
                Element.append(True)
            else:
                Element.append(False)

            if 800000000 < Coerced_Frequency <= 1000000000:
                Element.append(True)
            else:
                Element.append(False)

            if 500000000 < Coerced_Frequency <= 800000000:
                Element.append(True)
            else:
                Element.append(False)

            if 100000000 < Coerced_Frequency <= 500000000:
                Element.append(True)
            else:
                Element.append(False)

            if Coerced_Frequency < 100000000:
                Element.append(True)
            else:
                Element.append(False)

            Element_Bin = []
            for x in range(0, 8):
                if Element[x] == True:
                    Element_Bin.append(1)
                else:
                    Element_Bin.append(0)
            Element_Num = ''.join(str(e) for e in Element_Bin)
            Element5_Value = int(Element_Num, 2)

            Selected_band_index = int(math.log(Element5_Value, 2))

        if Device_Sub_Function == 0:

            if Selected_band_index == 0:
                LO1_Frequency = 2100000000
                LO2_Flag = True
            elif Selected_band_index == 1 or 2 or 3 or 4:
                LO1_Frequency = Coerced_Frequency
                LO2_Flag = False
            else:
                LO1_Frequency = 0
                LO2_Flag = False

            LO_Number = 'LO1'

            LO1_Output = I1.Tune_LO_UBX(LO1_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination, LO_Number, Selected_band_index)
            LO1_Frequency_Out = LO1_Output[0]

            if LO2_Flag == True:
                LO_Number = 'LO2'
                LO2_Frequency = LO1_Frequency_Out - Coerced_Frequency
                LO2_Output = I1.Tune_LO_UBX(LO2_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination, LO_Number, Selected_band_index)
                LO2_Frequency_Out = LO2_Output[0]
            else:
                LO2_Output = [0,0]
                LO2_Frequency_Out = LO2_Output[0]

        else:

            if Selected_band_index == 0:
                LO1_Frequency = 2380000000
                LO2_Flag = True
            elif Selected_band_index == 1:
                LO1_Frequency = 2440000000
                LO2_Flag = True
            elif Selected_band_index == 2 or 3 or 4 or 5 or 6 or 7:
                LO1_Frequency = Coerced_Frequency
                LO2_Flag = False
            else:
                LO1_Frequency = 0
                LO2_Flag = False

            LO_Number = 'LO1'

            LO1_Output = I1.Tune_LO_UBX(LO1_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination, LO_Number, Selected_band_index)
            LO1_Frequency_Out = LO1_Output[0]

            if LO2_Flag == True:
                LO_Number = 'LO2'
                LO2_Frequency = LO1_Frequency_Out - Coerced_Frequency
                LO2_Output = I1.Tune_LO_UBX(LO2_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination, LO_Number, Selected_band_index)
                LO2_Frequency_Out = LO2_Output[0]
            else:
                LO2_Output = [0,0]
                LO2_Frequency_Out = LO2_Output[0]

        LO_Frequency = LO1_Frequency_Out - LO2_Frequency_Out

        Coerced_Frequency_Out = LO_Frequency

        return (LO_Frequency, Coerced_Frequency_Out, LO1_Output, LO2_Output)

if __name__ == '__main__':

    class InputVariables:

        def __init__(self, Target_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination):

            self.Target_Frequency = Target_Frequency
            self.Data_Rate = Data_Rate
            self.Integer_N_Mode = Integer_N_Mode
            self.Device_Sub_Function = Device_Sub_Function   # 0 for TX, 1 for Default/RX
            self.Destination = Destination
                            #Radio_Perif_0/Radio_Perif_1/Global/Radio_0_I2C/Radio_1_I2C/Global_I2C/Radio_0_SPI/Radio_1_SPI/Global_SPI

    Input = InputVariables(200000000, 200000000, True, 0, 'Radio_Perif_0')

    Output = SetLO_UBX()
    O1 = Output.Set_LO_UBX(Input.Target_Frequency, Input.Data_Rate, Input.Integer_N_Mode, Input.Device_Sub_Function, Input.Destination)

    LO_Frequency = O1[0]
    Coerced_Frequency = O1[1]
    LO1_Packets = O1[2][1]
    LO2_Packets = O1[3][1]

    print(LO_Frequency, Coerced_Frequency, LO1_Packets, LO2_Packets)

    Number_Of_Packets = len(LO1_Packets)

    Index_Address = 1
    Destination = "Radio_0_Config"

    with open("Result_UBX_LO1", 'w') as f:
        for i in range(Number_Of_Packets):
            Sequence_Number = i + 1
            Address = LO1_Packets[i][1] // 4
            Data = LO1_Packets[i][2]
            Output_Packets = O2.construct_radio_register(Index_Address, Address, Data, Destination, Sequence_Number)
            Number_Of_Packets1 = len(Output_Packets)
            print(Output_Packets)
            Output_Packets_Str = str(Output_Packets)
            data_write = f.write(Output_Packets_Str)
            data_write = f.write("\n")
            for j in range(Number_Of_Packets1):
                Output_Encoded = O3.Encode_Process(Output_Packets[j])
                print(Output_Encoded)
                data_write = f.write(Output_Encoded)
                data_write = f.write("\n")
    f.close()

    if LO2_Packets == 0:
        with open("Result_UBX_LO2", 'w') as f:
            data_write = f.write("0")
            data_write = f.write("\n")
        f.close()
    else:
        Number_Of_Packets_2 = len(LO2_Packets)

        Index_Address = 1
        Destination = "Radio_0_Config"

        with open("Result_UBX_LO2", 'w') as f:
            for i in range(Number_Of_Packets_2):
                Sequence_Number = i + 1
                Address = LO2_Packets[i][1] // 4
                Data = LO2_Packets[i][2]
                Output_Packets_2 = O2.construct_radio_register(Index_Address, Address, Data, Destination, Sequence_Number)
                Number_Of_Packets3 = len(Output_Packets_2)
                print(Output_Packets_2)
                Output_Packets_Str = str(Output_Packets_2)
                data_write = f.write(Output_Packets_Str)
                data_write = f.write("\n")
                for j in range(Number_Of_Packets3):
                    Output_Encoded = O3.Encode_Process(Output_Packets_2[j])
                    print(Output_Encoded)
                    data_write = f.write(Output_Encoded)
                    data_write = f.write("\n")
        f.close()
