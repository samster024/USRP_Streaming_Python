import FormatRadioCommand as O1
import EncodingStream as O2

if __name__ == '__main__':

    class InputClass:

        def __init__(self, Index_Address, Address, Data, SSID, Sequence_Number):
            self.Index_Address = Index_Address
            self.Address = Address
            self.Data = Data
            self.SSID = SSID
            self.Sequence_Number = Sequence_Number

    Input = InputClass(1, 8, 3, "Radio_0_Config", 1)

    Output = O1.construct_radio_register(Input.Index_Address, Input.Address, Input.Data, Input.SSID, Input.Sequence_Number)
    Number_Of_Packets = len(Output)

    for i in range(Number_Of_Packets):
        Output1 = O2.Encode_Process(Output[i])
        print (Output1)

'''
Input

1, 8, 3, "Radio_0_Config", 1
'''


'''
Output

0000000000000000000000000000000000000000000000000000001000000011
0000000000000000000000000000000000000000000000000000000100000011
0000000000000000000000001000000000000001000000000000010000000011
0000000000000000000000000000000000000000000000000000001100000011
0000000000000000000000000000000000000000000000000000100000000011
'''