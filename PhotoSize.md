The PhotoSize model can be viewed as a named set of parameters that Photologue uses to automatically resize and process your images. These paramters include output dimensions, compression quality, effects and watermarks. There is no limit to the number of PhotoSize models you can define and because Photologue only process your images when explicitly told to, you don't have to worry about your disk space being wasted.

## How Photologue Resize Your Images ##
Photo sizes are very flexible in the way your images are resized. You can resize to a maximum width, height or both. You can also have Photologue crop your images to an exact set of dimensions.

### Fit To A Box ###
You can tell Photologue to resize you images to fit within a "box" by defining (non-zero value) both a width and height. If you define a PhotoSize that is 500 wide and 500 tall (no crop), portrait oriented images (taller than wide) will be resized proportionately to 500 pixels tall and landscape oriented images (wider than tall) will be resized to 500 pixels wide.

### Fit To One Dimension ###
If you only define ONE dimension in a PhotoSize, either width or height, and leave the other set to zero your photos will be resized proportionally to the one defined dimension regardless of the size of the image. If you define a PhotoSize that is 700 wide (no crop) and 0 high. An image that is 1800 pixels tall by 1400 pixels wide will be resized to 900 pixels tall by 700 pixels wide. An image that is 400 pixels tall by 1400 pixels wide will be resized to 200 pixels tall by 700 pixels wide.

### No Resize ([r351](https://code.google.com/p/django-photologue/source/detail?r=351)) ###
If you define a PhotoSize with both the height and width set to zero Photologue will apply all appropriate effects and watermarks but will not resize the image. Please note that this is provided only so for instances where you need to apply effects or watermarks to an image and do not want it resized. You should not use this as a way of getting the original image as there is a small loss of quality when the image is resaved. The method `get_image_url()` method will return the original uploaded image file.

### Crop To Fit ###
By checking the "crop" check box for a PhotoSize your images will be resized to the exact dimensions you specify (**note: you must specify both a width and height if "crop" is True), cropping any areas that do not fit as specified by that individual photo's "crop\_from" property.**

## Properties ##
Apart from it's "name", each of the properties in the PhotoSize model tell Photologue how to process your images.

### name ###
A descriptive name for this PhotoSize. The "name" property is used to provide special methods to the Photo model and other ImageModel subclasses. PhotoSize names should contain only letters, numbers and underscores. Examples: "thumbnail", "display", "small", "main\_page\_widget". This is not currently enforced at the model level but will cause problems when the system tries to add the method "get\_my **awesome** size!!!!!111\_url" to your photo model objects.

### width & height ###
Specifies the width and height of the output file in pixels. See above to learn how Photologue uses these values to resize your source images.

### quality ###
The JPEG compression quality of the output file. Only applies to JPEG images.

### upscale ###
If False, Photologue will not enlarge your source images to fit the supplied dimensions. _If crop is True your source images will be enlarged to fit regardless of this property._

### crop ###
If True your images will be cropped to fit the exact width and height supplied.

### pre\_cache ###
If True, your images will automatically be resized and pre-cached as specified by this PhotoSize upon save or change. To conserve disk space, this should be set only for a PhotoSize you know you will want pre-generated for all images in your project.

### increment\_count ###
If True, this PhotoSize will increment an images view\_count property when it's URL is requested.

### effect ###
Specifies a PhotoEffect to apply to images when processed.

### watermark ###
Specifies a [Watermark](Watermark.md) to apply to images when processed.