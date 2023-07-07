from scripts.api.handlers.handlers import Handling
from scripts.api.schemas.response_schema import DefaultFailureResponse, DefaultResponse

class Service:
    def create_an_item(item):
        """ A function that calls the newentry function from handling which takes one entry and inserts it into the database
        params: one item according to the format of the table
        returns:success and the entry that has just been inserted else Failed and exception
        """
        try:
            return DefaultResponse(message="Success", data=Handling.new_entry(item))
        except Exception as e:
            return DefaultFailureResponse(
                message="Failed", error=str(e)
            ).dict()
    def download_file():
        """ A function that calls the report function from handling which return a csv file containing the report
        params: NA
        returns: A CSV file containing the reports else Failed and the exception
        """
        try:
            return Handling.report()
        except Exception as e:
            return DefaultFailureResponse(
                    message="Failed", error=str(e)
                ).dict()
        

    