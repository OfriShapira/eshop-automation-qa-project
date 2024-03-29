import os
from time import sleep

from dotenv import load_dotenv

from config.constants import *
from simulators.service_simulator import ServiceSimulator
from utils.db.db_utils import MSSQLConnector

load_dotenv()


class BasketSimulator(ServiceSimulator):
    """
    A class that simulate the Basket microservice's input and output messages to RabbitMQ
    """

    def __init__(self):
        """
        Basket simulator class initializer.
        """
        super().__init__(queue=BASKET_QUEUE_NAME, confirm_routing_key=BASKET_TO_ORDER_ROUTING_KEY)

    def send_message_to_create_an_order(self, body):
        """
        Method to start the ordering process, by sending a confirmation message from the basket simulator to the ordering queue.
        Parameters:
            body: The payload of the message.
        """
        # The basket simulator sends to the ordering queue the validation for starting to create a new order.
        self.send_confirmation_message(body=body)
        # Wait for the order to enter the db.
        sleep(10)

        # Set the current order id.
        ServiceSimulator.CURRENT_ORDER_ID = self.get_order_id()
        print(
            f"Message Route: Basket -> Ordering. Routing Key: UserCheckoutAcceptedIntegrationEvent. Current Order ID is: {ServiceSimulator.CURRENT_ORDER_ID}")

    def get_order_id(self):
        """
        Method to get the current order id, by fetching the last order id that has been entered to the table.
        Returns:
            The current order id.
        """
        try:
            with MSSQLConnector() as conn:
                order_id = conn.select_query(
                    # In the below query, we fetch the last user order (max order id).
                    "SELECT MAX(o.Id) FROM ordering.orders o")
                return order_id[0]['']
        except ConnectionError as c:
            raise f'There were problem to retrieve the order id.\nException is: {c}'
