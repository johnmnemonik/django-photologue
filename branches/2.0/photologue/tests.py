import os
import unittest
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from models import *

# Path to sample image
TEST_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'res', 'test.jpg')


class TestUploadedFile(InMemoryUploadedFile):
    """ Simplified uploadedfile wrapper
    
    Django's save_FIELD_file method expects an object that has the method
    "chunks" so we need to pass the file data in the appropriate wrapper.
    """
    def __init__(self, file):
        self.file = file
        self.field_name = None
        self.file.seek(0)
        
        
class TestPhoto(ImageModel):
    """ Minimal ImageModel class for testing """
    name = models.CharField(max_length=30)
    
    
class PLTest(TestCase):
    """ Base TestCase class """
    def setUp(self):
        self.s = PhotoSize(name='test', width=100, height=100)
        self.s.save()
        self.p = TestPhoto(name='test')
        self.p.save_image_file(os.path.basename(TEST_IMAGE_PATH),
                               TestUploadedFile(open(TEST_IMAGE_PATH, 'rb')))
        self.p.save()

    def tearDown(self):
        self.p.delete()
        self.failIf(os.path.isfile(self.p.get_image_filename()))
        self.s.delete()     


class PhotoTest(PLTest):    
    def test_new_photo(self):
        self.assertEqual(TestPhoto.objects.count(), 1)
        self.failUnless(os.path.isfile(self.p.get_image_filename()))
        self.assertEqual(os.path.getsize(self.p.get_image_filename()),
                                         os.path.getsize(TEST_IMAGE_PATH))
                                         
    def test_exif(self):
        self.assert_(len(self.p.EXIF.keys()) > 0)

    def test_paths(self):
        self.assertEqual(self.p.cache_path(),
                         os.path.join(settings.MEDIA_ROOT,
                                      PHOTOLOGUE_DIR,
                                      'photos',
                                      'cache'))
        self.assertEqual(self.p.cache_url(),
                         settings.MEDIA_URL + PHOTOLOGUE_DIR + '/photos/cache')

    def test_count(self):
        for i in range(5):
            self.p.get_test_url()
        self.assertEquals(self.p.view_count, 0)
        self.s.increment_count = True
        self.s.save()
        self.p = TestPhoto.objects.get(name='test')
        for i in range(5):
            self.p.get_test_url()
        self.assertEquals(self.p.view_count, 5)
        
    def test_precache(self):
        # set the thumbnail photo size to pre-cache
        self.s.pre_cache = True
        self.s.save()
        # make sure it created the file
        self.failUnless(os.path.isfile(self.p.get_test_filename()))
        self.s.pre_cache = False
        self.s.save()
        # clear the cache and make sure the file's deleted
        self.p.clear_cache()
        self.failIf(os.path.isfile(self.p.get_test_filename()))
        
    def test_accessor_methods(self):
        self.assertEquals(self.p.get_test_photosize(), self.s)
        self.assertEquals(self.p.get_test_size(),
                          Image.open(self.p.get_test_filename()).size)
        self.assertEquals(self.p.get_test_url(),
                          self.p.cache_url() + '/' + \
                          self.p._get_filename_for_size(self.s))
        self.assertEquals(self.p.get_test_filename(),
                          os.path.join(self.p.cache_path(),
                          self.p._get_filename_for_size(self.s)))
        
        
class ImageResizeTest(PLTest):        
    def test_resize_to_fit(self):
        self.assertEquals(self.p.get_test_size(), (100, 75))
        
    def test_resize_to_fit_width(self):
        self.s.size = (100, 0)
        self.s.save()
        self.assertEquals(self.p.get_test_size(), (100, 75))

    def test_resize_to_fit_height(self):
        self.s.size = (0, 100)
        self.s.save()
        self.assertEquals(self.p.get_test_size(), (133, 100))
        
    def test_resize_and_crop(self):
        self.s.crop = True
        self.s.save()
        self.assertEquals(self.p.get_test_size(), self.s.size)
        
    def test_resize_rounding_to_fit(self):
        self.s.size = (113, 113)
        self.s.save()
        self.assertEquals(self.p.get_test_size(), (113,85))  
        
    def test_resize_rounding_cropped(self):
        self.s.size = (113, 113)
        self.s.crop = True
        self.s.save()
        self.assertEquals(self.p.get_test_size(), self.s.size)
        
    def test_resize_no_upscale(self):
        self.s.size = (2000, 2000)
        self.s.save()
        self.assertEquals(self.p.get_test_size(), (1600, 1200))
        
    def test_resize_upscale(self):
        self.s.size = (2000, 2000)
        self.s.upscale = True
        self.s.save()
        self.assertEquals(self.p.get_test_size(), (2000, 1500))


class PhotoEffectTest(PLTest):
    def test(self):
        effect = PhotoEffect(name='test')
        im = Image.open(self.p.get_image_filename())
        self.assert_(isinstance(effect.pre_process(im), Image.Image))
        self.assert_(isinstance(effect.post_process(im), Image.Image))
        self.assert_(isinstance(effect.process(im), Image.Image))


class PhotoSizeCacheTest(PLTest):
    def test(self):
        cache = PhotoSizeCache()
        self.assertEqual(cache.sizes['test'], self.s)    
        