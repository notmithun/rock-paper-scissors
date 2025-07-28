try:
    from colorama import init, Fore, Style
    import shutil
    import os
    os.system("cls")
    from time import sleep
    from random import choice
    # Init colorama
    init(autoreset=True)

    points = {
        "ai": 0,
        "human": 0
    }

    def print_round_banner(text: str):
        width = shutil.get_terminal_size().columns
        text = f" {text} "
        side_len = (width - len(text)) // 2
        line = "-" * side_len + text + "-" * (width - side_len - len(text))
        print(line)


    def check(player_choice: str, ai_choice: str, player_name: str) -> str:
        pc = player_choice
        ai = ai_choice

        if pc == ai:
            return "The game has ended in a draw!"
        elif (
            (pc == "Rock" and ai == "Scissors") or
            (pc == "Paper" and ai == "Rock") or
            (pc == "Scissors" and ai == "Paper")
        ):
            return f"{player_name} has won this round!"
        else:
            return "The AI has won this round!"

    def game(player_name: str):
        round = 1
        print("Rock, Paper, Scissors has been started!")
        game_on = True
        while game_on:
            os.system("cls")
            print(f"""Points are:
    {player_name}: {points["human"]}
    AI: {points['ai']}""")
            print_round_banner(f"ROUND {round}")
            print(f"{Fore.CYAN}Please choose your option:{Style.RESET_ALL}\n{Fore.BLUE}Type the number to choose that option!:{Style.RESET_ALL}\n\n{Fore.GREEN}1 - Rock 🪨{Style.RESET_ALL}\n{Fore.LIGHTRED_EX}2 - Paper 📄{Style.RESET_ALL}\n3 - Scissors ✂️\n\n")
            while True:
                try:
                    pc: int = int(input(f"{Fore.MAGENTA}What is your choice?(1, 2 or 3): {Style.RESET_ALL}"))
                    if pc not in [1, 2, 3]:
                        raise ValueError("Please enter numbers 1, 2 or 3!")
                except ValueError:
                    print(f"{Fore.RED}Please enter numbers 1, 2 or 3")
                    continue
                if pc == 1:
                    player_choice = "Rock"
                    break
                elif pc == 2:
                    player_choice = "Paper"
                    break
                elif pc == 3:
                    player_choice = "Scissors"
                    break
            print("Now it's time for the truth! Who has won this round?")
            ai_choice = choice(["Rock", "Paper", "Scissors"])
            winner = check(player_choice, ai_choice, player_name)
            sleep(1.5)
            if winner == f"{player_name} has won this round!":
                print(f"""You choose: {player_choice}\nThe AI choose: {ai_choice}""")
                print(f"{Fore.GREEN}{winner}")
                print(f"{Fore.GREEN}You have also got a point!")
                points["human"] = points["human"] + 1
                os.system("pause")
            elif winner == "The AI has won this round!":
                print(f"""You choose: {player_choice}\nThe AI choose: {ai_choice}""")
                print(f"{Fore.YELLOW}{winner}")
                print(f"{Fore.YELLOW}AI has got a point!")
                points["ai"] = points["ai"] + 1
                os.system("pause")
            else:
                print(f"""You choose: {player_choice}\nThe AI choose: {ai_choice}""")
                print(f"{Fore.YELLOW}{winner}")
                print("No one has got a point!")
                os.system("pause")
            if round == 5:
                print("The games have finally came to an end!")
                print(f"{Fore.GREEN}The winner is...")
                sleep(2.5)
                if points["human"] > points["ai"]:
                    print(f"{Fore.GREEN}You! {player_name} has won the game with {points['human']}! GG!")
                elif points["human"] < points["ai"]:
                    print(f"{Fore.YELLOW}AI! AI has won the game with {points['ai']}! GG!")
                elif points["human"] == points["ai"]:
                    print(f"{Fore.YELLOW}The games have ended in a draw! GG!")
                print("Would you like to play again? (y/n)")
                x = input(f"{Fore.MAGENTA}> {Style.RESET_ALL}")
                if x == "y":
                    points["human"] = 0
                    points["ai"] = 0

                    game(player_name)
                else:
                    exit(0)
            else:
                round = round + 1


    def home():
        banner_text = r"""
        ______ _____ _____  _   __   ______  ___  ______ ___________     _____ _____ _____ _____ _____  ___________  _____ 
        | ___ \  _  /  __ \| | / /   | ___ \/ _ \ | ___ \  ___| ___ \   /  ___/  __ \_   _/  ___/  ___||  _  | ___ \/  ___|
        | |_/ / | | | /  \/| |/ /    | |_/ / /_\ \| |_/ / |__ | |_/ /   \ `--.| /  \/ | | \ `--.\ `--. | | | | |_/ /\ `--. 
        |    /| | | | |    |    \    |  __/|  _  ||  __/|  __||    /     `--. \ |     | |  `--. \`--. \| | | |    /  `--. \\
        | |\ \\ \_/ / \__/\| |\  \_  | |   | | | || |   | |___| |\ \ _  /\__/ / \__/\_| |_/\__/ /\__/ /\ \_/ / |\ \ /\__/ /
        \_| \_|\___/ \____/\_| \_( ) \_|   \_| |_/\_|   \____/\_| \_( ) \____/ \____/\___/\____/\____/  \___/\_| \_|\____/ 
                                |/                                 |/                                                     
        """

        # Credit line
        credit_text = "a game by Mithun :)"
        centered_credit = credit_text.center(shutil.get_terminal_size().columns)

        # Print it with color
        print("Welcome to...")
        print(Fore.CYAN + banner_text)
        print(Fore.YELLOW + centered_credit + Style.RESET_ALL)

        sleep(2.5)

        os.system("pause")
        print(f"{Fore.CYAN}Before we start, please tell us your name!")
        name = input(f"{Fore.MAGENTA}> {Style.RESET_ALL}") or "Guest"
        if name == "Guest":
            print("Don't want to tell us your name? It's cool! You'll just be known as 'Guest'!")
        print(f"{Fore.YELLOW}Things to note before the game starts:{Style.RESET_ALL}\n\n1 - Click `CTRL (Contorl) and C` to exit the game whenever you want safely!\n2 - This version of Rock, Paper, Scissors games contains 5 rounds of RPS{Style.RESET_ALL}")
        print("Now let's start shall we?")
        os.system("pause")
        os.system("cls")
        game(name)

    if __name__ == "__main__":
        home()
except KeyboardInterrupt:
    print(f"\n{Fore.RED}The games have been halted!{Style.RESET_ALL}")