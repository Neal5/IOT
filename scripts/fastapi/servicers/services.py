from scripts.fastapi.handlers.handlers import handling
from scripts.fastapi.schemas.response_schema import DefaultFailureResponse, DefaultResponse
class service:
    def create_an_item(item):
        """ A function that calls the newentry function from handling which takes one entry and inserts it into the database
        params: one item according to the format of the table
        returns:success and the entry that has just been inserted else Failed and exception
        """
        try:
            # new_item = handling.newentry(item)

            # return handling.newentry(item)
            return DefaultResponse(message="Success", data=handling.newentry(item))
        except Exception as e:
            # print(e)
            return DefaultFailureResponse(
                message="Failed", error=str(e)
            ).dict()