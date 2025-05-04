# Documenation of the learning_sample_1

## The naming of the services has a meaning.
- The "business provider" focuses on being the first source of truth for the business that It drives, ie. an "n" service of sorts.
For "n" substiture any business domain like banking etc. It can have a few api's, like async http/2 WebApp api for constant data stream and 
ensuring the user that the thing that he needs is in the making and the system didn't just die. As well as a technical "integration" api which can be
used to utilize our data in some other service/business/place.
- "data_processor" is a service that focuses on receiving api calls, doing work and notifying about the work done via async message queue.
- "web" a plain bootstrap web app meant to provide some demo experience

## What is the main idea/technologies for each and one of them?
- "business provider" is meant to utilize python with a few libraries like Falcon, httpx, asyncio, trio, pytest and tech needed for http/2 connection between the WebApp.
- "data_processor" is to be based on spring + java persistence and rabbitmq broker connection lib.
- "web" typescript + angular

## What is the testing methodology?
- Automated grey box integration test suites, as well as black box e2e suites + unit test driven continuous dev.

## How are they going to be integrated?
- Dev will utilize dockerfiles + docker_compose as the orchestrator of docker.
- "Prod"(fake) will utilize Kubernetes to enable potential scalability and eventual loadbalancing across real-world computational nodes/machines.

## What arch style will be used in the system? 
- For development purposes this project will be considered a deployable monolith, because It will be treated as a single binary via the use of docker_compose.
- It is a distributed system which is utlizing a sort of pipeline/event driven architecture to provide the business value and needed metrics for effeciency and cost analysis. 

## And what style will be used in the particular services?
- "business_provider" is a DDD + hex based service utilizing modularized monolith arch flavour. While, It is worth mentioning, the mod monolith is actuallytaking patterns from other arch's like space-based
- "data_processor" is also a DDD + hex based service utilizing async computing if possible, ie. an event is created by a message queue receiving something. 
An web api is only used to retrieve the data after finishing the processing, ie. by sending a positive outcome event to the queue