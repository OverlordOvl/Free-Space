import os

from OpenSSL import SSL
from twisted.internet import ssl


class CRTFactory(ssl.ClientContextFactory):

    def __init__(self, factory_path):
        super(CRTFactory, self).__init__()
        self.factory_path = factory_path

    def getContext(self):
        self.method = SSL.SSLv23_METHOD
        ctx = ssl.ClientContextFactory.getContext(self)
        ctx.use_certificate_file(os.path.join(self.factory_path, 'client.crt'))
        ctx.use_privatekey_file(os.path.join(self.factory_path, 'client.key'))

        return ctx
