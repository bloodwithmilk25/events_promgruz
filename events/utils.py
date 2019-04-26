from transliterate import translit


# helper function to generate image names
def image_name(instance, filename):
    """
    filename consists of transliterated filename and extension
    it is put it the folder with name that corresponds with instance name
    if name was in latin it stays the same
    """
    ext = filename.split('.')[1]
    filename = translit(filename.split('.')[0][:20], 'ru', reversed=True).replace(" ", "") + '.' + ext
    try:
        if instance.path:  # if it's a call from "Image" model
            if instance.location:
                location_name = instance.location.name.replace(" ", "").replace("«", "").replace("»", "")
                location_name = translit(location_name[:35], 'ru', reversed=True)
                return "{}/{}".format(location_name, filename)
            else:
                print(instance.event.name)
                event_name = instance.event.name.replace(" ", "").replace("«", "").replace("»", "")
                event_name = translit(event_name[:35], 'ru', reversed=True).replace(" ", "")
                return "{}/{}".format(event_name, filename)
    except AttributeError:
        #  if it's a call from other models, not "Image"
        name = instance.name.replace(" ", "").replace("«", "").replace("»", "")
        name = translit(name[:35], 'ru', reversed=True).replace(" ", "")
        return "{}/{}".format(name, filename)
