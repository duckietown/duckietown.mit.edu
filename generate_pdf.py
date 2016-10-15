#!/usr/bin/env python
import logging
logging.basicConfig()
import sys, yaml, os, urllib2, platform
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from system_cmd import system_cmd_result

def main():
    try:

        documents_data = sys.stdin.read()
        documents = yaml.load(documents_data)

        out = 'media/pdfs'

        if not os.path.exists(out):
            os.makedirs(out)

        errors = []
        pdfs = []

        for d in documents:
            id_document = get_id(d)
            if (d['tags'] == 'paper'):
                continue

            pdf_url = make_pdf_url(id_document)

            pdf_file = os.path.join(out, id_document + '.pdf')

            if os.path.exists(pdf_file):
                pdfs.append(pdf_file)
            else:
                logger.info('Downloading %s' % pdf_file)
                response = urllib2.urlopen(pdf_url)
                data = response.read()

                is_valid = (data[1:4] == 'PDF')

                if is_valid:
                    with open(pdf_file, 'w') as f:
                        f.write(data)
                    pdfs.append(pdf_file)
                else:
                    logger.error('Invalid response for document %r' % d)
                    errors.append(id_document)
                    with open(pdf_file + '.invalid-response.html', 'w') as f:
                        f.write(data)


        pdfout = 'joined.pdf'

        cmd = ['pdftk']
        cmd.extend(pdfs)
        cmd.extend(['cat', 'output', pdfout])

        system_cmd_result(
            cwd='.', cmd=cmd,
            display_stdout=True,
            display_stderr=True,
            raise_on_error=True)


        with open(pdfout) as f:
            data = f.read()
        logger.info('Writing on stdout %s' % len(data))
        sys.stdout.write(data)

        if errors:
            logger.error('Could not download all files.')
            sys.exit(2)


    except Exception as e:
        import traceback
        logger.error(traceback.format_exc(e))
        sys.exit(-1)

def make_pdf_url(id_document):
    return 'https://docs.google.com/document/d/%s/export?format=pdf' % id_document

def get_id(d):
    s = d['google_docs_share_link']
    
    # "https://docs.google.com/document/d/1hIZftFCZEpcvL-yp8kkYMjWzGBiNcwajdn2_ZxeirIM/edit?usp=sharing"
    s = s.replace('https://docs.google.com/document/d/', '')
    s = s.replace('https://drive.google.com/file/d/','')
    s = s.replace('/edit?usp=sharing','')
    s = s.replace('/view?usp=sharing','')
    s = s.replace('https://drive.google.com/open?id=', '')

    return s

def add_coloring_to_emit_ansi(fn):
    # add methods we need to the class
    def new(*args):
        levelno = args[1].levelno
        if(levelno >= 50):
            color = '\x1b[31m'  # red
        elif(levelno >= 40):
            color = '\x1b[31m'  # red
        elif(levelno >= 30):
            color = '\x1b[33m'  # yellow
        elif(levelno >= 20):
            color = '\x1b[32m'  # green
        elif(levelno >= 10):
            color = '\x1b[35m'  # pink
        else:
            color = '\x1b[0m'  # normal

        args[1].msg = color + str(args[1].msg) + '\x1b[0m'  # normal
        return fn(*args)
    return new

if platform.system() != 'Windows':
    emit2 = add_coloring_to_emit_ansi(logging.StreamHandler.emit)
    logging.StreamHandler.emit = emit2

if __name__ == '__main__':
    main()

