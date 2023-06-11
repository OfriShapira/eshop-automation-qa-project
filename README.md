# Final Project for Automation Development Certification by Ofri shapira 
## Introduction
As part of the final project for the training program, i've designed and developed an end-to-end automation infrastructure in
Pytest for a microservices-based web application, in addition to planning the full QA process,
writing a variety of manual test cases and integrating them into the automation infrastructure.<br />The test cases will be based on the ordering micro service that will function as a “Unit Under Test”.
 
## System under test description
The SUT for the project is called “EshopOnline”. It’s an online shop website which includes client applications, backend micro services, API Gateways, DBs and an Event bus to communicate between the micro services.
The whole system is launched as a docker containers on the local machine.
Each micro service is running independently as listed in the diagram below:

<img src="https://github.com/dotnet-architecture/eShopOnContainers/raw/dev/img/eShopOnContainers-architecture.png" alt="Eshop containers architecture">

## List of services:
* Basket API – Handles shopping basket
* Catalog API – Handles the store catalog
* Identity API – Handles shop customers
* Payment API – Handles customer payments
* Ordering API – Handles orders after purchases
* Event bus – Handles communications between services
* Web status – Shows the status of each service
* Web/mobile clients – Used for system review / manual testing

## The QA process documents
The test plan for the project can be found [here](https://github.com/OfriShapira/eshop-automation-qa-project/blob/ofri-shapira/documents/std/Test%20Plan%20-%20Orders%20Service%20-%20Ofri%20Shapira.docx) (click on 'View raw' to download).<br />
The project summary presentation can be found [here](https://github.com/OfriShapira/eshop-automation-qa-project/tree/ofri-shapira/documents/presentation) (click on 'View raw' to download).

## The automation infrastructure
The automation infrastructure for the ordering service has been written in python, using Pytest as the testing framework, and composed from the following components:
* Tests suites package – contains the actual tests to run.
* Scenarios package - meant to add shared steps functionality to the tests.
* Simulators package – contains a couple of microservices simulators that are mocking RabbitMQ message publication and consumption.
* Message Generator class (data factory implementation) – class that generates unique RabbitMQ messages.
* Utils package – contains utilities wrapper classes for: Ordering API, SQL Server driver, Docker API and Pika library (for communicate with RabbitMQ).
