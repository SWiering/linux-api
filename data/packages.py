def all_packages():
    """Get all currently installed packages

    Returns:
        list: list of dictionaries containing all package info
    """
    # First need to have the entire package list before cross referencing dependencies
    parsedpackaged = parse_packages()
    dps = package_dependencies(parsedpackaged)
    

def package_dependencies(packages):
    dependency_key = 'Depends'

    package_name_list = [package['Package'] for package in packages]

    for package in packages:
        if dependency_key in package.keys(): # if true means that the package has dependencies
            seperate_deps = package[dependency_key].split(',')

            # x = get_dependency_urls()
            for dependency in seperate_deps:
                dependency_name = dependency.replace(' ', '').split('(')[0]
                print(dependency_name)

    return True

def parse_packages():
    statusfile = 'status'
    filecontents = ''

    # TODO: Make correction location file
    with open(statusfile, 'r', encoding="utf8") as statcontent:
        filecontents = statcontent.readlines()

    # What seperates the key from the value in the status file
    property_seperator = ': '
    all_packages = []
    curr_obj = {}
    # Define here because will be used in different scopes in the loop
    package_key = ''
    # The offset for when the value starts
    str_offset = 2

    for line in filecontents:
        cleanline = line.rstrip('\n') # Remove newline to keep it pretty

        # if line is empty, it means it will move on to the next package
        if line.isspace():
            all_packages.append(curr_obj)
            curr_obj = {}
        # Descrption can also contain :, but always starts with a space, if the line starts with space, then there should be a property set
        elif property_seperator in cleanline and not cleanline.startswith(' '):
            sepratorindex = cleanline.index(property_seperator)

            package_key = cleanline[:sepratorindex]
            package_value = cleanline[sepratorindex + str_offset:]
            
            curr_obj[package_key] = package_value
        else:
            curr_obj[package_key] = curr_obj[package_key] + cleanline

    return all_packages


def find_package(package_name):
    """find package by name in the list of dictionaries

    Args:
        package_name (str): name of the package

    Returns:
        dict: dictionary containing all info of installed package
    """
    package_filter = [pckg for pckg in all_packages() if pckg['Package'] == package_name]
    filter_result = package_filter[0]

    return filter_result

all_packages()

