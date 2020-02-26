from PIL import Image
import os


def blend_channel(start, stop, channel):
    shift = start or stop
    if start and stop:
        start /= 2
        stop /= 2

    coordinates = (0 + start, 0, channel.width - stop, channel.height)
    ch_cropped = channel.crop(coordinates)

    coordinates = ((shift / 2), 0, channel.width - (shift / 2), channel.height)
    ch_cropped_two = channel.crop(coordinates)

    channel_blend = Image.blend(ch_cropped, ch_cropped_two, 0.5)

    return channel_blend


def generate_file_name(file_path, prefix):
    dir_name, file_name = os.path.split(file_path)
    file_name = "{}_{}".format(prefix, file_name)

    return '{}/{}'.format(dir_name, file_name)


def get_style_ava(img_path, shift):
    image = Image.open(img_path)
    red_ch, green_ch, blue_ch = image.split()

    red_ch = blend_channel(shift, 0, red_ch)
    blue_ch = blend_channel(0, shift, blue_ch)
    green_ch = blend_channel(shift, shift, green_ch)

    new_image = Image.merge("RGB", (red_ch, green_ch, blue_ch))
    new_name = generate_file_name(img_path, "style")
    new_image.save(new_name)

    return new_name


def get_thumbnail_ava(img_path):
    image = Image.open(img_path)
    new_name = generate_file_name(img_path, "thumbnail")
    image.thumbnail((80, 80))
    image.save(new_name)

    return new_name

