from colorama import init, Fore as F, Style as S, Back as B
from pathlib import Path
import random
import shutil
import json
import os

init()

CMODS: dict[str: list[str] | str: list] = {
    "BOOM": ["-t"],
    "LEAF": ["-t"],
    "D"   : ["-t"],
}

PUNCIE = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you can imagine is real. – Pablo Picasso",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "The road to success and the road to failure are almost exactly the same. – Colin R. Davis",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The best way to predict the future is to create it. – Abraham Lincoln",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "The only way to achieve the impossible is to believe it is possible. – Charles Kingsleigh",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "It is never too late to be what you might have been. – George Eliot",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "Everything you've ever wanted is on the other side of fear. – George Addair",
    "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "Dream big and dare to fail. – Norman Vaughan",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "The best revenge is massive success. – Frank Sinatra",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "The harder you work for something, the greater you’ll feel when you achieve it. – Unknown",
    "Push yourself, because no one else is going to do it for you. – Unknown",
    "Great things never come from comfort zones. – Unknown",
    "Success doesn’t just find you. You have to go out and get it. – Unknown",
    "Dream it. Wish it. Do it. – Unknown",
    "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "The harder you work for something, the greater you’ll feel when you achieve it. – Unknown",
    "Don’t stop when you’re tired. Stop when you’re done. – Unknown",
    "Wake up with determination. Go to bed with satisfaction. – Unknown",
    "Do something today that your future self will thank you for. – Unknown",
    "Little things make big days. – Unknown",
    "It’s going to be hard, but hard does not mean impossible. – Unknown",
    "Don’t wait for opportunity. Create it. – Unknown",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths. – Unknown",
    "The key to success is to focus on goals, not obstacles. – Unknown",
    "Dream it. Wish it. Do it. – Unknown",
    "Learn as if you will live forever, live like you will die tomorrow. – Mahatma Gandhi",
    "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "In order to succeed, we must first believe that we can. – Nikos Kazantzakis",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "You are braver than you believe, stronger than you seem, and smarter than you think. – A.A. Milne",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Opportunities don't happen, you create them. – Chris Grosser",
    "Your life does not get better by chance, it gets better by change. – Jim Rohn",
    "To be successful, you must act big, think big and talk big. – Aristotle Onassis",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "I am not a product of my circumstances. I am a product of my decisions. – Stephen Covey",
    "If you don’t build your dream, someone else will hire you to help them build theirs. – Dhirubhai Ambani",
    "The secret of getting ahead is getting started. – Mark Twain",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "The best way to predict the future is to create it. – Abraham Lincoln",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "The only thing standing between you and your goal is the story you keep telling yourself. – Jordan Belfort",
    "Do not wait to strike till the iron is hot, but make it hot by striking. – William Butler Yeats",
    "Act as if what you do makes a difference. It does. – William James",
    "You must be the change you wish to see in the world. – Mahatma Gandhi",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "The best revenge is massive success. – Frank Sinatra",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. – Roy T. Bennett",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "I have not failed. I’ve just found 10,000 ways that won’t work. – Thomas Edison",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "It is never too late to be what you might have been. – George Eliot",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. – Brian Tracy",
    "Life is what happens when you’re busy making other plans. – John Lennon",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "When one door of happiness closes, another opens; but we often look so long at the closed door that we do not see the one which has been opened for us. – Helen Keller",
    "We may encounter many defeats but we must not be defeated. – Maya Angelou",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "The harder you work for something, the greater you’ll feel when you achieve it. – Unknown",
    "Dream big and dare to fail. – Norman Vaughan",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt"
]

def takeInput() -> str:
    UI: str = input(f'{F.BLUE + S.BRIGHT}[?]: {S.RESET_ALL}')
    return UI

def lexingProcess(userInput: str) -> list[str] | list:
    return userInput.strip().lower().split()

def JSON_VERSION() -> str | FileNotFoundError:
    with open("../Documents/Config/version.json", "r") as file:
        versionInfo = json.load(file)
        print(f'{S.BRIGHT}{versionInfo["version"]} - {versionInfo["status"].capitalize()}{S.RESET_ALL}')

