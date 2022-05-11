import random
import time
import Gacha_List
import Trivia
import Fun_Fact

## Abbreviation:
## Len = Length
## Ques = Question
## Ans = Answer

App = True

## Stuff/List for Gacha

Gacha_Country_List = ['Germany', 'USSR', 'USA']
Gacha_Tier_List = ['Ultra Rare', 'Rare', 'Uncommon']
Gacha_Country_Len = len(Gacha_Country_List)

### Germany

Germany_Len_Uncommon = len(Gacha_List.Germany_Uncommon)
Germany_Len_Rare = len(Gacha_List.Germany_Rare)
Germany_Len_UltraRare = len(Gacha_List.Germany_UltraRare)

### USSR

Gacha_USSR_Len_Uncommon = len(Gacha_List.USSR_Uncommon)
Gacha_USSR_Len_Rare = len(Gacha_List.USSR_Rare)
Gacha_USSR_Len_UltraRare = len(Gacha_List.USSR_UltraRare)

### USA

Gacha_USA_Len_Uncommon = len(Gacha_List.USA_Uncommon)
Gacha_USA_Len_Rare = len(Gacha_List.USA_Rare)
Gacha_USA_Len_UltraRare = len(Gacha_List.USA_UltraRare)

while App:
    print('''
List of commands:
    1. Trivia
    2. Fun Fek
    3. Help
    4. Gacha Roll
    5. Shutdown''')

    Time = time.localtime()
    Time_Hour = Time.tm_hour
    Time_Min = Time.tm_min
    Time_Zone = Time.tm_zone

    if Time_Hour > 11:
        Time_Meridian = 'PM'
    else:
        Time_Meridian = 'AM'

    print(f'''{Time_Hour}:{Time_Min} {Time_Meridian}
{Time_Zone}
''')

    Initialization = input('Enter a number >>> ')

## Trivia Command

    if Initialization == '1':

        ## Variables for Trivia

        ## The index for the question and answer must be the same, otherwise it will break down :D

        Trivia_Len = len(Trivia.Trivia_Ques)
        Trivia_Correct = '\nMAN, you answered it correctly!'
        Max_Wrong = 3

        ## Coding for Trivia

        Trivia_Loop = True
        Trivia_Score = 0
        print('\nRound 1!')
        while Trivia_Loop:
            Trivia_Random = random.randrange(0,Trivia_Len)
            print(f'\n{Trivia.Trivia_Ques[Trivia_Random]}')
            Wrong_Ans = 0
            User_Ans = input('Answer >> ')
            while Wrong_Ans < Max_Wrong:
                Answer = Trivia.Trivia_Ans[Trivia_Random]

                ### Lower case the answer you give so you (and I) dont have to bother using correct capitalization

                User_Lower_Ans = str.lower(User_Ans)

                ### +4 the Wrong_Ans to get to end the second loop without causing  

                if User_Lower_Ans == Answer:
                    print(Trivia_Correct)
                    Trivia_Score = Trivia_Score + 1
                    Wrong_Ans = Wrong_Ans + 4
                else:
                    Wrong_Ans = Wrong_Ans + 1
                    Tries_Left = Max_Wrong - Wrong_Ans
                    if Wrong_Ans < Max_Wrong:
                        print(f'\nYou got it wong~! You\'ve still got {Tries_Left} tries left~')
                    else:
                        print('\nHA! You failed miserably, loser~!')
                        
            print(
f'''
Score : {Trivia_Score}
Continue?
    1. Yes
    2. No''')
            Trivia_Continue = input('Enter a number >>> ')
            if Trivia_Continue == '1':
                print(f'\nRound {Trivia_Score + 1}!')
                Wrong_Ans = Wrong_Ans + 4
            else:
                print(
f'''
Final Score : {Trivia_Score}                
That concludes the Trivia :D''')

                ## Idk why, without the 'break', it prints 'Invalid entry has been detected'
                break


## Fun fact Command

    if Initialization == '2':

        ## Variables for Fun fek

        Fun_Fact_len = len(Fun_Fact.Fun_Fact_List)

        ## Coding for Fun fek

        Fun_Loop = True
        while Fun_Loop:
            Fun_Fact_Random = random.randrange(0,Fun_Fact_len)
            print(f'\n{Fun_Fact.Fun_Fact_List[Fun_Fact_Random]}')
            print(
'''\nMore?
    1. No''')
            Choice = input('Enter a number >>> ')
            if Choice == '1':
                break
        
## Help Command

    elif Initialization == '3':
        print('''
Brief Explanation

    Trivia = A Trivia will be taken from a list, you must answer the Trivia correctly in order to pass it. However, you must answer it correctly using the correct capitalization.
    Fun fek = A Fun Fact will be taken from a list
        
Contact the developer through Discord :D, 
[Redacted]''')

## Gacha Roll

    elif Initialization == '4':

        ## Useful statistic
        Gacha_Rolled = 0
        Germany_Rolled = 0
        USA_Rolled = 0
        USSR_Rolled = 0
        Uncommon_Rolled = 0
        Rare_Rolled = 0
        UltraRare_Rolled = 0
        Uncommon = 0
        Rare = 0
        Ultra_Rare= 0

        Gacha_Roll = int(str(input('''\n
Enter the number of times you want to roll >>> ''')))
                    
        ## Gacha System to choose, even odds or unfair odds
        Gacha_System = input('''\n
List of Gacha Systems:
1. Gaijin Style
2. Fair Probability Style
Enter a number >>> ''')

