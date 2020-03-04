
# pubdoc
Публикация документации

## Возможности
* Работа в ОС семейства: Linux, Mac OS X;
* Подерживается публикация на:
  * [DokuWiki](https://www.dokuwiki.org/)

## Установка и обновление

## Использование скрипта
```
Usage: pubdoc.py [OPTIONS] COMMAND [ARGS]...

Options:
  --log-level TEXT  Log level [CRITICAL, FATAL, ERROR, WARNING, DEBUG, INFO,
                    NOTSET]
  --help            Show this message and exit.

Commands:
  dokuwiki
```  
### Публикация на DokuWiki
Команда `dokuwiki`
```
Usage: pubdoc.py dokuwiki [OPTIONS]

Options:
  -t, --target TEXT         Dokuwiki url.  [required]
  --username TEXT           Dokuwiki username.  [required]
  --password TEXT           Dokuwiki password.  [required]
  -n, --namespace TEXT      Dokuwiki namespace.  [required]
  -d, --data-dir PATH       Input data dir.  [required]
  -m, --data-dir-mask TEXT  Files mask for option '--data-dir'.
  --help                    Show this message and exit.
```

#### Пример использования скрипта в Linux
```sh
pubdoc.py dokuwiki \
    --target 'https://bla.bla.com' \
    --username 'Логин' \
    --password 'Пароль' \
    --namespace 'Проект 1:Техническая документация' \
    --data-dir './testdocs' \
    --data-dir-mask '**/*.md'
```

#### Пример использования скрипта в Linux c использованием переменных среды
```sh
export PUBDOC_DOKUWIKI_TARGET='https://bla.bla.com'
export PUBDOC_DOKUWIKI_USERNAME='Логин'
export PUBDOC_DOKUWIKI_PASSWORD='Пароль'
export PUBDOC_DOKUWIKI_NAMESPACE='Проект 1:Техническая документация'
export PUBDOC_DOKUWIKI_DATA_DIR='./testdocs'
export PUBDOC_DOKUWIKI_DATA_DIR_MASK='**/*.md'
export PUBDOC_LOG_LEVEL='DEBUG'
pubdoc.py dokuwiki 
```