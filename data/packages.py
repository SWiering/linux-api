class Packages():

    __installed_packages = []
    __dependencies = {}
    __dependency_key = 'Depends'

    def __init__(self):
        self.__get_packages()
        self.__set_dependencies()

    def __get_packages(self):
        """Function the is designed to read the packages in the package file located in the root folder of the project
        """
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

        self.__installed_packages = all_packages

    def __set_dependencies(self):
        """used to set dependencies on list level
        """

        # use range to save the package back into the list
        for index in range(0, len(self.__installed_packages)):
            package = self.__installed_packages[index] 

            if self.__dependency_key in package.keys(): # if true means that the package has dependencies
                package = self.__parse_dependencies(package)
                
            self.__installed_packages[index] = package

        print(self.__dependencies)

    def __parse_dependencies(self, package):
        """Makes sure the dependency urls are added on package-level in case they are installed

        Args:
            package (dict): dictionary containing all package info

        Returns:
            dict: returns the package with the dependency urls added into package
        """
        seperate_deps = package[self.__dependency_key].split(',') # split all the dependencies
        package['dependency_urls'] = [] 

        # Add the urls to dependency_urls for the packages that exist in __installed_packages
        for dependency in seperate_deps:
            dependency_name = dependency.replace(' ', '').split('(')[0]

            # Adds the absolute urls to the package info
            if dependency_name in self.package_names():
                package['dependency_urls'].append(f'/{dependency_name}')

                package_name = package['Package']

                # creates dependency associations for reverse dependencies
                if dependency_name in self.__dependencies.keys():
                    self.__dependencies[dependency_name].append(package_name)
                else:
                    self.__dependencies[dependency_name] = [package_name]

        return package

    def all(self):
        """Returns all the installed packages

        Returns:
            list: list of packages
        """
        return self.__installed_packages

    def find(self, package_name):
        """Find info of a package using the package name

        Args:
            package_name (str): package_name

        Returns:
            dict: dictionary with package info
        """
        package_filter = [pckg for pckg in self.__installed_packages if pckg['Package'] == package_name]
        filter_result = package_filter[0]

        if package_name in self.__dependencies.keys():
            filter_result['reverse_dependencies'] = self.__dependencies[package_name]

        return filter_result

    def package_names(self):
        """Returns a list of all package names

        Returns:
            list: package names
        """
        package_list = [package['Package'] for package in self.__installed_packages]

        return package_list


