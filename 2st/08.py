import os, psutil

def get_process_name():
    pid = os.getpid()
    
    for proc in psutil.process_iter():
        try:
            proc_pid = proc.pid
            if proc_pid == pid:
                proc_name = proc.name()
                return proc_name
        
        except psutil.NoSuchProcess:
            pass

    return "No such process"

if __name__ == '__main__':
    print('프로세서 이름 : ', get_process_name())