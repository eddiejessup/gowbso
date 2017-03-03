import argparse
import importlib

from . import wbso_lib, utils


description = '''
usage examples:
  gowbso wbso_data
  gowbso ~/admin/wbso/wbso_data.py
  gowbso --monday 2017-02-27 wbso_data
'''


def main():
    parser = argparse.ArgumentParser(
        description='Make WBSO CSV files quickly',
        epilog=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'events_module',
        help='A Python module containing the week\'s activities. '
             'May be either the name of a Python module that can be imported, '
             'or a path to a Python file.'
    )
    parser.add_argument(
        '-m', '--monday', type=wbso_lib.valid_monday,
        help='A string representing the Monday that begins '
             'the week for which you want to generate data'
    )
    args = parser.parse_args()

    # If the week to make data for is not specified, use the most recent
    # Monday.
    if args.monday is None:
        args.monday = wbso_lib.get_monday()

    # If passed a path to a Python file.
    if args.events_module.endswith('.py'):
        # Allow modules in that directory to be imported.
        utils.make_module_path_importable(args.events_module)
        # And get the module name for that file.
        module_name = utils.file_path_to_module_name(args.events_module)
    # Otherwise, assume we have been passed an actual module name.
    else:
        module_name = args.events_module
    # Either way, import the module.
    events_module = importlib.import_module(module_name)

    week_days = wbso_lib.monday_to_week_days(args.monday)
    events = events_module.get_events(*week_days)
    wbso_lib.write_events(events)


if __name__ == '__main__':
    main()