## Unfair Gaijin Style Gacha (A game company that makes simulation, war, etc genre. The Gacha is inspired by the extremely unfair gacha in a game called 'War Thunder')
            
        if Gacha_System == '1':
            Gacha_Tier_List = ['Ultra Rare']
            Uncommon_Repetition = 995
            Rare_Repetition = 4

            Repetition_Count = 0
            while Repetition_Count < Uncommon_Repetition:
                Gacha_Tier_List.append('Uncommon')
                Repetition_Count = Repetition_Count + 1
            
            Repetition_Count = 0
            while Repetition_Count < Rare_Repetition:
                Gacha_Tier_List.append('Rare')
                Repetition_Count = Repetition_Count + 1
            print('\nThe odds of the Gacha has been changed :D, enjoy the Gaijin experience!')

        elif Gacha_System == '2':
            print('\nEnjoy your unadulterated odds :D')

        else:
            print('Invalid input has been detected.')

        print('\nRewards:')
        while Gacha_Rolled < Gacha_Roll:
            Gacha_Rolled = Gacha_Rolled + 1

            ## So get the index of List of countries and get the country as a string in a variable

            Gacha_Tier_Len = len(Gacha_Tier_List)
            Origin = random.randrange(0,Gacha_Country_Len)
            Country = Gacha_Country_List[Origin]
            Tier_Index = random.randrange(0,Gacha_Tier_Len)
            Tier = Gacha_Tier_List[Tier_Index]

            ## Use the assigned variable and then randomly pick an index of that country in order print the vehicle that you the person rolled
            if Country == 'Germany':
                if Tier == 'Uncommon':
                    Country_Tier = Gacha_List.Germany_Uncommon
                    Vehicle = random.randrange(0,Germany_Len_Uncommon)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (Germany) ({Tier})')
                    Uncommon_Rolled = Uncommon_Rolled + 1

                elif Tier == 'Rare':
                    Country_Tier = Gacha_List.Germany_Rare
                    Vehicle = random.randrange(0,Germany_Len_Rare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (Germany) ({Tier})')
                    Rare_Rolled = Rare_Rolled + 1

                elif Tier == 'Ultra Rare':
                    Country_Tier = Gacha_List.Germany_UltraRare
                    Vehicle = random.randrange(0,Germany_Len_UltraRare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (Germany) ({Tier})')
                    UltraRare_Rolled = UltraRare_Rolled + 1
                
                Germany_Rolled = Germany_Rolled + 1


            elif Country == 'USSR':
                if Tier == 'Uncommon':
                    Country_Tier = Gacha_List.USSR_Uncommon
                    Vehicle = random.randrange(0,Gacha_USSR_Len_Uncommon)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USSR) ({Tier})')
                    Uncommon_Rolled = Uncommon_Rolled + 1

                elif Tier == 'Rare':
                    Country_Tier = Gacha_List.USSR_Rare
                    Vehicle = random.randrange(0,Gacha_USSR_Len_Rare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USSR) ({Tier})')
                    Rare_Rolled = Rare_Rolled + 1

                elif Tier == 'Ultra Rare':
                    Country_Tier = Gacha_List.USSR_UltraRare
                    Vehicle = random.randrange(0,Gacha_USSR_Len_UltraRare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USSR) ({Tier})')
                    UltraRare_Rolled = UltraRare_Rolled + 1

                USSR_Rolled = USSR_Rolled + 1

            elif Country == 'USA':
                if Tier == 'Uncommon':
                    Country_Tier = Gacha_List.USA_Uncommon
                    Vehicle = random.randrange(0,Gacha_USA_Len_Uncommon)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USA) ({Tier})')
                    Uncommon_Rolled = Uncommon_Rolled + 1

                elif Tier == 'Rare':
                    Country_Tier = Gacha_List.USA_Rare
                    Vehicle = random.randrange(0,Gacha_USA_Len_Rare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USA) ({Tier})')
                    Rare_Rolled = Rare_Rolled + 1

                elif Tier == 'Ultra Rare':
                    Country_Tier = Gacha_List.USA_UltraRare
                    Vehicle = random.randrange(0,Gacha_USA_Len_UltraRare)
                    print(f'{Gacha_Rolled}. {Country_Tier[Vehicle]} (USA) ({Tier})')
                    UltraRare_Rolled = UltraRare_Rolled + 1
                
                USA_Rolled = USA_Rolled + 1

        print(f'''\n
Gacha Statistic:
Total Roll = {Gacha_Rolled}
Germany Roll = {Germany_Rolled}
USSR Roll = {USSR_Rolled}
USA Roll = {USA_Rolled}

Uncommon Rolled = {Uncommon_Rolled}
Rare Rolled = {Rare_Rolled}
Ultra Rare Rolled = {UltraRare_Rolled}

Probability:
Uncommon = 995/1000
Rare = 4/1000
Ultra Rare = 1/1000
        ''')

## Exit Command

    elif Initialization == '5':
        exit()

## Response For Invalid Entry

    else:
        print('\nInvalid entry has been detected.')






    
    

