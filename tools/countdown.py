import time
import sys


def count():
    print("Waiting to re-run: ")

    animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    # animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□",
    # "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    try:
        for i in range(len(animation)):
            time.sleep(5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
    except:
        print("\nExit..")
        sys.exit(0)

    print("\n")