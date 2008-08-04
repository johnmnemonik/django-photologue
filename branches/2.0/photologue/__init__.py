from django.db.models import signals
from django.dispatch import dispatcher
import models

def get_response(msg, func=int, default=None):
    while True:
        resp = raw_input(msg)
        if not resp and default is not None:
            return default            
        try:
            return func(resp)
        except:
            print 'Invalid input.'

def create_size(name, width=0, height=0, crop=False, pre_cache=False, increment_count=False):
    try:
        size = models.PhotoSize.objects.get(name=name)
    except models.PhotoSize.DoesNotExist:
        size = models.PhotoSize(name=name)
    print '\nWe will now define the "%s" photo size:\n' % size
    w = get_response('Width (in pixels):', lambda inp: int(inp), width)
    h = get_response('Height (in pixels):', lambda inp: int(inp), height)
    c = get_response('Crop to fit? (yes, no):', lambda inp: inp == 'yes', crop)
    p = get_response('Pre-cache? (yes, no):', lambda inp: inp == 'yes', pre_cache)
    i = get_response('Increment count? (yes, no):', lambda inp: inp == 'yes', increment_count)
    size.width = w
    size.height = h
    size.crop = c
    size.pre_cache = p
    size.increment_count = i
    size.save()
    print '\nA "%s" photo size has been created.\n' % name
    return size

def post_sync(sender, app, created_models, verbosity, interactive):
    if interactive:
        msg = '\nPhotologue requires a specific photo size to display thumbnail previews in the Django admin application.\nWould you like to generate this size now? (yes, no):'
        if get_response(msg, lambda inp: inp == 'yes', False):
            admin_thumbnail = create_size('admin_thumbnail', width=100, height=75, crop=True, pre_cache=True)
            msg = 'Would you like to apply a sample enhancement effect to your admin thumbnails? (yes, no):'
            if get_response(msg, lambda inp: inp == 'yes', False):
                effect, created = models.PhotoEffect.objects.get_or_create(name='Enhance Thumbnail', description="Increases sharpness and contrast. Works well for smaller image sizes such as thumbnails.", contrast=1.2, sharpness=1.3)
                admin_thumbnail.effect = effect
                admin_thumbnail.save()                
        msg = '\nPhotologue comes with a set of templates for setting up a complete photo gallery. These templates require you to define both a "thumbnail" and "display" size.\nWould you like to define them now? (yes, no):'
        if get_response(msg, lambda inp: inp == 'yes', False):
            thumbnail = create_size('thumbnail', width=100, height=75)
            display = create_size('display', width=400, increment_count=True)
            msg = 'Would you like to apply a sample reflection effect to your display images? (yes, no):'
            if get_response(msg, lambda inp: inp == 'yes', False):
                effect, created = models.PhotoEffect.objects.get_or_create(name='Display Reflection', description="Generates a reflection with a white background", reflection_size=0.4)
                display.effect = effect
                display.save()

dispatcher.connect(post_sync, sender=models, signal=signals.post_syncdb)
