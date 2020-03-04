import click
import logging

def setlogger():
    log = logging.getLogger("pubdoc")
    log.setLevel(logging.DEBUG)
    fh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log

@click.group()
@click.option("--log-level", "log_level", envvar='LOG_LEVEL', required=False,
              help="Log level [CRITICAL, FATAL, ERROR, WARNING, DEBUG, INFO, NOTSET]",)
def cli(log_level):
    if log_level:
        log.setLevel(log_level)
    else:
        log.setLevel(logging.INFO)


@cli.command()
@click.option("--data-dir", "-d", "data_dir", envvar='DATA_DIR', required=False,
              help="Input data dir.",
              type=click.Path(exists=True, dir_okay=True, readable=True),)
@click.option("--data-dir-mask", "-m", "data_dir_mask", envvar='DATA_DIR_MASK', required=False,
              help="Files mask for option '--data-dir-mask'.",)
def dokuwiki(data_dir, data_dir_mask):
    pass

log = setlogger()

if __name__ == '__main__':
    cli(auto_envvar_prefix='PUBDOC')
