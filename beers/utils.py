def image_upload_location (instance, filename):
    return 'media/beer/images/%s/%s.png' % (instance.id, filename)