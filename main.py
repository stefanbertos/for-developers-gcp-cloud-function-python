from google.cloud import logging


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Instantiates a client
    logging_client = logging.Client()
    # The name of the log to write to
    log_name = "hello-function-log"
    # Selects the log to write to
    logger = logging_client.logger(log_name)
    # Writes the log entry simple text
    logger.log_text("My function is starting")

    request_json = request.get_json()  # see https://flask.palletsprojects.com/en/2.0.x/api/ get_json Parse data as JSON

    logger.log_text("Request headers:" + str(request.headers))

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        logger.log_text("sending the default response as no input was provided", severity="WARNING")
        return f'Hello World!'
