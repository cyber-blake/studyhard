from sys import version_info


def get_ver():
    print(f"Python {version_info.major}.{version_info.minor}.{version_info.micro}")
