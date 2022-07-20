from flask import Blueprint, jsonify
from data.packages import Packages

# Use blueprint for routing purposes
packages_blueprint = Blueprint('packages', __name__)

PackageData = Packages()

@packages_blueprint.route('/', methods=['GET'])
def get_packages():
    """Endpoint to show all package names

    Returns:
        list: name of all installed packages
    """
    package_names = PackageData.package_names()

    return jsonify(package_names)


@packages_blueprint.route('/<package_name>')
def get_package(package_name):
    """Find info for specific installed package

    Args:
        package_name (str): name of the installed package to find

    Returns:
        dict: dictionary containing all info of installed package
    """
    if package_name in PackageData.package_names():
        package_info = PackageData.find(package_name)

        return jsonify(package_info)
    else:
        return jsonify(success=False)
