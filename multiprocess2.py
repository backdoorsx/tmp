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
    #chars = string.ascii_lowercase
    print(chars)
    wordlist = []
    for xs in itertools.product(chars, repeat=5):
        wordlist.append(''.join(xs))

    div = int(len(wordlist)/2)
    print(len(wordlist))
    
    pdf_file = "VyplatnyListok_2024-10.pdf"
    
    s = time.monotonic()

    #zobrat kazde 4te
    div_first = int(len(wordlist[:div])/2)
    div_second = int(len(wordlist[div:])/2)

    first_wordlist = wordlist[:div]
    first_wordlist = first_wordlist[:div_first]
    second_wordlist = wordlist[:div]
    second_wordlist = second_wordlist[div_first:]

    third_wordlist = wordlist[div:]
    third_wordlist = third_wordlist[:div_second]
    fourth_wordlist = wordlist[div:]
    fourth_wordlist = fourth_wordlist[div_second:]
    
    p1 = multiprocessing.Process(target=crack, args=(1, first_wordlist, pdf_file))
    p2 = multiprocessing.Process(target=crack, args=(2, second_wordlist, pdf_file))
    p3 = multiprocessing.Process(target=crack, args=(3, third_wordlist, pdf_file))
    p4 = multiprocessing.Process(target=crack, args=(4, fourth_wordlist, pdf_file))
    #p1 = multiprocessing.Process(target=prime, args=(1, 100000, 140000))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    # both processes finished
    e = time.monotonic()
    print(f"Done! {e-s}")


if __name__ == "__main__":
    t1 = threading.Thread(target=main, args=(1,))
    t1.start()
    t1.join()
    print('The End')
