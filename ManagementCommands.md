Photologue ships with a few management commands to help manage your image cache

## plcache ##
By default this command pre-caches all photo sizes with pre\_cache=True.

```
    python manage.py plcache
```

You can also specify a list of photo size names as an argument to force pre-caching.

```
    python manage.py plcache display, thumbnail
```

## plcreatesize ##
This command allows you to generate new photosizes interactively using the command line interface.

```
    python manage.py plcreatesize my_new_size
```

## plflush ##
This command flushes or clears the cache for all images.

```
    python manage.py plflush
```

You can also specify a list of photo size names to flush.

```
    python manage.py plflush display, thumbnail
```

## plinit ##
This command initiates the Photologue initialization routine and prompts you to create a number of default photo sizes and effects. This command takes no arguments.

```
    python manage.py plinit
```