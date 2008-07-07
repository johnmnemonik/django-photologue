from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

class Command(BaseCommand):
    help = ('Clears the photologue cache for the given sizes.')
    args = '[sizes]'

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
    
    size_list = [size.strip(' ,') for size in sizes]
    
    if len(size_list) < 1:
        sizes = PhotoSize.objects.all()
    else:
        sizes = PhotoSize.objects.filter(name__in=size_list)
        
    if not len(sizes):
        raise CommandError('No photo sizes were found.')
        
    print 'Flushing cache...'
        
    for photo in Photo.objects.all():
       for photosize in sizes:
           print 'Flushing %s size images' % photosize.name
           for photo in Photo.objects.all():
               photo.remove_size(photosize)


