import logging

# Create and Configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="c:\\Python\\loggingTest.log",
                    level =logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

# Test the logger
logger.info("our first message")
