from collective.grok import gs
from reddplusid.userregistration import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.userregistration', 
    title=_('reddplusid.userregistration import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.userregistration.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
