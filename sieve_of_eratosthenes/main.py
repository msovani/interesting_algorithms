master_primes = list()


def get_primes_below(max_value=100):
    global master_primes
    initial_list = list()
    for i in range(2, max_value):
        initial_list.append(i)
    loops = 0
    while loops < max_value:
        if initial_list is not None:
            initial_list = process_sieve(initial_list, loops)
            loops = loops + 1
        else:
            break
    return master_primes


def process_sieve(raw_data, loops):
    global master_primes
    prime_nums = list()
    if raw_data is None or len(raw_data) == 0:
        return
    first_elem = raw_data[0]
    loop = 0
    for item in raw_data:
        if first_elem == raw_data[loop]:
            master_primes.append(first_elem)
        elif first_elem < raw_data[loop]:
            if item % first_elem != 0:
                prime_nums.append(item)
        loop = loop + 1
    return prime_nums


def keep_getting_primes():
    global master_primes
    master_primes.clear()
    seed = 2
    master_primes.append(seed)
    while True:
        seed = seed + 1
        mod_success = True
        for x in master_primes:
            if seed % x == 0:
                mod_success = False
                break
        if mod_success:
            master_primes.append(seed)
            print(str(master_primes))
            if len(master_primes) > 1000:
                break


if __name__ == '__main__':
    # This call gives primes below 1000, this value can be changed
    print(str(get_primes_below(max_value=1000)))
    # This call keeps giving prime numbers, after getting first 1000 primes the code stops.
    # limit of 1000 can be changed.
    keep_getting_primes()
