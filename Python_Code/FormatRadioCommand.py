def construct_radio_register( Index_Address, Address, Data, SSID, Sequence_Number):

    Intermediate_Array = []
    Output_Array = []
    Read_Flag = 0  # Make more flexible
    Notify_Flag = 0  # Make more flexible
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

    if SSID == "Radio_0_Config":  # Add additional cases
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

    return (Output_Array)
