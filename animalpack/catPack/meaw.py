def spea_direct():
    print("meow direct")

def speak_imported():
    print("meow imported")


def test():
    print("meow test")


if __name__=="__main__":   #direkt olarak çalıstırıldığında bu
    spea_direct()

else:
    speak_imported()   #import olarak alıp çalıstırdığımızda bu çalısır
