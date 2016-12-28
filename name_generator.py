__author__ = 'dmadden'
from subprocess import check_output
from argparse import ArgumentParser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def gen_name(n):
    for x in range(n):
        yield check_output("{}/table_data/npc/name_gen.sh".format(dir_path)).rstrip("\n")


if __name__ == "__main__":
    parser = ArgumentParser(description="A CLI entrypoint for pathfinder name generator.")
    parser.add_argument("-n", dest='num_names', action='store', default=1, help="The number of names to be generated.", type=int)
    args = parser.parse_args()
    for x in gen_name(args.num_names):
        print x
