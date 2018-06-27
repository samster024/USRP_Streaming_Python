import DestinationEncoding as D1
import FormatRadioCommand as O4
import EncodingStream as O5


class ConstructADC:

    def construct_ADC(self, TX_Configuration, RX_Configuration, Lo_LPF_Enable, CPLD_Enable, SPI_Address, Antenna_Configuration, Coerced_Gain, ADC_Gain, Destination):

        Gain_Addition = ADC_Gain + RX_Configuration[0]

        if Gain_Addition > 63:
            OR_Element_1 = True
        else:
            OR_Element_1 = False

        Coerced_Gain_Summed = Coerced_Gain + Coerced_Gain

        if Coerced_Gain_Summed > 255:
            Coerced_Gain_Summed_Changed = 255
        elif Coerced_Gain_Summed < 0:
            Coerced_Gain_Summed_Changed = 0
        else:
            Coerced_Gain_Summed_Changed = Coerced_Gain_Summed

        if Coerced_Gain_Summed_Changed == Gain_Addition:
            OR_Element_2 = False
        else:
            OR_Element_2 = True

        if Coerced_Gain > 31.5:
            OR_Element_3 = True
        else:
            OR_Element_3 = False

        OR_Flag_1 = OR_Element_1 | OR_Element_3

        AND_Flag_1 = OR_Flag_1 & OR_Element_2

        Destination_Value = D1.Destinattion(Destination)

        Coerced_Gain_Dif_2 = Coerced_Gain_Summed - 63

        if Coerced_Gain_Dif_2 > 255:
            Coerced_Gain_Comp1 = 255
        elif Coerced_Gain_Dif_2 < 0:
            Coerced_Gain_Comp1 = 0
        else:
            Coerced_Gain_Comp1 = Coerced_Gain_Dif_2

        if AND_Flag_1 == True:
            if OR_Flag_1 == True:

                Coerced_Gain_Dif = Coerced_Gain_Summed - 63
                Coerced_Gain_Dif_Shifted = Coerced_Gain_Dif << 20

                Packet1 = []
                Packet1.append(Destination_Value)
                Packet1.append(36)
                Packet1.append(2415919168)

                Packet2 = []
                Packet2.append(Destination_Value)
                Packet2.append(40)

                Packet2_Data = 1426063360 + Coerced_Gain_Dif_Shifted
                Packet2.append(Packet2_Data)

                Packet3 = []
                Packet3.append(Destination_Value)
                Packet3.append(40)

                Packet3_Data = 1744830464 + Coerced_Gain_Dif_Shifted
                Packet3.append(Packet3_Data)

                Packets = []
                Packets.append(Packet1)
                Packets.append(Packet2)
                Packets.append(Packet3)
                return (Packets, Coerced_Gain_Comp1)


            else:

                Packet1 = []
                Packet1.append(Destination_Value)
                Packet1.append(36)
                Packet1.append(2415919168)

                Packet2 = []
                Packet2.append(Destination_Value)
                Packet2.append(40)
                Packet2.append(1426063360)

                Packet3 = []
                Packet3.append(Destination_Value)
                Packet3.append(40)
                Packet3.append(1744830464)

                Packets = []
                Packets.append(Packet1)
                Packets.append(Packet2)
                Packets.append(Packet3)
                return (Packets, Coerced_Gain_Comp1)

        else:

            Packets = 0
            return(Packets, Coerced_Gain_Comp1)



if __name__ == '__main__':

    class InputVariables:

        def __init__(self, RX_Mixer_Enable, RX_Power_Enable, RX_Gain, TX_Mixer_Enable, TX_Power_Enable, TX_Gain, Lo_LPF_Enable, CPLD_Enable, SPI_Address, Antenna_Configuration, Coerced_Gain, ADC_Gain, Destination):

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
            self.Coerced_Gain = Coerced_Gain
            self.ADC_Gain = ADC_Gain
            self.Destination = Destination

            self.RX_Configuration = []
            self.RX_Configuration.append(RX_Gain)
            self.RX_Configuration.append(RX_Mixer_Enable)
            self.RX_Configuration.append(RX_Power_Enable)

            self.TX_Configuration = []
            self.TX_Configuration.append(TX_Gain)
            self.TX_Configuration.append(TX_Mixer_Enable)
            self.TX_Configuration.append(TX_Power_Enable)

    Input = InputVariables(False, True, 0, False, True, 0, False, True, 4, 1, 33, 64, "Radio_Perif_0")

    Output = ConstructADC()
    O1 = Output.construct_ADC(Input.TX_Configuration, Input.RX_Configuration,Input.Lo_LPF_Enable, Input.CPLD_Enable, Input.SPI_Address, Input.Antenna_Configuration, Input.Coerced_Gain, Input.ADC_Gain, Input.Destination)
    print(O1)

    Number_Of_Packets = len(O1[0])

    Index_Address = 1

    Destination = "Radio_0_Config"

    with open("Result_ADC_1", 'w') as f:
        for i in range(Number_Of_Packets):
            Sequence_Number = i + 1
            Address = O1[0][i][1] // 4
            Data = O1[0][i][2]
            Output_Packets = O4.construct_radio_register(Index_Address, Address, Data, Destination, Sequence_Number)
            Number_Of_Packets1 = len(Output_Packets)
            print(Output_Packets)
            Output_Packets_Str = str(Output_Packets)
            # data_write = f.write(Output_Packets_Str)
            # data_write = f.write("\n")
            for j in range(Number_Of_Packets1):
                Output_Encoded = O5.Encode_Process(Output_Packets[j])
                print(Output_Encoded)
                # data_write = f.write(Output_Encoded)
                # data_write = f.write("\n")
                Output_Decimal = int(Output_Encoded, 2)
                data_write = f.write(str(Output_Decimal))
                data_write = f.write("\n")
    f.close()
