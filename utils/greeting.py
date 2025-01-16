import logging

logger = logging.getLogger(__name__)

class Greeting:
    """
    Returns hello world string
    """

    def __init__(self, greeting: str = "hello") -> None:
        self.greeting = greeting

    def execute(self) -> str:
        """
        Return two available CIDRs for the new environment
        """
        try:
            return self.greeting
        except Exception as e:
            raise Exception(f"Greeting Unable to return string: {str(e)}")

def main():
    try:
        logging.basicConfig(level=logging.INFO)
        result = Greeting().execute()
        logger.info(f"Greeting: {Greeting().execute()}")
    except Exception as ex:
        logger.error(f"Main execution failed with {str(ex)}")

if __name__ == "__main__":
    main()
