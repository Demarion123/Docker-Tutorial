import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format for log messages
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)

# Create a custom logger
logger = logging.getLogger(__name__)

def divide_numbers(a, b):
    logger.debug(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Division by zero error", exc_info=True)
        return None
    except Exception as e:
        logger.exception("Unexpected error occurred")
        return None

if __name__ == "__main__":
    logger.info("Starting the division script")
    
    num1 = 10
    num2 = 0  # This will cause a division by zero error
    
    result = divide_numbers(num1, num2)
    if result is None:
        logger.warning("Result is None due to an error in division")
    
    num3 = 5
    num4 = 2
    
    result = divide_numbers(num3, num4)
    if result is not None:
        logger.info(f"Result of division: {result}")
    
    logger.info("Script finished")

