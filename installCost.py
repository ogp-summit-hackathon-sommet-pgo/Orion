import pandas


def install_cost_solar(area: float) -> int:
    """
    Calculates the average cost of installing solar panels over a given area
    Info:
        1 Panel is 17.55 square feet, 1.63 m^2
        6 kW system requires 20 panels, 32.6 m^2
        $2.78 per Watt
        $512 per m^2
    :param area: Area to be covered in solar panels, in meters squared
    :return: Average cost of installing solar panels for given area, in CAD
    """
    return int(512 * int(area))


def install_cost_green(area: float) -> int:
    """
    Calculates the average cost of installing a green roof over a given area
    Info:
        $240 per m^2
    :param area: Area to be covered, in meters squared
    :return: Average cost of installing a green roof for given area, in CAD
    """
    return int(240 * int(area))


if __name__ == "__main__":
    f = lambda a: (install_cost_solar(float(a)))
    massing_df = pandas.read_csv('DataSets/3DMassing_2018_WGS84_fixed.csv', index_col=['SHAPE_AREA'],
                                 usecols=['SHAPE_AREA'])

