# importing the multiprocessing module
import multiprocessing
import time
from PyPDF2 import PdfReader, PdfWriter
import string
import itertools
import threading

def prime(core, lower, upper):

    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(f'{core}:{num}')

def crack(core, wordlist, file):
    reader = PdfReader(file)
    for paswd in wordlist:
        if reader.is_encrypted:
            result = str(reader.decrypt(paswd))
            if result == 'PasswordType.USER_PASSWORD':
                print(f'password={paswd}')


#if __name__ == "__main__":
def main(t):
    chars = string.digits
    chars = string.ascii_lowercase
    chars = string.digits + string.ascii_lowercase
    
    print(chars)
    wordlist = []
    # 3.7GHz CPUs 8 :
    # 94seconds = digits+ascii_lowercase repeat=4 wordlist length = 1.679.616
    # = digits+ascii_lowercase repeat=5 wordlist length = 60.466.176 (need +8G RAM)
    for xs in itertools.product(chars, repeat=5):
        wordlist.append(''.join(xs))

    div = int(len(wordlist)/2)
    print(len(wordlist))
    
    pdf_file = "VyplatnyListok_2024-10.pdf"
    print(multiprocessing.cpu_count())
    
    s = time.monotonic()

    cores = 8
    processes = []
    n = int(len(wordlist)/cores)
    for c in range(cores):
        a = c*n
        b = (c+1)*n
        if c+1 == cores:
            print(f'core {c+1} wordlist[{a}:]')
            processes.append(multiprocessing.Process(target=crack, args=(c, wordlist[a:], pdf_file)))
        else:
            print(f'core {c+1} wordlist[{a}:{b}]')
            processes.append(multiprocessing.Process(target=crack, args=(c, wordlist[a:b], pdf_file)))

    for process in processes: # start all processes
        process.start()
    
    for process in processes: # wait for all processes to complete
        process.join()
    
##    p1 = multiprocessing.Process(target=crack, args=(1, first_wordlist, pdf_file))
##    p2 = multiprocessing.Process(target=crack, args=(2, second_wordlist, pdf_file))
##    p3 = multiprocessing.Process(target=crack, args=(3, third_wordlist, pdf_file))
##    p4 = multiprocessing.Process(target=crack, args=(4, fourth_wordlist, pdf_file))
##    #p1 = multiprocessing.Process(target=prime, args=(1, 100000, 140000))
##
##    p1.start()
##    p2.start()
##    p3.start()
##    p4.start()
##    
##    p1.join()
##    p2.join()
##    p3.join()
##    p4.join()
    
    # both processes finished
    e = time.monotonic()
    print(f"Done! {e-s}")


if __name__ == "__main__":
    t1 = threading.Thread(target=main, args=(1,))
    t1.start()
    t1.join()
    print('The End')
