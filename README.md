# Automation Development Certification - Ness - Final Project
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
