class ConstructATR:

    def construct_ATR_SBX_CBX(self, TX_Configuration, RX_Configuration, Lo_LPF_Enable, Antenna_Configuration):

        if RX_Configuration[2] == True:
            Selector_1 = 8
        else:
            Selector_1 = 32

        if RX_Configuration[1] == True:
            Selector_2 = 4
        else:
            Selector_2 = 0

        RX_Gain_Mask = (RX_Configuration[0] & 63) << 8

        if Lo_LPF_Enable == True:
            Lo_LPF_Enable_Value = 1
            Lo_LPF_Enable_Value_Shifted = Lo_LPF_Enable_Value << 15
        else:
            Lo_LPF_Enable_Value = 0
            Lo_LPF_Enable_Value_Shifted = Lo_LPF_Enable_Value << 15

        if Antenna_Configuration == 1:
            RX_Mixer_Enable_Antenna = not RX_Configuration[1]
            if RX_Mixer_Enable_Antenna == True:
                RX_Mixer_Enable_Antenna_Value = 1
                RX_Mixer_Enable_Antenna_Value_Shifted = RX_Mixer_Enable_Antenna_Value << 6
                RX_Mixer_Enable_Antenna_Value_Shifted_OR1 = RX_Mixer_Enable_Antenna_Value_Shifted | 128
            else:
                RX_Mixer_Enable_Antenna_Value = 0
                RX_Mixer_Enable_Antenna_Value_Shifted = RX_Mixer_Enable_Antenna_Value << 6
                RX_Mixer_Enable_Antenna_Value_Shifted_OR1 = RX_Mixer_Enable_Antenna_Value_Shifted | 128
            TX_Mixer_Enable_Antenna = not TX_Configuration[1]
            if TX_Mixer_Enable_Antenna == True:
                TX_Mixer_Enable_Antenna_Value = 1
                TX_Mixer_Enable_Antenna_Value_Shifted = TX_Mixer_Enable_Antenna_Value << 6
                TX_Mixer_Enable_Antenna_Value_Shifted_OR1 = TX_Mixer_Enable_Antenna_Value_Shifted | 0
            else:
                TX_Mixer_Enable_Antenna_Value = 0
                TX_Mixer_Enable_Antenna_Value_Shifted = TX_Mixer_Enable_Antenna_Value << 6
                TX_Mixer_Enable_Antenna_Value_Shifted_OR1 = TX_Mixer_Enable_Antenna_Value_Shifted | 0
        else:
            RX_Mixer_Enable_Antenna = not RX_Configuration[1]
            if RX_Mixer_Enable_Antenna == True:
                RX_Mixer_Enable_Antenna_Value = 1
                RX_Mixer_Enable_Antenna_Value_Shifted = RX_Mixer_Enable_Antenna_Value << 6
                RX_Mixer_Enable_Antenna_Value_Shifted_OR1 = RX_Mixer_Enable_Antenna_Value_Shifted | 0 | 16384
            else:
                RX_Mixer_Enable_Antenna_Value = 0
                RX_Mixer_Enable_Antenna_Value_Shifted = RX_Mixer_Enable_Antenna_Value << 6
                RX_Mixer_Enable_Antenna_Value_Shifted_OR1 = 16384 | RX_Mixer_Enable_Antenna_Value_Shifted | 0
            TX_Mixer_Enable_Antenna = not TX_Configuration[1]
            if TX_Mixer_Enable_Antenna == True:
                TX_Mixer_Enable_Antenna_Value = 1
                TX_Mixer_Enable_Antenna_Value_Shifted = TX_Mixer_Enable_Antenna_Value << 6
                TX_Mixer_Enable_Antenna_Value_Shifted_OR1 = TX_Mixer_Enable_Antenna_Value_Shifted | 0 | 16384
            else:
                TX_Mixer_Enable_Antenna_Value = 0
                TX_Mixer_Enable_Antenna_Value_Shifted = TX_Mixer_Enable_Antenna_Value << 6
                TX_Mixer_Enable_Antenna_Value_Shifted_OR1 = 16384 | TX_Mixer_Enable_Antenna_Value_Shifted | 0

        TX_Gain_Mask = (TX_Configuration[0] & 63) << 8

        if TX_Configuration[2] == True:
            Selector_3 = 8
        else:
            Selector_3 = 32

        if TX_Configuration[1] == True:
            Selector_4 = 20
        else:
            Selector_4 = 0

        Output_OR1 = Selector_1 | Selector_2 | RX_Gain_Mask | Lo_LPF_Enable_Value_Shifted | RX_Mixer_Enable_Antenna_Value_Shifted_OR1

        Output_OR2 = 0 | 0 | TX_Mixer_Enable_Antenna_Value_Shifted_OR1 | Lo_LPF_Enable_Value_Shifted | TX_Gain_Mask | Selector_3 | Selector_4
        #Check Output 2
        Output_OR2_Shifted  = Output_OR2 << 16

        Final_Output = Output_OR1 | Output_OR2_Shifted

        return(Final_Output)

    def construct_ATR_UBX(self, TX_Configuration, RX_Configuration, CPLD_Enable, SPI_Address, Antenna_Configuration):

        RX_Power_Mixer = RX_Configuration[1] & RX_Configuration[2]
        RX_Power_Mixer_Not = not RX_Power_Mixer
        if RX_Power_Mixer_Not == True:
            Selector_1 = 64
        else:
            Selector_1 = 0

        RX_Gain_Mask = (RX_Configuration[0] & 63) << 10

        if Antenna_Configuration == 1:
            Antenna_Configuration_Output = 0
        else:
            Antenna_Configuration_Output = 16

        TX_Gain_Mask = (TX_Configuration[0] & 63) << 10

        if CPLD_Enable == True:
            CPLD_Enable_Value = 8
        else:
            CPLD_Enable_Value = 0

        TX_Power_Mixer = TX_Configuration[1] & TX_Configuration[2]
        TX_Power_Mixer_Not = not TX_Power_Mixer
        if TX_Power_Mixer_Not == True:
            Selector_2 = 34
        else:
            Selector_2 = 0

        Output_OR1 = RX_Gain_Mask | 0 | 0 | 0 | 0
        # Check Output 1
        Output_OR2 = Antenna_Configuration_Output | Selector_1 | CPLD_Enable_Value | SPI_Address | TX_Gain_Mask | Selector_2 | 0

        Output_OR2_Shifted  = Output_OR2 << 16

        Final_Output = Output_OR1 | Output_OR2_Shifted

        return(Final_Output)

    def construct_ATR_WBX(self, TX_Configuration, RX_Configuration, Antenna_Configuration):

        if RX_Configuration[2] == True:
            Selector_1 = 200
        else:
            Selector_1 = 0

        if RX_Configuration[1] == True:
            Selector_2 = 20
        else:
            Selector_2 = 0

        RX_Gain_Mask = (RX_Configuration[0] & 63) << 8

        if Antenna_Configuration == 1:
            RX_Antenna_Configuration_Output = 0
            TX_Antenna_Configuration_Output = 1 << 15
        else:
            RX_Antenna_Configuration_Output = 1 << 15
            TX_Antenna_Configuration_Output = 0

        TX_Gain_And1 = TX_Configuration[0] & 2
        TX_Gain_And2 = TX_Configuration[0] & 28
        TX_Gain_And3 = TX_Configuration[0] & 32
        TX_Gain_And2_Shifted = TX_Gain_And2 << 1
        TX_Gain_And3_Shifted = TX_Gain_And3 << 9
        TX_Gain_Mask = TX_Gain_And1 | TX_Gain_And2_Shifted | TX_Gain_And3_Shifted

        if TX_Configuration[2] == True:
            Selector_3 = 192
        else:
            Selector_3 = 0

        if TX_Configuration[1] == True:
            Selector_4 = 4
        else:
            Selector_4 = 0

        Output_OR1 = Selector_1 | Selector_2 | 0 | RX_Gain_Mask | RX_Antenna_Configuration_Output
        # Check Output 1
        Output_OR2 = 0 | 0 | 0 | TX_Antenna_Configuration_Output | TX_Gain_Mask | Selector_3 | Selector_4
        #Check Output 2
        Output_OR2_Shifted  = Output_OR2 << 16

        Final_Output = Output_OR1 | Output_OR2_Shifted

        return(Final_Output)

