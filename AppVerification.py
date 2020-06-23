import shutil
from collections import defaultdict
import Application_setup as appsetup
import Utilities as util
import abc


class AppVerification(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def verify_parameters(self):
        pass

    @property
    @abc.abstractmethod
    def settings(self):
        pass


class ParamVerificationSinglePicture(AppVerification):
    def __init__(self, args: dict):
        self.task_params = defaultdict(lambda: None)
        self.args = args
        self.arguments = appsetup.SINGLE_PICTURE_ARGUMENTS

    def settings(self):
        return self.task_params

    def verify_parameters(self):
        def check_tuple_size(input_tuple):
            return len(input_tuple) == 2

        if self.args:
            difference_of_arguments = self.args.keys() - self.arguments
            if difference_of_arguments == {'task'}:
                try:
                    # Inputs were collected by argparse as list.
                    image_path = self.args['image_path'][0]
                    if util.check_if_valid_file(image_path):
                        self.task_params['image_path'] = image_path

                    tile_size = self.args['tile_size']
                    if check_tuple_size(tile_size):
                        self.task_params['tile_size'] = tile_size

                    save_path = self.args['save_path'][0]
                    if util.check_if_dir_exists(save_path):
                        shutil.rmtree(save_path)
                    self.task_params['save_path'] = save_path

                    remaining_args_to_add = self.arguments - self.task_params.keys()
                    for each_arg in remaining_args_to_add:
                        coordinates = self.args[each_arg]
                        if check_tuple_size(coordinates):
                            self.task_params[each_arg] = coordinates

                except KeyError as e:
                    print(e)
                except ValueError as e:
                    print('Invalid action', e)

            else:
                err_str = ', '.join(difference_of_arguments[1:])
                print(f"Invalid actions : {err_str}.")

            self.task_params['task'] = self.args['task']
            all_param_verified = {arg: 0 if self.task_params[arg] is None else 1 for arg in self.arguments}
            values = all_param_verified.values()
            passed = all(values)
            if not passed:
                for key, val in all_param_verified.items():
                    if val == 0:
                        print(f"Invalid parameter for action: {key}")
            return passed


class ParamVerificationMultiplePictures(AppVerification):
    def __init__(self, args: dict):
        self.task_params = defaultdict(lambda: None)
        self.args = args
        self.arguments = appsetup.MULTIPLE_PICTURES_ARGUMENTS

    def settings(self):
        return self.task_params

    def verify_parameters(self):
        pass
