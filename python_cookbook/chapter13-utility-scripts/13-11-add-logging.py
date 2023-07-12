import logging

def main():
    # configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )

    # variables (to make the calls that follow work)
    hostname = 'www.baidu.com'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("couldn't fine %r", item)
    logging.warning('feature is deprecated')
    logging.info('opening file %r, mode=%r', filename, mode)
    logging.debug('got here')

if __name__ == '__main__':
    main()