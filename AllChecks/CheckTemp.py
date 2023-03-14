# import cpuinfo

# # Get the CPU temperature
# cpu_info = cpuinfo.get_cpu_info()

# print (cpu_info)

# # temperature = cpu_info['hz_advertised_friendly'].split()[0]

# # # Print the CPU temperature
# # print(f"CPU temperature: {temperature}°C")


if __name__ == '__main__':
    from cpuinfo import get_cpu_info

    for key, value in get_cpu_info().items():
        print("{0}: {1}".format(key, value))

