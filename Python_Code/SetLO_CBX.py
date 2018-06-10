import math
import CreateMax2870Packets as O3
import FormatRadioCommand as O4
import EncodingStream as O5

class CalculateCoerceFrequency:

    def Calculate_Coerce_Frequency(self, Frac, INT, Ref_Div_2, RF_DIV, D_Terminal, R, Data_Rate, Mod, Feedback_Divisor):

        R1 = Frac // Mod

        R2 = R1 + INT

        R3 = R2 * Data_Rate

        if D_Terminal == True:
            Check = 1
        else:
            Check = 0

        Check_Incremented = Check + 1

        R4 = R3 * Check_Incremented

        if Ref_Div_2 == True:
            Check1 = 1
        else:
            Check1 = 0

        Check1_Incremented = Check1 + 1

        R5 = R * Check1_Incremented

        R6 = R4 // R5

        R7 = Feedback_Divisor * R6

        R8 = R7 // RF_DIV

        return(R8)

class CalculateDividers:

    def Calculate_Dividers(self, Integer_N_Mode, Mod, Target_Frequency, D_Terminal, Ref_Freq, Target_PFD_Frequency, Ref_Div, Feedback_Is_Divided, RF_DIV, Integer_N_Mode_Max_N_Value):

        if Feedback_Is_Divided == True:
            if RF_DIV > 16:
                Selecter_1 = True
            else:
                Selecter_1 = False

            if Selecter_1 == True:
                Feedback_Divisor = 16
            else:
                Feedback_Divisor = RF_DIV
        else:
            Feedback_Divisor = 1

        Flag = False

        Iteration = 0

        while Flag == False:

            Iteration = Iteration + 1

            if Ref_Div == True:
                C1 = 1
            else:
                C1 = 0

            C2 = C1 + 1

            Multiplier_1 = C2 * Iteration

            R_Counter_Max_Value = 1023

            if Iteration > R_Counter_Max_Value:
                While_OR_2 = True
            else:
                While_OR_2 = False

            if D_Terminal == True:
                C3 = 1
            else:
                C3 = 0

            C4 = C3 + 1

            Freq1 = Ref_Freq * C4

            Freq2 = Freq1 // Multiplier_1

            if Freq2 > Target_PFD_Frequency:
                Overall_Values = True
            else:
                Overall_Values = False

            if Overall_Values == True:

                Frac = 0
                Band_Select = 0
                INT = 0
                Pfd_Freq = Freq2

                Quo = Iteration // 2
                Rem = Iteration % 2

                if Rem == 0:
                    R = Quo
                    Ref_Div_2 = True
                else:
                    R = Iteration
                    Ref_Div_2 = Ref_Div

                While_OR_1 = False

                Loop_Function = While_OR_1 | While_OR_2

                if Loop_Function == True:
                    Flag = True

            else:

                Freq3 = Target_Frequency // Freq2

                Freq4 = Freq3 // Feedback_Divisor

                if Freq4 > 0:
                    Round_Freq4 = int(Freq4)
                else:
                    Round_Freq4 = round(Freq4)

                Sub1 = Freq4 - Round_Freq4

                Multiplier_2 = Mod * Sub1

                Round_Multiplier = round(Multiplier_2)

                if Integer_N_Mode == True:

                    Frac = 0

                    Mod_Divided = Mod // 2

                    if Round_Multiplier > Mod_Divided:
                        Feed = Round_Freq4 + 1
                    else:
                        Feed = Round_Freq4

                    INT = Feed

                    if Integer_N_Mode_Max_N_Value > Feed:
                        Flag_2 = True
                    else:
                        Flag_2 = False

                    if 16 < Feed:
                        Flag_3 = True
                    else:
                        Flag_3 = False

                    And1 = Flag_2 & Flag_3

                    if And1 == True:
                        Divider_1 = (Freq2 + 50000 - 1) // 50000
                        Band_Select = Divider_1
                        if Divider_1 <= 1023:
                            While_OR_1 = True
                        else:
                            While_OR_1 = False
                    else:
                        Band_Select = 0
                        While_OR_1 = False

                else:

                    Frac = Round_Multiplier

                    INT = Round_Freq4

                    if 4091 > Round_Freq4:
                        Flag_2 = True
                    else:
                        Flag_2 = False

                    if 19 < Round_Freq4:
                        Flag_3 = True
                    else:
                        Flag_3 = False

                    And1 = Flag_2 & Flag_3

                    if And1 == True:
                        Divider_1 = (Freq2 + 50000 - 1) // 50000
                        Band_Select = Divider_1
                        if Divider_1 <= 1023:
                            While_OR_1 = True
                        else:
                            While_OR_1 = False
                    else:
                        Band_Select = 0
                        While_OR_1 = False

                Pfd_Freq = Freq2

                Quo = Iteration // 2
                Rem = Iteration % 2

                if Rem == 0:
                    R = Quo
                    Ref_Div_2 = True
                else:
                    R = Iteration
                    Ref_Div_2 = Ref_Div

                Loop_Function = While_OR_1 | While_OR_2

                if Loop_Function == True:
                    Flag = True

        return (Frac, Band_Select, INT, Pfd_Freq, R, Ref_Div_2, Feedback_Divisor)


