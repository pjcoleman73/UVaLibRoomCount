from interruptingcow import timeout
import time

while True:
    # simulate waiting for laser A
    print("Waiting for laser A")
    time.sleep(2)
    print("laser A tripped")
    try:
        with timeout(.25, exception=RuntimeError):
            # perform a potentially very slow operation
            print("Wait for laser B")
            time.sleep(2)
            print("laser B tripped, add 1 to DB")
            pass
    except RuntimeError:
        print "didn't finish within .25 seconds"
