from min_max_pair import MinMaxPair


class ZeroElements(Exception):
    pass


# TODO: change this to work with any type of object list
class MinMax3:

    @staticmethod
    def min_max(num_list):
        if len(num_list) < 1:
            raise ZeroElements()

        elif len(num_list) == 1:
            return MinMaxPair(0, 0)
        start = 1
        mmp = None
        if len(num_list) % 2 == 1:
            mmp = MinMaxPair(0, 0)
        else:
            if num_list[0] < num_list[1]:
                mmp = MinMaxPair(0, 1)
            else:
                mmp = MinMaxPair(1, 0)
            start = 2

        for trk in range(start, len(num_list), 2):
            if num_list[trk] < num_list[trk + 1]:
                if num_list[trk] < mmp.min:
                    mmp.min = trk
                if num_list[trk + 1] > mmp.max:
                    mmp.max = trk + 1
            else:
                if num_list[trk + 1] < mmp.min:
                    mmp.min = trk + 1
                if num_list[trk] > mmp.max:
                    mmp.max = trk
            # print(mmp)
        return mmp


if __name__ == '__main__':
    num_list = [3, 2, 4, 1, 6, 9, 8, 7, 5, 0]
    print('The elements are')
    print(num_list)
    print()

    mmp = MinMax3.min_max(num_list)
    print(mmp)
