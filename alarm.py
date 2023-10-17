import playsound
import time
CLEAR = "\033[2]"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elasped = 0;
    print(CLEAR)

    while time_elasped < seconds:
        time.sleep(1);
        time_elasped +=1;

        time_left = seconds - time_elasped;
        min_left = time_left // 60;
        sec_left = time_left % 60;
        print(f"{CLEAR_AND_RETURN}time left is ${min_left:02d}:{sec_left:02d}")


alarm(5);