import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(selfs):
        for _ in range(100):
            time.sleep(0.001)
            amount = random.randint(50,500)
            selfs.balance += amount
            if selfs.balance >= 500 and selfs.lock.locked():
                selfs.lock.release()
            print(f"Пополнение: {amount}. Баланс: {selfs.balance}")

    def take(self):
        for _ in range(100):
            time.sleep(0.001)
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            elif self.lock.locked():
                self.lock.acquire()
                print(f"Заппрос на {amount} отклонён, недостаточно средств")

bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')