import logging
import ssl
import click
import dokuwiki as doku_wiki
import os


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
@click.option('--username', prompt=True, envvar='USERNAME')
@click.option('--password', prompt=True, envvar='PASSWORD', hide_input=True, confirmation_prompt=False)
@click.option("--data-dir", "-d", "data_dir", envvar='DATA_DIR', required=True,
              help="Input data dir.",
              type=click.Path(exists=True, dir_okay=True, readable=True),)
@click.option("--data-dir-mask", "-m", "data_dir_mask", envvar='DATA_DIR_MASK', required=False,
              help="Files mask for option '--data-dir-mask'.",)
@click.option("--namespace", "-n", envvar='NAMESPACE', required=True,
              help="Dokuwiki namespace.",)              
def dokuwiki(username, password, data_dir, data_dir_mask, namespace):
    # Отключение верификации сертификата
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    wiki = doku_wiki.DokuWiki(
        'https://bcvm750.dev.ts:10447', username, password)
    #print(wiki.pages.list('/'))
    #wiki.pages.set('start', '** Тест1 **')

    # Публикуем доки

    


log = setlogger()

if __name__ == '__main__':
    cli(auto_envvar_prefix='PUBDOC')
