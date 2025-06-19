import psutil

def ProcessDisplay():
    border = "*"*70
    
    print("\n", border)
    print("Information of currently running processes: ")
    print(border, "\n")

    for proc in psutil.process_iter():    #iter = iterate
        info = proc.as_dict(attrs=['pid', 'name', 'username']) 
        info['vms'] = proc.memory_info().vms / (1024 * 1024)   #vms = virtual memory
        print(info)

def main():
    ProcessDisplay()


if __name__ == "__main__":
    main()    
    
