#
#
#

from ..idna import IdnaError, idna_decode


class RecordException(Exception):
    pass


class ValidationError(RecordException):
    @classmethod
    def build_message(cls, fqdn, reasons, context=None):
        reasons = '\n  - '.join(reasons)
        try:
            decoded = idna_decode(fqdn)
        except IdnaError:
            decoded = fqdn
        msg = f'Invalid record "{decoded}"'
        if context:
            msg += f', {context}'
        msg += f'\n  - {reasons}'
        return msg

    def __init__(self, fqdn, reasons, context=None):
        super().__init__(self.build_message(fqdn, reasons, context))
        self.fqdn = fqdn
        self.reasons = reasons
        self.context = context