def YPHUS() -> str:
    print(f'''{S.BRIGHT}*: Required
&: Optional

C1: "scd" - Show Current Directory
T1: This command shows which directory is working on now.
S1: scd rt <{F.LIGHTBLUE_EX}str{S.RESET_ALL + S.BRIGHT}>
E1: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}scd {F.LIGHTGREEN_EX}[Output]{S.RESET_ALL + S.BRIGHT}C:/

C2: "chcd" - Change Current Directory
T2: This command changes current directory.
S2: chcd {F.GREEN}[path*]{S.RESET_ALL + S.BRIGHT} rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E2: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}chcd C:/Beautiful_Directory/ {F.LIGHTGREEN_EX}[Output]{S.RESET_ALL + S.BRIGHT} ...

C3: "ldf" - List Directories and Files
T3: This command lists all folders and files in the current directory.
S3: ldf rt <{F.LIGHTBLUE_EX}str{S.RESET_ALL + S.BRIGHT}>
E3: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}ldf {F.LIGHTGREEN_EX}[Output]{S.RESET_ALL + S.BRIGHT} ...

C4: "boom" - Boom 
T4: This command creates a folder in the target directory or current directory.
S4: boom {F.GREEN}[mod&:-t]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[path&*]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[fname*]{S.RESET_ALL + S.BRIGHT} rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E4.1: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}boom a_perfect_folder_name {F.LIGHTGREEN_EX}[Output]{S.RESET_ALL + S.BRIGHT} ...
E4.2: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}boom -t C:/Beautiful_Directory/ another_perfect_folder_name {F.LIGHTGREEN_EX}[Output]{S.RESET_ALL + S.BRIGHT} ...

C5: "leaf" - Leaf
T5: This command creates a file in the target directory or current directory.
S5: leaf {F.GREEN}[mod&:-t]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[path&*]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[fname*]{S.RESET_ALL + S.BRIGHT} rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E5.1: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}leaf a_perfect_file_name.blahblah {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...
E5.2: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}leaf -t C:/Beautiful_Directory/ another_perfect_file_name.blahblah {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...

C6: "d" - Destroy
T6: This command deletes a file or folder in the target directory or current directory.
S6: d {F.GREEN}[mod&:-t]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[path&*]{S.RESET_ALL + S.BRIGHT} {F.GREEN}[fname*]{S.RESET_ALL + S.BRIGHT} rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E6.1: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}d a_perfect_file_name.blahblah {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...
E6.2: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}d -t C:/Beautiful_Directory/ another_perfect_file_name.blahblah {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...

C7: "cl" | "cls" - Clear
T7: This command clears the terminal screen.
S7: cl | cls rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E7: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}cl {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...

C8: "yphus" - Yphus
T8: This command shows all commands how can use with every detail.
S8: yphus rt <{F.LIGHTBLUE_EX}str{S.RESET_ALL + S.BRIGHT}>
E8: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}yphus {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT} ...

C9: "q" | "quit" | "exit" - Quit, Exit
T9: This command exits from the app.
S9: q | quit | exit rt <{F.LIGHTBLUE_EX}sysfunc{S.RESET_ALL + S.BRIGHT}>
E9: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}q | {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}quit | {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}exit {F.GREEN}[Output]{S.RESET_ALL + S.BRIGHT} ...

C10: "punch" - Punch
T10: This command prints whatever you write.
S10: punch {F.GREEN}[mod&:-t]{S.RESET_ALL + S.BRIGHT} rt <{F.LIGHTBLUE_EX}str{S.RESET_ALL + S.BRIGHT}>
E10.1: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}punch {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT} ...
E10.2: {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}punch Hello World! {F.GREEN}[Input]{S.RESET_ALL + S.BRIGHT}Hello World!{S.RESET_ALL}\n''')

def PUNCH(UI: str) -> str:
    if len(UI.strip().lower().split()) == 1:
        PunchieRandom = random.randint(0, 99)
        print(PUNCIE[PunchieRandom])
        print()
    
    else:
        UI: str = UI.lstrip()[6:]
        print(UI + '\n')

def SCD(UI: str) -> str:
    print(Path.cwd())
    print()

def CHCD(UI: str) -> None:
    LUI: list[str] = UI.strip().split()

    if len(LUI) == 1:
        print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} You should give arguments.\n')
    
    else:
        try:
            chPath: Path = Path(' '.join(LUI[1:]))

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}')
            print()

        else:
            try:
                os.chdir(chPath)

            except Exception as e:
                print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}')
                print()

            else:
                print()

def LDF(UI: str) -> str:
    LUI: list[str] = UI.strip().split()

    if len(LUI) != 1:
        print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} You give {len(LUI) - 1} arguments but "ldf" command take just no argument.\n')

    else:
        crPath: Path = Path.cwd()
        DandF: list[str] | list = [entry.name for entry in crPath.iterdir()]
        if not DandF:
            print('There is no file or a folder in this directory.\n')

        else:
            for piece in DandF:
                print(f'{piece} - {os.path.getsize(piece)} Byte')

            print()

