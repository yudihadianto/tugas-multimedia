import ascii_magic
import argparse
try:
    parser = argparse.ArgumentParser()
    parser.add_argument('p', help='Masukan path gambar !', type=str)

    arg = parser.parse_args()
    path = arg.p

    my_art = ascii_magic.from_image_file(path)
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print('Error!', e)
