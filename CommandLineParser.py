import argparse
import Application_setup as appsetup
from Task import TaskRunner
from verify_param import VerifyParameters


class CommandLineParser(object):
    def __init__(self):
        self.description = appsetup.APP_DESCRIPTION
        self._parser = argparse.ArgumentParser(self.description)
        self.subparsers = self.initialize_subparser(help_txt='Options', destination='task')

    def initialize_subparser(self, help_txt, destination):
        return self._parser.add_subparsers(help=help_txt, dest=destination)

    def get_parser(self):
        return self._parser

    def add_new_sub_parser(self, sub_parser_info):
        new_parser = self.subparsers.add_parser(sub_parser_info['name'],
                                                help=sub_parser_info['description'])
        try:
            for each_argument in sub_parser_info['arguments']:

                new_parser.add_argument(each_argument.name_arg,
                                        action=each_argument.action_arg,
                                        nargs=each_argument.number_of_args,
                                        const=each_argument.const_arg,
                                        default=each_argument.default_arg,
                                        type=each_argument.type_arg,
                                        choices=each_argument.choices_arg,
                                        required=each_argument.required_arg,
                                        help=each_argument.help_arg,
                                        metavar=each_argument.metavar_arg,
                                        dest=each_argument.destination_arg)

        except KeyError as e:
            print('Given parser has no arguments.')
            exit()


class StartApplication:
    @classmethod
    def start(cls):
        app_parser = CommandLineParser()
        for each_command in appsetup.APPLICATION_COMMANDS:
            app_parser.add_new_sub_parser(each_command)

        args = vars(app_parser.get_parser().parse_args())
        is_verified, task_setup = VerifyParameters.create_appropriate_app_verification(args)
        if is_verified:
            TaskRunner.run_task(task_setup)
