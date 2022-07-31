import re


def ipv4_validator(ipv4_address_string: str) -> bool:
    """Validates IPv4 Addresses 0.0.0.0 - 255.255.255.255.

    Args:
        ipv4_address_string (str): Potential IPv4 Address to be tested.

    Returns:
        bool: True when ipv4_address_string is valid.
    """
    if (re.search(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$', ipv4_address_string) == None):
        return False
    return True


if __name__ == "__main__":
    # If you run this file directly (not importing the file), the following will run:
    # region [CONSTANTS - SCRIPT INFO]
    SCRIPT_TITLE = "IPv4 Validator"
    VERSION = "1.0.0.0"
    DATE_CREATED = "7/31/2022"
    AUTHOR = "Joshua Wren"
    # endregion

    # region [TEST CASES]
    tests_expect_true = ["192.168.1.1", "0.0.0.0", "255.255.255.255"]
    tests_expect_false = [".2.3.4", "256.1.1.1", "!.1.1.1", "192.168.1.1.1"]
    # endregion

    # region [RUNNING TEST CASES]
    print(f"Welcome to {SCRIPT_TITLE} v{VERSION}!")
    print(f"\nCreated by {AUTHOR} on {DATE_CREATED}")
    print("-"*20)
    print("\nTesting Expected Good IPv4 Addresses...")
    for test in tests_expect_true:
        print(f"{test}: {ipv4_validator(test)}")

    print("\nTesting Expected Bad IPv4 Addresses...")
    for test in tests_expect_false:
        print(f"{test}: {ipv4_validator(test)}")
    # endregion
