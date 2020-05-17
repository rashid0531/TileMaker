from collections import defaultdict
import Application_setup as appsetup
import Utilities as util
import abc


class AppVerification(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def verify_parameters(self, args: dict):
        pass

    @property
    @abc.abstractmethod
    def settings(self):
        pass


class ParamVerificationSinglePicture(AppVerification):
    def __init__(self, args: dict):
        self.task_params = defaultdict(lambda: None)
        self.args = args
        self.actions = appsetup.SINGLE_PICTURE_ACTIONS

    def settings(self):
        return self.task_params

    def verify_parameters(self):

        def check_tuple_size(input_tuple):
            return 3 > len(input_tuple) > 0

        if self.args:
            difference_of_actions = self.args.keys() - self.actions
            if difference_of_actions == {'task'}:
                try:
                    # Check if the actions are given right parameters.
                    if util.check_if_valid_file(self.args['image_path']):
                        self.task_params['image_path'] = self.args['image_path']

                    tile_size = util.format_string_to_int(self.args['tile_size'])
                    if check_tuple_size(tile_size):
                        self.task_params['tile_size'] = tile_size

                    if not util.check_if_dir_exists(self.args['save_path']):
                        self.task_params['save_path'] = self.args['save_path']

                    remaining_actions_to_add = self.actions - self.task_params.keys()
                    for each_action in remaining_actions_to_add:
                        coordinates = util.format_string_to_int(self.args[each_action])
                        if check_tuple_size(coordinates):
                            self.task_params[each_action] = coordinates

                except KeyError as e:
                    print(e)
                except ValueError as e:
                    print('Invalid action', e)

            else:
                err_str = ', '.join(difference_of_actions[1:])
                print(f"Invalid actions : {err_str}.")

            self.task_params['task'] = self.args['task']
            all_param_verified = [0 if self.task_params[action] is None else 1 for action in self.actions]
            return all(all_param_verified)


class ParamVerificationMultiplePictures(AppVerification):
    def __init__(self, args: dict):
        self.settings = None
        self.args = args
        self.actions = appsetup.MULTIPLE_PICTURES_ACTIONS

    def settings(self):
        return self.settings

    def verify_parameters(self, args: dict):
        pass
