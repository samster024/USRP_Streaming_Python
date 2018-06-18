import math
import CreateMax2871Packets as O3

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


def Tune_LO_UBX(Target_Frequency, Data_Rate, Integer_N_Mode, Device_Sub_Function, Destination, UBX_LO_Value, Band_Index):

        Constant_Register0 = [False, 0, 0, False, False, False]  #INT_mode, INT, FRAC, C3, C2, C1
        Constant_Register1 = [0, 0, 0, 0, False, False, True]   #CPL, CPT, Phase, MOD, C3, C2, C1
        Constant_Register2 = [False, 0, 0, False, False, 0, False, 0, False, False, False, False, False, False, False, True, False]
                                             # LDS, SDN, MUX, DBR, RDIV2, R, REG4DB, CP, LDF, LDP, PDP, SHDN, TRI, RST, C3, C2, C1
        Constant_Register3 = [0, False, False, False, False, 0, 0, False, True, True]
                                                                    #VCO, VAS_SHDN, VAS_TEMP, CSM, MUTEDEL, CDM, CDIV, C3, C2, C1
        Constant_Register4 = [False, False, False, False, 0, 0, False, False, False, False, 0, False, 0, True, False, False]
                                        #SDLDO, SDDIV, SDREF, FB, DIVA, BS, SDVCO, MTLD, BDIV, RFB_EN, BPWR, RFA_EN, APWR, C3, C2, C1
        Constant_Register5 = [0, False, False, 0, False, False, 0, True, False, True]  # VASDLY, SDPLL, F01, LD, MUX, ADCS, ADCM, C3, C2, C1

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

        Target_PFD_Frequency = 50000000

        Integer_N_Mode_Max_N_Value = 65535

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

        Constant_Register0[0] = Integer_N_Mode

        if Integer_N_Mode == True:
            Constant_Register1[0] = 0
            Constant_Register2[8] = True
        else:
            Constant_Register1[0] = 1
            Constant_Register2[8] = False

        Constant_Register0[2] = Frac

        Constant_Register0[1] = INT

        if Device_Sub_Function == 0:
            if Band_Index == 0:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 2
            elif Band_Index == 1:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 2:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 0
            elif Band_Index == 3:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 4:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 5:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 0
            else:
                LO1_Power_Setting = 65535
                LO2_Power_Setting = 65535
        else:
            if Band_Index == 0:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 2
            elif Band_Index == 1:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 2
            elif Band_Index == 2:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 3:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 0
            elif Band_Index == 4:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 5:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 6:
                LO1_Power_Setting = 2
                LO2_Power_Setting = 0
            elif Band_Index == 7:
                LO1_Power_Setting = 3
                LO2_Power_Setting = 0
            else:
                LO1_Power_Setting = 65535
                LO2_Power_Setting = 65535

        if UBX_LO_Value == 'LO1':
            Constant_Register4[12] = LO1_Power_Setting
        else:
            Constant_Register4[12] = LO2_Power_Setting

        Constant_Register4[11] = True

        Constant_Register2[5] = R

        Constant_Register4[5] = Band_Select

        Constant_Register2[4] = Ref_Div_2

        Pfd_Freq_Multiplied = Pfd_Freq * 0.0004

        Pfd_Freq_Divided = int(Pfd_Freq_Multiplied + Mod - 1) // Mod

        if Pfd_Freq_Divided > 1:
            Constant_Register3[6] = Pfd_Freq_Divided
        else:
            Constant_Register3[6] = 1

        Constant_Register1[3] = Mod

        Constant_Register4[4] = int(math.log(RF_DIV, 2))

        Constant_Register2[3] = D_Terminal

        if Pfd_Freq > 32000000:
            Constant_Register2[0] = True
        else:
            Constant_Register2[0] = False

        Constant_Register3[2] = False

        Constant_Register3[5] = 0

        Constant_Register2[7] = 15

        Constant_Register2[2] = 7

        Constant_Register5[3] = 1

        Constant_Register2[1] = 0

        Constant_Register1[2] = 0

        if Feedback_Is_Divided == True:
            Constant_Register4[3] = False
        else:
            Constant_Register4[3] = True

        Constant_Register2[1] = 0

        Constant_Register2[6] = True

        Constant_Register2[9] = False

        Constant_Register2[10] = True

        Constant_Register2[11] = False

        Constant_Register2[12] = False

        Constant_Register2[13] = False

        Constant_Register3[0] = 0

        Constant_Register3[1] = False

        Constant_Register3[3] = False

        Constant_Register3[4] = False

        Constant_Register4[0] = False

        Constant_Register4[1] = False

        Constant_Register4[2] = False

        Constant_Register4[6] = False

        Constant_Register4[7] = False

        Constant_Register4[8] = True

        Constant_Register4[9] = False

        Constant_Register4[10] = 0

        Constant_Register5[0] = 0

        Constant_Register5[1] = False

        Constant_Register5[2] = True

        Constant_Register5[4] = False

        Constant_Register5[5] = False

        Constant_Register5[6] = 0

        Device_Sub_Function_TX = 0  #Research This

        Packets = O3.Create_Max_2871_Packets(Constant_Register0, Constant_Register1, Constant_Register2, Constant_Register3, Constant_Register4, Constant_Register5, Device_Sub_Function_TX, Destination)

        return(Coerced_Frequency, Packets)
