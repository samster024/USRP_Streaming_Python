class ConstructRadioRegister:

    def construct_radio_register(self, Index_Address, Address, Data, SSID, Sequence_Number):

        Intermediate_Array = []
        Output_Array = []
        Read_Flag = 0     #Make more flexible
        Notify_Flag = 0   #Make more flexible
        Dummy_Address = 0
        Output_Stream1 = []
        Output_Stream2 = []
        Output_Stream3 = []
        Output_Stream4 = []
        Output_Stream5 = []

        SID = 1

        Index_Address_Increment = Index_Address + 1
        Index_Address_Multipled = Index_Address_Increment * 2
        Index_Address_Shifted = Index_Address_Multipled << 32

        Sequence_Number_Shifted = Sequence_Number << 48

        Flags = 8
        Flags_Shifted = Flags << 60

        Output1 = SID | Index_Address_Shifted | Sequence_Number_Shifted | Flags_Shifted

        Intermediate_Array.append(Output1)

        Address_Shifted = Address << 32

        Output2 = Address_Shifted | Data

        Intermediate_Array.append(Output2)

        Element_0 = Intermediate_Array[0]

        High_Part_Constant = ((Element_0 & 0xffffffff00000000) >> 32)
        Low_Part_Sequence_Number = Element_0 & 0xffffffff

        Element_1 = Intermediate_Array[1]

        High_Part_Address = ((Element_1 & 0xffffffff00000000) >> 32)
        Low_Part_Data = Element_1 & 0xffffffff

        if SSID == "Radio_0_Config":  #Add additional cases
            SSID_Nr = 3
        elif SSID == "Radio_1_Config":
            SSID_Nr = 4
        else:
            SSID_Nr = 0

        Output_Stream1.append(Read_Flag)
        Output_Stream1.append(Notify_Flag)
        Output_Stream1.append(Dummy_Address)
        Output_Stream1.append(Index_Address_Increment)
        Output_Stream1.append(SSID_Nr)
        Output_Array.append(Output_Stream1)

        Output_Stream2.append(Read_Flag)
        Output_Stream2.append(Notify_Flag)
        Output_Stream2.append(Dummy_Address)
        Output_Stream2.append(Low_Part_Sequence_Number)
        Output_Stream2.append(SSID_Nr)
        Output_Array.append(Output_Stream2)

        Output_Stream3.append(Read_Flag)
        Output_Stream3.append(Notify_Flag)
        Output_Stream3.append(Dummy_Address)
        Output_Stream3.append(High_Part_Constant)
        Output_Stream3.append(SSID_Nr)
        Output_Array.append(Output_Stream3)

        Output_Stream4.append(Read_Flag)
        Output_Stream4.append(Notify_Flag)
        Output_Stream4.append(Dummy_Address)
        Output_Stream4.append(Low_Part_Data)
        Output_Stream4.append(SSID_Nr)
        Output_Array.append(Output_Stream4)

        Output_Stream5.append(Read_Flag)
        Output_Stream5.append(Notify_Flag)
        Output_Stream5.append(Dummy_Address)
        Output_Stream5.append(High_Part_Address)
        Output_Stream5.append(SSID_Nr)
        Output_Array.append(Output_Stream5)

        return(Output_Array)

class EncodeBitStream:

    def Encode_Process(self, O1):

        SSID = O1[4]

        Data = O1[3]
        Data_Shifted = Data << 8

        Address = O1[2]
        Address_Shifted = Address << 40

        Notify = O1[1]
        Notify_Shifted = Notify << 56

        Read = O1[0]
        Read_Shifted = Read << 57

        Output_Stream = SSID | Data_Shifted | Address_Shifted | Notify_Shifted | Read_Shifted

        Output_Stream_Binary = bin(Output_Stream)[2: ]

        Output_Stream_Binary_Format = Output_Stream_Binary.zfill(64)

        return(Output_Stream_Binary_Format)

if __name__ == '__main__':

    class InputClass:

        def __init__(self, Index_Address, Address, Data, SSID, Sequence_Number):
            self.Index_Address = Index_Address
            self.Address = Address
            self.Data = Data
            self.SSID = SSID
            self.Sequence_Number = Sequence_Number

    Input = InputClass(1, 8, 3, "Radio_0_Config", 1)

    Output = ConstructRadioRegister()
    O1 = Output.construct_radio_register(Input.Index_Address, Input.Address, Input.Data, Input.SSID, Input.Sequence_Number)
    Number_Of_Packets = len(O1)

    for i in range(Number_Of_Packets):
        Encode_Output = EncodeBitStream()
        EO1 = Encode_Output.Encode_Process(O1[i])
        print(EO1)