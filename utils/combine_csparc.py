#!/usr/bin/env python

import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="combine multiple cryosparc cs files into a single cs file")
    parser.add_argument('input', nargs="+", help='cryosparc .cs file(s)')
    parser.add_argument('output', help='Output cs file')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    for f in args.input:
        assert f.endswith('.cs'), f"Input {f} is not a .cs file"
    assert args.output.endswith('.cs'), f"Output {args.output} is not a .cs file"

    data = []
    for f in args.input:
        data.append(np.load(f))
        print(f"{len(data[-1])} particles read from {f}")
    data = np.concatenate(data)
    print(f"{len(data)} particles saved to {args.output}")
    with open(args.output, "wb") as fp:
        np.save(fp, data)

if __name__ == '__main__':
    main()
