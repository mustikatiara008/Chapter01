import time
from do_something import * # Melakukan import dari file do_something.py (import semua yang ada di file tersebut)

# IMplementasi dari penggunaan function do_sumething yang dimanaakan membuat sebuah list integer dengan jumlah eksekusi
if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)

