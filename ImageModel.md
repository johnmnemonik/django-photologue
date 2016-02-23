The ImageModel abstract base class encapsulates all of the core functionality of the Photologue Photo model. Django models that inherit from this class will be augmented with the basic fields and behavior required for them to provide image resizing and cacheing, view counts, enchancements and effects, reflections, watermarks, rotation, etc.

## Fields ##

The following fields will be added to any model inheriting from the ImageModel base class. These field names will become reserved and can not be overridden in your subclass:

### image ###
Type: [ImageField](http://docs.djangoproject.com/en/dev/ref/models/fields/#model-field-types)

Stores the file path of the original image.

### date\_taken ###
Type: [DateTimeField](http://docs.djangoproject.com/en/dev/ref/models/fields/#model-field-types)

The date the photo was originally taken. Photologue will attempt to determine this from the images EXIF data but will fall back to the date the model was created.

### view\_count ###
Type: [PositiveIntegerField](http://docs.djangoproject.com/en/dev/ref/models/fields/#model-field-types)

The number of times a PhotoSize with increment\_count set to true has been requested for this image.

### crop\_from ###
Type: [CharField](http://docs.djangoproject.com/en/dev/ref/models/fields/#model-field-types)

The position that this image will be cropped from if required.

| | top | |
|:|:----|:|
| left | center | right |
| | bottom | |

### effect ###
Type: [ForeignKey](http://docs.djangoproject.com/en/dev/ref/models/fields/#module-django.db.models.fields.related)

Explicitly applies a specific PhotoEffect to this image. This setting will override any effect applied to the PhotoSize requested.

## Commonly Used Methods ##
For the following methods the text "SIZE" should be replaced with the "name" of the desired PhotoSize.

### get\_SIZE\_photosize ###
Returns the PhotoSize model with that name.

```
    >>> myphoto.get_thumbnail_photosize()
    <PhotoSize: thumbnail>    
```

### get\_SIZE\_size ###
Returns a tuple containing the actual width and height of the image file on disk in pixels. The file will be generated and cached if not already available.

```
    >>> myphoto.get_thumbnail_size()
    (150, 75)
```

### get\_SIZE\_url ###
Returns a relative URL for the size specified. The file will be generated and cached if not already available.

```
    >>> myphoto.get_thumbnail_url()
    u'/media/photologue/photos/cache/myfile_thumbnail.jpg'
```

This is also the method you should use to insert sized photos into your templates:

```
    {% for photo in photos %}
        <img src="{{ photo.get_thumbnail_url }}">
    {% endfor %}
```

### get\_SIZE\_filename ###
Returns the path to the file on disk. The file will NOT be generated if it does not already exists.

## Admin Integration ##
When you inherit from the ImageModel class you get Photologues admin thumbnails for free. Just add "admin\_thumbnail" to the "list\_display" property of your ModelAdmin class:

```
    from myapp.models import MyPhoto
    
    class MyPhotoAdmin(admin.ModelAdmin):
        list_display = ['title', 'admin_thumbnail']
        
    admin.site.register(MyPhoto, MyPhotoAdmin)
```

## Example ##

Here is a (very) simple, but real world, example of a custom model that inherits from the ImageModel abstract class.

```
    from django.contrib.auth.models import User
    from photologue.models import ImageModel
    
    class UserPortrait(ImageModel):
        user = models.OneToOneField(User, primary_key=True)        
```

Now we can create a new PhotoSize through the shell or admin interface:

```
    >>> from photologue.models import PhotoSize
    >>> PhotoSize.objects.create(name='avatar', width=60, height=60, crop=True)
```

All that's left is to add our new user portraits in a template

```
    <div id="user_info">
        <h1>{{ user.get_full_name }}</h1>
        <img id="user_avatar" src="{{ user.userportrait.get_avatar_url }}">
    </div>
```