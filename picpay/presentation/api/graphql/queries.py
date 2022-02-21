import strawberry


@strawberry.type
class Queries:

    @strawberry.field
    def hello(self) -> str:
        return "Hello"
