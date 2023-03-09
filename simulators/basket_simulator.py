import uuid

from utils.rabbitmq.rabbitmq_send import RabbitMQ


class BasketSimulator(RabbitMQ):

    def __init__(self, body, order_start_integration_message="OrderStartedIntegrationEvent",
                 accept_user_checkout="UserCheckoutAcceptedIntegrationEvent",
                 order_status_changed_to_submitted="OrderStatusChangedToSubmittedIntegrationEvent",
                 exchange="eshop_event_bus"):
        super().__init__()
        self.__order_start_integration_message = order_start_integration_message
        self.__accept_user_checkout = accept_user_checkout
        self.__order_status_changed_to_submitted = order_status_changed_to_submitted
        self.__exchange = exchange
        self.__body = body
        self.__queue = "Basket"

    def start_order_integration_listener(self):
        self.consume(self.__queue)
        pass

    def accept_user_checkout(self):
        self.publish(self.__exchange, self.__user_checkout_accepted_message, body=self.__body)

    def send_order_status_changed_to_submitted(self):
        self.publish(self.__exchange, self.__order_status_changed_to_submitted, body=self.__body)


# if __name__ == '__main__':
#     body = {
#         "UserId": "5b2eb009-f2b4-4406-a2a5-2949721f7872",
#         "UserName": "alice",
#         "OrderNumber": 0,
#         "City": "Redmond",
#         "Street": "15703 NE 61st Ct",
#         "State": "WA",
#         "Country": "U.S.",
#         "ZipCode": "98052",
#         "CardNumber": "4012888888881881",
#         "CardHolderName": "Alice Smith",
#         "CardExpiration": "2024-12-31T22:00:00Z",
#         "CardSecurityNumber": "123",
#         "CardTypeId": 1,
#         "Buyer": None,
#         "RequestId": str(uuid.uuid4()),
#         "Basket": {
#             "BuyerId": "5b2eb009-f2b4-4406-a2a5-2949721f7872",
#             "Items": [
#                 {
#                     "Id": "ec13598b-9a25-4624-b0a0-e9069be548d2",
#                     "ProductId": 1,
#                     "ProductName": ".NET Bot Black Hoodie",
#                     "UnitPrice": 19.5,
#                     "OldUnitPrice": 0,
#                     "Quantity": 1,
#                     "PictureUrl": "http://host.docker.internal:5202/c/api/v1/catalog/items/1/pic/"
#                 },
#                 {
#                     "Id": "43b0d9d0-802b-4987-b9a1-b648b094f5d3",
#                     "ProductId": 6,
#                     "ProductName": ".NET Blue Hoodie",
#                     "UnitPrice": 12,
#                     "OldUnitPrice": 0,
#                     "Quantity": 1,
#                     "PictureUrl": "http://host.docker.internal:5202/c/api/v1/catalog/items/6/pic/"
#                 },
#                 {
#                     "Id": "1c82cfd8-099b-4ea2-854f-7ee287684a08",
#                     "ProductId": 2,
#                     "ProductName": ".NET Black \u0026 White Mug",
#                     "UnitPrice": 8.5,
#                     "OldUnitPrice": 0,
#                     "Quantity": 1,
#                     "PictureUrl": "http://host.docker.internal:5202/c/api/v1/catalog/items/2/pic/"
#                 }
#             ]
#         },
#         "Id": "c008b3e0-e95a-44ec-a1a0-0916931c33d0",
#         "CreationDate": "2023-03-06T19:18:10.7326158Z"
#
#     }
#
#     with BasketSimulator(body) as mq:
#         mq.start_order_integration_listener()
