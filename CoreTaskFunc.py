from ImageObject import ImageObject


def make_tiles(image_obj: ImageObject, coordinates: tuple, tile_size: tuple, output_directory: str):
    success = False
    # Load image.
    img = image_obj.load_image()
    if img is None:
        return success

    abscissa_idx = 0
    ordinate_idx = 1
    a, b, c, d = coordinates
    cnn_input_width = tile_size[abscissa_idx]
    cnn_input_height = tile_size[ordinate_idx]

    try:
        tiles_per_row = int((b[abscissa_idx] - a[abscissa_idx]) / cnn_input_width)
        tiles_per_column = int((c[ordinate_idx] - b[ordinate_idx]) / cnn_input_height)
    except ZeroDivisionError as e:
        print(e)

    starting_point_x = a[abscissa_idx]
    starting_point_y = a[ordinate_idx]

    # Naming convention for tiled images.
    prefix = str(img.filename.split("/")[-1])
    prefix = str(prefix.split(".")[0])

    try:
        for i in range(0, tiles_per_column):
            for j in range(0, tiles_per_row):
                left = starting_point_x + j * cnn_input_width
                right = starting_point_x + (j + 1) * cnn_input_width
                upper = starting_point_y + i * cnn_input_height
                lower = starting_point_y + (i + 1) * cnn_input_height

                points = (left, upper, right, lower)
                tile = img.crop(points)
                tile.save(output_directory + "/" + prefix + "_" + str(i) + "_" + str(j) + ".jpg")

        success = True
        return success
    except Exception as e:
        print(e)
        return success
