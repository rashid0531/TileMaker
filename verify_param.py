class VerifyParameters(object):
    @classmethod
    def verify(cls, args: dict):
        coordinates = []
        for key, value in args.items():
            if 'cor' in str(key):
                coordinates.append((key, args[key]))
            else:
                img_path = args['image_path']
                tile_size = args['tile_size']
                save_path = args['save_path']

        prepare_coordinates(coordinates)

    def prepare_coordinates(coors):





class CoOrdinate(object):

    def __init__(self, name, coor:tuple):
        self.name = name
        self.abscissa, self.ordinate = coor
