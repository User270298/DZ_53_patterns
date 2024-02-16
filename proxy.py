from abc import ABC, abstractmethod
from typing import Dict, List
import logging
from random import randint
import ast

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


class IServer(ABC):
    @abstractmethod
    def get_numbers(self) -> List[int]:
        pass

    @abstractmethod
    def sum_numbers(self) -> int:
        pass

    @abstractmethod
    def max_numbers(self) -> int:
        pass

    @abstractmethod
    def min_numbers(self) -> int:
        pass


class Server(IServer):

    def __init__(self):

        self.numbers: List[int] = []

    def get_numbers(self) -> List[int]:
        with open('number.txt', 'w') as f:
            f.write(f'{[randint(-100, 100) for _ in range(5)]}')
        with open('number.txt', 'r') as f:
            nums=f.read()
        self.numbers=ast.literal_eval(nums)
        return self.numbers

    def sum_numbers(self) -> int:
        return sum(self.numbers)

    def max_numbers(self) -> int:
        return max(self.numbers)

    def min_numbers(self) -> int:
        return min(self.numbers)


class ProxyServer(IServer):
    def __init__(self, server: Server):
        self.__server = server

    def get_numbers(self):
        logging.info(f'User input list {self.__server.get_numbers()}')
        return self.__server.get_numbers()

    def sum_numbers(self):
        logging.info(f'Sum all numbers {self.__server.sum_numbers()}')
        return self.__server.sum_numbers()

    def max_numbers(self):
        logging.info(f'Maximum {self.__server.max_numbers()}')
        return self.__server.max_numbers()

    def min_numbers(self):
        logging.info(f'Minimum {self.__server.min_numbers()}')
        return self.__server.min_numbers()


if __name__ == '__main__':
    my_curse = ProxyServer(Server())
    print(my_curse.get_numbers())
    print(my_curse.sum_numbers())
    print(my_curse.min_numbers())
    print(my_curse.max_numbers())
    my = ProxyServer(Server())
    print(my.get_numbers())
    print(my.sum_numbers())
    print(my.min_numbers())
    print(my.max_numbers())
    print(my.max_numbers())
    # my_server = ProxyServer(Server())
    # print(my_server.get_page(1))
    # print(my_server.get_page(2))
    # print(my_server.get_page(3))
    #
    # print(my_server.get_page(3))
