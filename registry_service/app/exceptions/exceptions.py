class NotFoundError(Exception):

    def __init__(self, id: int, entity: str):
            super().__init__(f"{entity} id({id}) not found")