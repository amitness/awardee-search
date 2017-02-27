class Company(object):

    def __init__(self, name):
        self.name = name
        self.rating = 3
        self.streaks = [[0, 0, 10], [0, 1, 10], [0, 2, 15], [1, 0, 20], [1, 1, 11], [1, 2, 10], [2, 0, 9], [2, 1, 8], [2, 2, 10], [3, 0, 7], [3, 1, 11], [3, 2, 11], [4, 0, 6], [4, 1, 5], [4, 2, 8], [5, 0, 4], [5, 1, 1], [
            5, 2, 0], [6, 0, 12], [6, 1, 0], [6, 2, 1], [7, 0, 2], [7, 1, 1], [7, 2, 3], [8, 0, 4], [8, 1, 5], [8, 2, 6], [9, 0, 7], [9, 1, 8], [9, 2, 9], [10, 0, 10], [10, 1, 11], [10, 2, 1], [11, 0, 4], [11, 1, 10], [11, 2, 3]]
        self.won_bids = 24.03
        self.lost_bids = 100 - self.won_bids
        self.rnum = 43
        self.location = 'Kathmandu'
        self.registered = '2028-03-04'
        self.nsic_code = 5010
        self.is_verified = True
        self.is_blacklisted = False
