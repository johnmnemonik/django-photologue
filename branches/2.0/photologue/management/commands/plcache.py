from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from photologue.models import PhotoSizeCache

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--reset', '-r', action='store_true', dest='reset', help='Reset photo cache before generating'),
   )

    help = ('Manages photologue cache file for the given sizes.')
    args = '[sizes]'
    label = 'photo size'

    requires_model_validation = True
    can_import_settings = True

    def handle(self, *args, **options):
        return create_cache(args, options)

def create_cache(sizes, options):
    """
    Creates the cache for the given files
    """
    from django.db.models.loading import get_model
    Photo = get_model('photologue', 'Photo')
    PhotoSize = get_model('photologue', 'PhotoSize')
    reset = options.get('reset', None)

    print 'Caching photos, this may take a while...'
    
    size_list = [size.strip(' ,') for size in sizes]
    
    if len(size_list) < 1:
        sizes = PhotoSize.objects.filter(pre_cache=True)
    else:
        sizes = PhotoSize.objects.filter(name__in=size_list)
        
    for photo in Photo.objects.all():
       for photosize in sizes:
           print 'Creating %s size images' % photosize.name
           if photosize is None:
               raise CommandError('A PhotoSize named "%s" was not found.' % (photosize.name))
           else:
               for photo in Photo.objects.all():
                   if reset:
                        photo.remove_size(photosize)
                   photo.create_size(photosize)


