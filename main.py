from imports import *

running = True  #Until its True the program keeps running


while running:
    user = input(f"{random.choice(welcomes)} --->>")  # Takes input from the user(command)
    user = user.lower()    # This line make the input to lower

    if user in cmd_calc:
        szam1 = float(input("Szám 1: "))
        szam2 = float(input("Szám 2: "))
        task = input("Válassz műveletet(Összeadás/Kivonás/Szorzás/Osztás): ")
        osszeg = BasMath(task, szam1, szam2)
        osszeg = int(osszeg)
        print(f"Az összeg: {osszeg}")

    elif user in cmd_hlp:
        commands()

    elif user in cmd_clr:
        clear()
    
    elif user in cmd_time: 
        curr = time.ctime(1723899151.734237)
        print(f"Az idő jelenleg: {curr}")

    elif user in cmd_ext:
        exit(random.choice(goodbye))
        