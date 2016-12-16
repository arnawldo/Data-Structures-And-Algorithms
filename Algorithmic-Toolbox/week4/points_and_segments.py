# uses python3

'''
You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.'''

import sys

def fast_count_segments(starts, ends, points):
    cnt = []
    starts = [(c, 'l') for c in starts]
    ends = [(c, 'r') for c in ends]
    points = [[c, 'p'] for c in points]
    whole_segment = [].extend(starts)
    whole_segment = whole_segment.extend(ends)
    whole_segment = whole_segment.extend(points)
    whole_segment = sorted(whole_segment, key=lambda x: x[0])
    count = 0
    for pair in whole_segment:
        if pair[1] == 'l':
            count += 1
        elif pair[1] == 'p':
            cnt.append(count)
        elif pair[1] == 'r':
            count -= 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
