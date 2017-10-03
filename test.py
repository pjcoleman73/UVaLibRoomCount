from interruptingcow import timeout
import time

# def bTripped():
#     +1 to DB
#     continue

while True:
    # simulate waiting for laser A
    print("Waiting for laser A")
    time.sleep(2)
    print("laser A tripped")
    # Real code would be:
    # laserA.wait_for_dark()
    try:
        with timeout(.25, exception=RuntimeError):
            # perform a potentially very slow operation
            print("Wait for laser B")
            time.sleep(2)
            print("laser B tripped, add 1 to DB")
            # Real code would be:
            # laserB.when_dark() = bTripped
            pass
    except RuntimeError:
        print "didn't finish within .25 seconds"
