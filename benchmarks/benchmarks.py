# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(5000):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            for random_no in range(30000):
                _ = random_no**random_no
            pass

    def time_range(self):
        d = self.d
        for key in range(800):
            x = d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256
