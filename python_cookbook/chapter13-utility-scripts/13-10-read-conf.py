from configparser import ConfigParser

cfg = ConfigParser()
print(cfg.read('config.ini'))
print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('Server', 'port'))
