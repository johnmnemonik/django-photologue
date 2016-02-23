Photologue automatically and optionally supports the popular django-tagging application (0.2 at the time of this writing). If django-tagging is not found the "tags" field on the Photo and Gallery model behaves as a regular Django CharField, otherwise it is replaced with the django-tagging "TagField".

Please see [django-tagging](http://django-tagging.googlecode.com/svn/trunk/docs/overview.txt) for more information.

**Update: There seems to be an incompatibility with django-tagging and Django 1.0. Tagging functionality will not be supported until this is resolved.**