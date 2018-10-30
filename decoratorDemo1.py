#Decorator Function is a wrapper function
#It Receives function as an argument
#Returns a Function

def logit(original_func):
    def new_func():
        print("Start Logging")
        original_func()
        print("Stop Logging")
    return new_func

@logit
def print_status():
    print("Processing")
    

if __name__ == '__main__':
    #print_status = logit(print_status)
    #print(print_status)
    print_status()
