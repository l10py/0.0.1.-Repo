import schedule
import time
import schedule


# Program 1
def program1():
    print("Program 1 dijalankan.")

# Program 2
def program2():
    print("Program 2 dijalankan.")

# Jadwalkan program 2 untuk dijalankan 10 detik setelah program 1 selesai
schedule.every(2).seconds.do(program2)
#schedule.after(10, program2)
# Jalankan program 1
program1()

# Tunggu selama 10 detik
time.sleep(10)

# Cek apakah program 2 telah dijalankan
if schedule.jobs:
    print("Program 2 telah dijalankan.")
else:
    print("Program 2 belum dijalankan.")