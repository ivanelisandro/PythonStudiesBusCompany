logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
log_format = '%(levelname)s -> %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


def hypotenuse(side_1, side_2):
    h = round(((side_1 ** 2 + side_2 ** 2) ** 0.5), 2)
    logger.info('Hypotenuse of %s and %s is %s', side_1, side_2, h)
    return h
