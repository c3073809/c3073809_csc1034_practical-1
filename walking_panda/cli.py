from . import panda
import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation", action="store_true")
    parser.add_argument("--scale", type=float, default=0, help="Scale factor for the panda (default is 0)")
    parser.add_argument("--night-mode", help="Enable night mode", action="store_true")
    parser.add_argument("--panda-color", choices=['normal', 'brown', 'black'], default='normal',
                        help="Color of the panda (default is normal)")

    args = parser.parse_args()
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