class SetLO_CBX:

    def Set_LO_CBX(self, Target_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination):

        Constant_Register0 = [False, 125, 0, False, False, False]  #INT_mode, INT, FRAC, C3, C2, C1
        Constant_Register1 = [False, 1, 0, 1, 4095, False, False, True]   #CPOC, CPL, CPT, Phase, MOD, C3, C2, C1
        Constant_Register2 = [False, 3, 1, False, False, 1, False, 7, False, False, True, False, False, False, False, True, False]
                                    # LDS, SDN, MUX, DBR, RDIV2, R, REG4DB, CP, LDF, LDP, PDP, SHDN, TRI, RST, C3, C2, C1
        Constant_Register3 = [0, False, True, 0, 1, False, True, True]  #VCO, VAS_SHDN, RETUNE, CDM, CDIV, C3, C2, C1
        Constant_Register4 = [True, 0, 0, True, False, 0, True, 3, True, False, False]
                                                                #FB, DIVA, BS, BDIV, RFB_EN, BPWR, RFA_EN, APWR, C3, C2, C1
        Constant_Register5 = [True, 1, False, True, False, True]  # F01, LD, MUX, C3, C2, C1

        Ref_Div = False

        Mod = 4095

        Ref_Freq = Data_Rate

        RF_DIV = 1
        while Target_Frequency < 3000000000:
            Target_Frequency = Target_Frequency * 2
            RF_DIV = RF_DIV * 2

        if Data_Rate <= 10000000:
            D_Terminal = True
        else:
            D_Terminal = False

        Target_PFD_Frequency = 25000000

        Integer_N_Mode_Max_N_Value = 4095

        Feedback_Is_Divided = True

        Output = CalculateDividers()
        O1 = Output.Calculate_Dividers(Integer_N_Mode, Mod, Target_Frequency, D_Terminal, Ref_Freq, Target_PFD_Frequency, Ref_Div, Feedback_Is_Divided, RF_DIV, Integer_N_Mode_Max_N_Value)
        Frac = O1[0]
        Band_Select = O1[1]
        INT = O1[2]
        Pfd_Freq = O1[3]
        R = O1[4]
        Ref_Div_2 = O1[5]
        Feedback_Divisor = O1[6]

        Output1 = CalculateCoerceFrequency()
        O2 = Output1.Calculate_Coerce_Frequency(Frac, INT, Ref_Div_2, RF_DIV, D_Terminal, R, Data_Rate, Mod, Feedback_Divisor)

        Coerced_Frequency = O2
        LO_Frequency = Coerced_Frequency

        Constant_Register0[0] = Integer_N_Mode

        if Integer_N_Mode == True:
            Constant_Register1[0] = True
            Constant_Register1[1] = 0
            Constant_Register2[8] = True
        else:
            Constant_Register1[0] = False
            Constant_Register1[1] = 1
            Constant_Register2[8] = False

        Constant_Register0[2] = Frac

        Constant_Register0[1] = INT

        if Device_Sub_Function == 0:
            if 350000000 < Coerced_Frequency < 370000000:
                Select_Line = True
            else:
                Select_Line = False

            if Select_Line == True:
                Constant_Register4[7] = 2
            else:
                Constant_Register4[7] = 3
        else:
            Constant_Register4[7] = 3

        Constant_Register2[5] = R

        Constant_Register4[2] = Band_Select

        Constant_Register2[4] = Ref_Div_2

        Pfd_Freq_Multiplied = Pfd_Freq * 0.0004

        Pfd_Freq_Divided = int(Pfd_Freq_Multiplied + Mod - 1) // Mod

        if Pfd_Freq_Divided > 1:
            Constant_Register3[4] = Pfd_Freq_Divided
        else:
            Constant_Register3[4] = 1

        Constant_Register1[4] = Mod

        Constant_Register4[1] = int(math.log(RF_DIV, 2))

        Constant_Register2[3] = D_Terminal

        if Ref_Freq >= 3000000000:
            Flag = False
        else:
            Flag = True

        Constant_Register4[0] = Flag

        Packets = O3.Create_Max_2870_Packets(Constant_Register0, Constant_Register1, Constant_Register2, Constant_Register3, Constant_Register4, Constant_Register5, Device_Sub_Function, Destination)

        return(LO_Frequency, Coerced_Frequency, Packets)

if __name__ == '__main__':

    class InputVariables:

        def __init__(self, Target_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination):

            self.Target_Frequency = Target_Frequency
            self.Data_Rate = Data_Rate
            self.Integer_N_Mode = Integer_N_Mode
            self.Device_Sub_Function = Device_Sub_Function   # 0 for TX, 1 for Default/RX
            self.Destination = Destination
                            #Radio_Perif_0/Radio_Perif_1/Global/Radio_0_I2C/Radio_1_I2C/Global_I2C/Radio_0_SPI/Radio_1_SPI/Global_SPI

    Input = InputVariables(2000000000, 200000000, True, 0, 'Radio_Perif_0')

    Output = SetLO_CBX()
    O1 = Output.Set_LO_CBX(Input.Target_Frequency, Input.Data_Rate, Input.Integer_N_Mode, Input.Device_Sub_Function, Input.Destination)
    print(O1)

    Number_Of_Packets = len(O1[2])

    Index_Address = 1
    Destination = "Radio_0_Config"

    with open("Result_CBX_1", 'w') as f:
        for i in range(Number_Of_Packets):
            Sequence_Number = i + 1
            Address = O1[2][i][1] // 4
            Data = O1[2][i][2]
            Output_Packets = O4.construct_radio_register(Index_Address, Address, Data, Destination, Sequence_Number)
            Number_Of_Packets1 = len(Output_Packets)
            print(Output_Packets)
            Output_Packets_Str = str(Output_Packets)
            data_write = f.write(Output_Packets_Str)
            data_write = f.write("\n")
            for j in range(Number_Of_Packets1):
                Output_Encoded = O5.Encode_Process(Output_Packets[j])
                print (Output_Encoded)
                data_write = f.write(Output_Encoded)
                data_write = f.write("\n")
    f.close()
