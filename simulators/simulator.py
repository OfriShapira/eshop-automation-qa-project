from abc import ABC

from utils.rabbitmq.rabbitmq_send import RabbitMQ


class Simulator(ABC):
    """
    Class which contains general actions that a microservice simulator needs for communicating with RabbitMQ,
    """

    def __init__(self, queue):
        """
        The class initializer.
        """
        super().__init__()
        self.__queue = queue

    def get_first_message(self):
        """
         Method which reads the first messages from the given queue.

            :return: The first message in the basket queue.
        """
        try:
            with RabbitMQ() as mq:
                return mq.read_first_message(self.__queue)
        except ValueError as v:
            print(v)
        except BaseException as b:
            print(b)

    def purge_queue(self):
        """
        Method to purge the given queue.
        """
        try:
            with RabbitMQ() as mq:
                mq.purge_queue(self.__queue)
        except ValueError as v:
            print(v)
        except BaseException as b:
            print(b)
