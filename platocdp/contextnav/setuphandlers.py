from collective.grok import gs
from platocdp.contextnav import MessageFactory as _

@gs.importstep(
    name=u'platocdp.contextnav', 
    title=_('platocdp.contextnav import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('platocdp.contextnav.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
