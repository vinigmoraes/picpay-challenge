import strawberry
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from strawberry.fastapi import GraphQLRouter

from picpay.presentation.api.graphql.mutations import Mutations
from picpay.presentation.api.validation.validation_exception import ValidationException
from picpay.presentation.api.graphql.queries import Queries

app = FastAPI(title="Picpay Challenge")


@app.exception_handler(ValidationException)
def handle_payments_api_exception(request: Request, exception: ValidationException):
    return JSONResponse(status_code=exception.status_code, content=exception.response())


if __name__ == "__main__":
    schemas = strawberry.Schema(Queries, Mutations)
    routes = GraphQLRouter(
        schemas
    )

    app.include_router(routes, prefix='/picpay')

    uvicorn.run(app, host="0.0.0.0", port=8080)
