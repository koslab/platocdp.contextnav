from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from zope.publisher.interfaces import IRequest
from Products.CMFCore.interfaces import IContentish, ISiteRoot
from plone.app.layout.viewlets import interfaces as manager
from platocdp.contextnav.interfaces import IProductSpecific
from platocdp.contextnav.interfaces import IContextNavigationProvider

grok.templatedir('templates')

class ContextNav(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(manager.IAboveContent)
    grok.template('contextnav')
    grok.layer(IProductSpecific)

    def available(self):
        return True if self.navlinks() else False

    def navlinks(self):
        provider = getMultiAdapter(
            (self.context, self.request),
            IContextNavigationProvider
        )
        return provider.navlinks()

class SiteRootContextNav(ContextNav):
    grok.context(ISiteRoot)


class DefaultContextNavigationProvider(grok.MultiAdapter):
    grok.implements(IContextNavigationProvider)
    grok.adapts(IContentish, IRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def navlinks(self):
        return {}

class SiteRootNavigationProvider(DefaultContextNavigationProvider):
    grok.adapts(ISiteRoot, IRequest)

