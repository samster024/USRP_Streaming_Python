def Encode_Process(O1):

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
