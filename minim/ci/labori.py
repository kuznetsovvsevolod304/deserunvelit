def write_log(data_, filename):
    """Write data to a log file.

    Args:
        data_: Data to write to the log file.
        filename: Name of the log file.
    """

    with open(filename, "a") as f:
        f.write(data_ + "\n")

