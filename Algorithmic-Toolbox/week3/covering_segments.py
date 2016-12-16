# Uses python3
'''Given a set of n segments {[a 0 , b 0 ], [a 1 , b 1 ], . . . , [a n−1 , b n−1 ]} with integer coordinates on a line, find
the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [a i , b i ] there is a point x ∈ X such
that a i ≤ x ≤ b i
'''
import sys

def optimal_points(segments):
    # input list of tuples representing segments
    # sort segments according to rightmost value
    segments = sorted(segments, key= lambda x: x[1])
    # create list of points
    points = []
    # iterate through all segments
    for segment in segments:
        if len(points) == 0:
            points.append(segment[1])
            continue
        if (segment[0] <= points[-1]) and (points[-1] <= segment[1]):
            continue
        else:
            points.append(segment[1])
    return points

if __name__ == '__main__':
    INPUT = sys.stdin.read()
    DATA = INPUT.split()[1:]
    SEGS = [(int(i), int(j)) for i, j in zip(DATA[0::2], DATA[1::2])]
    PTS = optimal_points(SEGS)
    print(len(PTS))
    for p in PTS:
        print(p, end = ' ')
