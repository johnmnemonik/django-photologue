A Photologue Gallery is a named collection of photos. Galleries can be public or private, and they can be tagged. Photos are not restricted to a single gallery and can belong to as many as you want.

## Methods ##
Commonly used public methods include:

### latest ###
Returns a queryset containing the latest photos assigned to the gallery by date.

#### Usage: ####
```
    mygallery.latest(limit=5, public=True)
```

#### Arguments: ####
##### limit #####
default: 0 (returns all photos)

The number of photos to return

#### public ####
default: True

Whether to limit the results to "public" photos.

### sample ###
Returns the a random set of photos from the gallery.

#### Usage: ####
```
    mygallery.sample(count=5, public=True)
```

#### Arguments: ####
##### count #####
default: 0 (returns all photos)

The number of photos to return

#### public ####
default: True

Whether to limit the results to "public" photos.

### public ###
Returns a queryset containing all "public" photos assigned to this gallery.

#### Usage: ####
```
    mygallery.public()
```