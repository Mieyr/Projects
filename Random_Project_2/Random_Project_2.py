import random
import time
import sys

### This is based on a movie scene, 'Matrix', where there's a random letter being generated that is forming the word 'Matrix'


Alphabet_List = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
Bruh = True
while Bruh:
    print('''
Choose
    1. Randomize
''')
    Initialization = input('>>> ')

    if Initialization == '1':
        Input = str.upper(input('''
Give a Word
>>> '''))

        def Char(Input):
            return [char for char in Input]
            
        # Driver code
        Word = Char(Input)
        print(Word)
        Output = []
        Fake_Output = []
        Occupied_Index_Output = []
        Correct = 0

        while len(Output) < len(Word):
            Output.append('')
            Fake_Output.append('')

        while Correct < len(Word):
            Random_Output_Spot = random.randrange(0, len(Word))
            if Output[Random_Output_Spot] == '':
                while Output[Random_Output_Spot] != Word[Random_Output_Spot]:
                    Random_Chara_Index = random.randrange(0,len(Alphabet_List))
                    Random_Chara = Alphabet_List[Random_Chara_Index]
                    Fake_Output[Random_Output_Spot] = Random_Chara
                    if Random_Chara == Word[Random_Output_Spot]:
                        Output[Random_Output_Spot] = Random_Chara
                        Correct += 1
                    print(Fake_Output)

                    time.sleep(0.5)
                    def delete_last_line():
                        "Use this function to delete the last line in the STDOUT"

                        #cursor up one line
                        sys.stdout.write('\x1b[1A')

                        #delete last line
                        sys.stdout.write('\x1b[2K')
                    delete_last_line()
        print(Output)
        time.sleep(5)