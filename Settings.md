The following settings can be over-ridden in your project's settings file:

### PHOTOLOGUE\_DIR ###
Default: `"photologue"`

The relative path from your `MEDIA_ROOT` setting where Photologue will save image files. If your MEDIA\_ROOT is set to "/home/justin/media", photologue will upload your images to "/home/justin/media/photologue".

### PHOTOLOGUE\_PATH ###
Specifies a "callable" that takes a model instance and the original uploaded filename and returns a relative path from your MEDIA\_ROOT that the file will be saved. This function can be set directly.

```
    # myapp/utils.py:
    import os 
    def get_image_path(instance, filename): 
        return os.path.join('path', 'to', 'my', 'files', filename) 
```

```
    # settings.py:
    from utils import get_image_path
    
    PHOTOLOGUE_PATH = get_image_path
```

You can also pass a string path to the function.

```
    # settings.py:
    PHOTOLOGUE_PATH = 'myapp.utils.get_image_path'
```

_This setting will override the PHOTOLOGUE\_DIR setting if both are defined._

### PHOTOLOGUE\_MAXBLOCK ###
Default: `256 * 2 ** 10`

Sets the `ImageFile MAXBLOCK` setting.

### SAMPLE\_IMAGE\_PATH ###
Default: `"%Photologue App Directory%/res/sample.jpg"`

The absolute path to the image file you wish to use as the sample image for Photo Effects in the Django admin. Image will not be resized by photologue.

### GALLERY\_SAMPLE\_SIZE ###
Default: `5`

The number of sample images to display in the generic views when listing multiple galleries.

### PHOTOLOGUE\_GALLERY\_LATEST\_LIMIT ###
Default: `None`

If not None or 0 (Zero) this will limit the number of images returned from `Gallery.latest()`.

### PHOTOLOGUE\_IMAGE\_FIELD\_MAX\_LENGTH ###
Default: `100`

The integer value passed as `max_length` to the ImageModel's Image Field.