def BOOM(UI: str) -> None | str:
    LUI: list[str] = UI.strip().split()[1:]

    if LUI[0] in CMODS["BOOM"] and len(LUI) == 3:
        if LUI[1][-1] not in ["/", "\\"]:
            LUI[1] = LUI[1] + '/'

        tPath: Path = Path(''.join(LUI[1:])) #-t C:/Beautiful_Directory/ another_perfect_folder_name
        # C:/Beautiful_Directory/another_perfect_folder_name

        try:
            os.mkdir(tPath)

        except FileExistsError:
            print('This folder already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL} [C:102]\n')

        else:
            print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Created the folder.\n')

    elif len(LUI) == 1:
        try:
            os.mkdir(LUI[0])

        except FileExistsError:
            print('This folder already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}\n')

        else:
            print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Created the folder.\n')
    
    else:
        print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} Please control your mod or number of given arguments.\n')

def LEAF(UI: str) -> None | str:
    LUI: list[str] = UI.strip().split()[1:]

    if LUI[0] in CMODS["LEAF"] and len(LUI) == 3:
        if LUI[1][-1] not in ["/", "\\"]:
            LUI[1] = LUI[1] + '/'

        tPath: Path = Path(''.join(LUI[1:])) #-t C:/Beautiful_Directory/ another_perfect_file_name.blahblah
        # C:/Beautiful_Directory/another_perfect_file_name.blahblah

        try:
            tPath.touch()

        except FileExistsError:
            print('This file already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL} [C:103]\n')

        else:
            print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Created the file.\n')

    elif len(LUI) == 1:
        try:
            tPath: Path = Path(LUI[0])
            tPath.touch()

        except FileExistsError:
            print('This file already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}\n')

        else:
            print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Created the file.\n')
    
    else:
        print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} Please control your mod or number of given arguments.\n')

def D(UI: str) -> None | str:
    LUI: list[str] = UI.strip().split()[1:]

    if LUI[0] in CMODS["LEAF"] and len(LUI) == 3:
        if LUI[1][-1] not in ["/", "\\"]:
            LUI[1] = LUI[1] + '/'
    
        tPath: Path = Path(''.join(LUI[1:])) #-t C:/Beautiful_Directory/ another_perfect_file_name.blahblah
        # C:/Beautiful_Directory/another_perfect_file_name.blahblah

        try:
            if tPath.is_file():
                tPath.unlink()
                print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Deleted the file.\n')
            
            elif tPath.is_dir():
                shutil.rmtree(tPath)
                print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Deleted the folder.\n')

            else:
                print('Path doesn\'t exist.\n')
        
        except FileExistsError:
            print('This file already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}\n')

    elif len(LUI) == 1:
        tPath: Path = Path(LUI[0])
        
        try:
            if tPath.is_file():
                tPath.unlink()
                print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Deleted the file.\n')
            
            elif tPath.is_dir():
                shutil.rmtree(tPath)
                print(f'{F.GREEN + S.BRIGHT}Successful!{S.RESET_ALL} Deleted the folder.\n')

            else:
                print('Path doesn\'t exist.\n')
        
        except FileExistsError:
            print('This file already exist.\n')

        except PermissionError:
            print('You don\'t have enough permission.\n')

        except Exception as e:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}{e}{S.RESET_ALL}\n')
            
    else:
        print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} Please control your mod or number of given arguments.\n')

def main() -> str | None:
    print(f'{F.YELLOW + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}To get help write "yphus".{S.RESET_ALL}')
    JSON_VERSION()
    print()

    while True:
        UI: str = takeInput()
        LUI: list[str] | list = lexingProcess(UI)

        if not UI.split():
            pass

        elif UI.strip().lower() in ['q', 'quit', 'exit']:
            break

        elif UI.strip().lower() in ['cl', 'cls']:
            os.system('cls')

        elif UI.strip().lower() == 'yphus':
            YPHUS()

        elif LUI[0] == 'punch':
            PUNCH(UI)

        elif UI.strip().lower() == 'scd':
            SCD(UI)

        elif LUI[0] == 'chcd':
            CHCD(UI)

        elif LUI[0] == 'ldf':
            LDF(UI)
        
        elif LUI[0] == 'boom':
            BOOM(UI)

        elif LUI[0] == 'leaf':
            LEAF(UI)

        elif LUI[0] == 'd':
            D(UI)

        else:
            print(f'{F.LIGHTRED_EX + S.BRIGHT}Syntax Error!{S.RESET_ALL} There is no command like this.\n')

if __name__ == '__main__':
    main()