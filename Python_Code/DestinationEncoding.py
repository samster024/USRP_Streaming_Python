def Destinattion(Destination):

    if Destination == 'Radio_Perif_0':
        Destination_Encoded = 0
    elif Destination == 'Radio_Perif_1':
        Destination_Encoded = 1
    elif Destination == 'Global':
        Destination_Encoded = 2
    elif Destination == 'Radio_0_I2C':
        Destination_Encoded = 3
    elif Destination == 'Radio_1_I2C':
        Destination_Encoded = 4
    elif Destination == 'Global_I2C':
        Destination_Encoded = 5
    elif Destination == 'Radio_0_SPI':
        Destination_Encoded = 6
    elif Destination == 'Radio_0_SPI':
        Destination_Encoded = 7
    elif Destination == 'Global_SPI':
        Destination_Encoded = 8
    else:
        Destination_Encoded = 'Input_Error'

    return (Destination_Encoded)
