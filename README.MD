# Picpay Challenge

Challenge retirado do repositório [backend-challenge](https://github.com/CollabCodeTech/backend-challenges), criado com o intuito de praticar as seguintes tecnologias:

- [Python](https://www.python.org/)
- [GraphQL](https://graphql.org/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

# System Design / Architecture

O challenge foi criado utilizando o conceito de [Clean Architecture](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)

- Application
  - Camada responsável pelos usecases da aplicação, onde fazem a orquestração dos passos que devem ser realizados no domínio da aplicação.
- Domain
  - Camada responsável pelas entidades de domínio da aplicação.
- Infrastructure
  - Camada responsável por conter as implementações com o mundo externo, esses recursos são disponibilizados através de interfaces (portas).
- Presentation
  - Camada responsável pela visualização da API.