if __name__ == '__main__':

    class InputVariables:

        def __init__(self, RX_Mixer_Enable, RX_Power_Enable, RX_Gain, TX_Mixer_Enable, TX_Power_Enable, TX_Gain, Lo_LPF_Enable, CPLD_Enable, SPI_Address, Antenna_Configuration, Daugtherboard):

            self.RX_Mixer_Enable = RX_Mixer_Enable
            self.RX_Power_Enable = RX_Power_Enable
            self.RX_Gain = RX_Gain
            self.TX_Mixer_Enable = TX_Mixer_Enable
            self.TX_Power_Enable = TX_Power_Enable
            self.TX_Gain = TX_Gain
            self.Lo_LPF_Enable = Lo_LPF_Enable
            self.CPLD_Enable = CPLD_Enable
            self.SPI_Address = SPI_Address
            self.Antenna_Configuration = Antenna_Configuration      #TX1 RX1 receives and RX2 is Unused = 1, TX1 RX1 transmits and RX2 Receives = 2
            self.Daugtherboard = Daugtherboard                      #SBX, CBX, Default = 1, UBX = 2, WBX = 3

            self.RX_Configuration = []
            self.RX_Configuration.append(RX_Gain)
            self.RX_Configuration.append(RX_Mixer_Enable)
            self.RX_Configuration.append(RX_Power_Enable)

            self.TX_Configuration = []
            self.TX_Configuration.append(TX_Gain)
            self.TX_Configuration.append(TX_Mixer_Enable)
            self.TX_Configuration.append(TX_Power_Enable)

    Input = InputVariables(False, True, 0, False, True, 0, False, False, 7, 2, 2)

    Output = ConstructATR()
    if Input.Daugtherboard == 1:
        O1 = Output.construct_ATR_SBX_CBX(Input.TX_Configuration, Input.RX_Configuration, Input.Lo_LPF_Enable, Input.Antenna_Configuration)
    elif Input.Daugtherboard == 2:
        O1 = Output.construct_ATR_UBX(Input.TX_Configuration, Input.RX_Configuration, Input.CPLD_Enable, Input.SPI_Address, Input.Antenna_Configuration)
    elif Input.Daugtherboard == 3:
        O1 = Output.construct_ATR_WBX(Input.TX_Configuration, Input.RX_Configuration, Input.Antenna_Configuration)
    print(O1)
