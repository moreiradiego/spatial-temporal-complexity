from iteration_utilities import duplicates
from memory_profiler import memory_usage
import time
from numpy import unique, random


# Time complexity comparison algorithm
def profile_complexity_function(fn_to_be_profiled, *arg, **kwargs):
    tuple_to_pass = (fn_to_be_profiled, arg, kwargs)
    t = time.process_time()
    mem_usage, result = memory_usage(tuple_to_pass, retval=True)
    elapsed_time = time.process_time() - t
    max_memory_MiB = max(mem_usage)
    min_memory_MiB = min(mem_usage)
    diff = max_memory_MiB - min_memory_MiB

    return {
        'time_enlapsed': elapsed_time,
        'memory_delta': diff
    }


def show_equals_in_list(*a_list):
    aux_list = []
    duplicated_items = []
    for item in a_list:
        if item not in aux_list:
            aux_list.append(item)
        else:
            duplicated_items.append(item)
    return duplicated_items


def show_equals_list_iteration_utilities(*a_list):
    return list(duplicates(a_list))


def show_equals_iterations_w_numpy(*a_list):
    u, c = unique(a_list, return_counts=True)
    dup = u[c > 1]
    return dup


def calculate_max_mem_and_time_usage(function_to_evaluate, data_to_be_processed, times_to_iterate):
    data = {"max_memory_usage_mib": 0, "max_memory_usage_kib": 0, "max_time_enlapsed": 0}
    for _ in range(times_to_iterate):
        result = profile_complexity_function(function_to_evaluate, *data_to_be_processed)
        data["max_memory_usage_mib"] = result["memory_delta"] if result["memory_delta"] > data[
            "max_memory_usage_mib"] else data["max_memory_usage_mib"]
        data["max_time_enlapsed"] = result["memory_delta"] if result["time_enlapsed"] > data["max_time_enlapsed"] else \
        data["max_time_enlapsed"]
    data["max_memory_usage_kib"] = data["max_memory_usage_mib"] * 1000
    return data


if __name__ == '__main__':
    list_to_be_processed = random.randint(0, 100, 1000)
    times_to_iterate = 100
    print(show_equals_in_list.__name__, calculate_max_mem_and_time_usage(show_equals_in_list, list_to_be_processed,
                                                                         times_to_iterate=times_to_iterate))
    print(show_equals_list_iteration_utilities.__name__,
          calculate_max_mem_and_time_usage(show_equals_list_iteration_utilities, list_to_be_processed,
                                           times_to_iterate=times_to_iterate))
    print(show_equals_iterations_w_numpy.__name__,
          calculate_max_mem_and_time_usage(show_equals_iterations_w_numpy, list_to_be_processed,
                                           times_to_iterate=times_to_iterate))
