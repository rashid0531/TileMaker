import Application_setup as appsetup
import abc


class VerifyParameters:
    @classmethod
    def create_appropriate_app_verification(cls, args: dict):
        try:
            if args['task'] in appsetup.TASKS:
                task_name = args['task']
                verification_method = appsetup.TASKS[task_name](args)
                verified = verification_method.verify_parameters()
                if verified:
                    return verified, verification_method.settings()
                else:
                    return verified, None
            else:
                # TODO
                # Check if this block of code executes or not.
                task_list = ''
                for each in appsetup.TASKS.keys():
                    task_list += '-' + each + '\n'
                print(f'Invalid Task. Possible tasks are: \n \t {task_list}')
        except KeyError as e:
            print(f' {e} Not found.')



class CoOrdinate(object):

    def __init__(self, name, coor: list):
        self.name = name
        self.abscissa, self.ordinate = coor
