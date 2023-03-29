# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
from tbt import run_this

# class TimeSuite:
#     """
#     An example benchmark that times the performance of various kinds
#     of iterating over dictionaries in Python.
#     """
#     def setup(self):
#         self.d = {}
#         for x in range(5):
#             self.d[x] = None

#     def time_keys(self):
#         for key in self.d.keys():
#             pass

#     def time_values(self):
#         for value in self.d.values():
#             pass

#     def time_range(self):
#         d = self.d
#         for key in range(800):
#             x = d[key]

class testbench:
    def setup(self):
        pass

    def time_runthis(self):
        _ =  run_this()

# class MemSuite:
#     def mem_list(self):
#         return [0] * 256
