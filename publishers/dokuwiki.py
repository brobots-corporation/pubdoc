
from collections import namedtuple
import pathlib
import os
import dokuwiki

document = namedtuple("Record", ['file_path', 'publish_path', 'original_path'])

class DokuWikiPub:
    
    dokuwiki_supported_input_format_file = ['md', 'MD']

    def __init__(self, log, target, username, password, root_namespace):
        super().__init__()
        self.target = target
        self.username = username
        self.password = password
        self.root_namespace = root_namespace
        self.docs = list()
        self.log = log
    
    def from_dir(self, path, mask):
        self.log.info(" Loading documents from %s" % str(path))
        docs = list()
        root = pathlib.Path(path)
        for data_file in root.glob(mask):
            if data_file.is_file():

                filename = os.path.basename(os.path.realpath(data_file))
                relpath = os.path.relpath(data_file, path)
                file_path = os.path.realpath(data_file)
                name = os.path.splitext(filename)[0]

                # Skiop file If file extension not in suppoted format
                extension = file_path.split('.')[-1]
                if extension not in self.dokuwiki_supported_input_format_file:
                    self.log.debug(" Skip %s" % data_file)
                    continue

                self.log.info(" Loaded %s" % str(data_file))
                lnk = relpath.split('/')
                for i in range(len(lnk[:-2])):
                    lnk[i] = lnk[i].replace('.', '_')
                original_path = ':'.join(lnk)
                lnk.insert(0, self.root_namespace)
                publish_path = ':'.join(lnk)

                self.docs.append(document(file_path=file_path,
                                    publish_path=publish_path,
                                    original_path=original_path))
        return docs

    def publish(self):
        try:
            self.log.info("Connect to %s as %s" % (self.target, self.username))
            wiki = dokuwiki.DokuWiki(self.target, self.username, self.password)
        except (dokuwiki.DokuWikiError, Exception) as err:
            self.log.error('Unable to connect: %s' % err)
            exit(1)

        # print(wiki.pages.list('/'))   
        for doc in self.docs:
            with open(doc.file_path,'r') as fread:
                data = fread.read()
                wiki.pages.set(doc.publish_path, data)


