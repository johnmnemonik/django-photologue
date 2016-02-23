**Note: this project is being transferred to Github. [Please head over there](https://github.com/jdriscoll/django-photologue) for the latest downloads, and to report bugs.**

## What is Photologue? ##

Photologue is a reusable Django application that provides powerful image management and manipulation functionality as well as a complete photo gallery solution. The 2.x release adds more effects, including reflections and transparent watermarks. It also introduces the ImageModel abstract base class allowing developers to easily integrated the Photologue core functionality into their own models. Photologue embraces the Django admin and smoothly integrates with photo thumbnails and effect previews.

## What does it do? ##

  * Photologue allows you to define PhotoSize models. "Photo Sizes" are predefined image specifications such as thumbnails, banners, display sizes and user portraits. "Photo Sizes" can be scaled to a height or width proportionately or cropped from the center, top, left, bottom or right. Photologue will resize your original images to the sizes on you define on request and cache the results for further requests.

  * Photologue allows you to apply your own pre-defined PhotoEffect models to your "Photo Sizes" as well as individual photos. "Photo Effects" include adjusts such as "color", "brightness", "contrast" and "sharpness" as well as filters like "Find Edges" and "Emboss". Sharpen your images. Make your thumbnails black and white. It's auto-magical with Photologue.

  * Photologue gives you the ability to upload an entire gallery of images at once, using the GalleryUpload model, in a .zip file. Save time uploading a large number of images and apply tags, effects, and more.

  * Photologue's ImageModel abstract class parses EXIF information from supported files using the excellent [EXIF.py](http://sourceforge.net/projects/exif-py/) module and stores the information as a Python property for easy access.

  * Photologue's [Photo](Photo.md) model replaces the Django ImageField. Plug Photologue into your existing apps using foreign key relationships and enjoy a better experience managing uploaded images.

  * Photologue is easy to use. Models inheriting from the ImageModel abstract base class, including the [Photo](Photo.md) model, are modified at runtime with several "accessor" methods for retrieving specific photo paths, urls, etc. For instance, if you defined a "display" photo size, your photo models would be extended with the following methods: "get\_display\_url", "get\_display\_path" and  "get\_display\_size". These methods are added for each "Photo Size" you define.

  * Photologue is efficient. Uploaded images are only resized and processed upon first request. It then caches the result saving disk space, memory and processing power. Individual "Photo Sizes" such as thumbnails can be "pre-cached" to improve performance.

  * Photologue optionally supports the django-tagging application for setting tags on both your photos and galleries.

  * Photologue comes with a complete set of example templates for setting up a photo gallery fast. Define a master template, apply some styles and you've got a complete photo gallery system for your site or blog.

  * Photologue cleans up after itself. Unused files and folders are deleted automatically.

## What's New in Version 2? ##

  * New effects. Photologue 2 can automatically generate glossy image reflections and overlay your photos with transparent watermark images you upload and configure.

  * Rotation. You can now rotate specific images or image sizes.

  * View counts. You can now specify which photo sizes contribute to an automatically maintained photo view count.

  * The ImageModel abstract base class. Developers can now include all of the core Photologue functionality in their own models simply by inheriting from the included ImageModel class.

  * Interactive setup. Instead of loading a set of fixtures, Photologue 2 includes an interactive setup command.

  * Unit test suite.

  * Various bug fixes and performance improvements.

## Dependancies ##

Photologue 2 is compatible Django 1.0 or later. Photologue requires the [Python Imaging Library](http://www.pythonware.com/products/pil/). Tagging functionality requires the popular [django-tagging](http://code.google.com/p/django-tagging/) application.