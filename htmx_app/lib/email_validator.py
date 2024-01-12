import logging

log = logging.getLogger(__name__)


def validate_email( email_data ):
    """ Validates email. """
    if email_data == '':
        rslt = False
    else:
        rslt = True
    log.debug( f'rslt, ``{rslt}``' )
    return rslt