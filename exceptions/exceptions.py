from fastapi import HTTPException
class BadRequestException(HTTPException):
    def __init__(self)->None:
        super().__init__(status_code=400, detail="Product not created, invalid inputs")


class NotFoundException(HTTPException):
    def __init__(self)->None:
        super().__init__(status_code=404, detail="The Product not found")