import sys
from time import sleep
from queue import Queue
from threading import Thread, enumerate

# Создаем FIFO очередь
queue = Queue()


# Функция генерирующая данные для очереди
def source(n):
    for i in range(1, 1 + n):
        yield i


# Функция заполняющая очередь заданиями
def put(n):
    for item in source(n):
        queue.put(item)


def worker():
    while True:
        # Если заданий нет - закончим цикл
        if queue.empty():
            sys.exit()
        # Получаем задание из очереди
        item = queue.get()
        print(u'Очередь: %s выполняется' % item)
        # Сообщаем о выполненном задании
        queue.task_done()
        print(u'Очередь: %s завершилась' % item)


if __name__ == '__main__':

    # Создаем и запускаем потоки, которые будут обслуживать очередь
    for x in range(1, 4):
        print(u'Поток', str(x), u'стартовал')

        put(x)
        Thread(target=worker).start()

        sleep(2)

    print('Over')
