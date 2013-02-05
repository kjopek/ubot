import logging
import sys

def global_exc_handler(t, v, tb):
    tbinfo=[]

    logger = logging.getLogger('GLOBAL EXC')

    if not tb:
        raise AssertionError("traceback does not exist")

    while tb:
        tbinfo.append(
            (tb.tb_frame.f_code.co_filename,
             tb.tb_frame.f_code.co_name,
             str(tb.tb_lineno))
            )
        tb=tb.tb_next

    tbinfo.reverse()

    logger.fatal('%s: %s: '%(t.__name__,str(v)))
    logger.fatal('%s [%s %s]'%(tbinfo[0][1],tbinfo[0][0],tbinfo[0][2]))
    logger.fatal('Complete traceback:')

    for item in tbinfo[1:]:
        logger.fatal('  %s in %s [%s]' % (item[1],item[0],item[2]))

    sys.exit(1)
