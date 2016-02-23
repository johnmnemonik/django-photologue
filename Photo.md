The Photologue Photo model is a default implementation of the ImageModel abstract class. If work with the [Gallery](Gallery.md) model and included templates to provide an out-of-the-box photo gallery solution.

## Methods ##
Commonly used public methods include:

### get\_previous\_in\_gallery ###
Returns the previous photo in a specific gallery by date.

#### Usage: ####
```
    mygallery = Gallery.objects.get(title="My Gallery")
    myphoto.get_previous_in_gallery(mygallery)
```

#### Arguments: ####
##### gallery #####

A gallery object.

### get\_next\_in\_gallery ###
Returns the next photo in a specific gallery by date.

#### Usage: ####
```
    mygallery = Gallery.objects.get(title="My Gallery")
    myphoto.get_next_in_gallery(mygallery)
```

#### Arguments: ####
##### gallery #####

A gallery object.

### public\_galleries ###
Returns a queryset containing all "public" galleries this photo is assigned to.

#### Usage: ####
```
    myphoto.public_galleries()
```