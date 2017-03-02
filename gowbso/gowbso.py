import argparse
import importlib

from . import wbso_lib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('events_module')
    parser.add_argument('-m', '--monday', type=wbso_lib.valid_monday)
    args = parser.parse_args()

    # If the week to make data for is not specified, use the most recent
    # Monday.
    if args.monday is None:
        args.monday = wbso_lib.get_monday()

    events_module = importlib.import_module(args.events_module)
    week_days = wbso_lib.monday_to_week_days(args.monday)
    events = events_module.get_events(*week_days)
    wbso_lib.write_events(events)


if __name__ == '__main__':
    main()
