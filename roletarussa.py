import random
import os
import platform

def jogar():
    print("Welcome to Russian Roulette!")
    print("There is 1 bullet in a 6-chamber revolver.")
    print("Spin the chamber and pull the trigger...")

    chamber = [0, 0, 0, 0, 0, 1]
    random.shuffle(chamber)

    while True:
        input("Press Enter to pull the trigger...")
        shot = chamber.pop()

        if shot == 1:
            print("Bang! You're out!")
            shutdown_computer()
            break
        else:
            print("Click! You're safe... for now.")

        if not chamber:
            print("The revolver is empty. You survived!")
            break

    print("Game over!")

def shutdown_computer():
    os_name = platform.system()
    print("Shutting down the computer...")

    if os_name == "Windows":
        os.system("shutdown /s /t 1")
    elif os_name == "Linux" or os_name == "Darwin":  # Darwin = macOS
        os.system("shutdown -h now")
    else:
        print("Unsupported OS for shutdown command.")

if __name__ == "__main__":
    jogar()
