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


def create_cost_df(area_series: pandas.Series) -> pandas.DataFrame:
    """
    Creates a pandas DataFrame of the cost of solar and green roofing for given area series
    :param area_series: Pandas series with roof areas
    :return: Pandas DataFrame with columns ['SOLAR_COST', 'GREEN_COST']
    """
    count = int()
    size = area_series.shape[0]
    print('Generating area costs: ')
    cost = []
    for area in area_series:
        print(count/size * 100, '%')
        cost.append((install_cost_solar(area), install_cost_green(area)))
        count += 1
    cost_df = pandas.DataFrame(cost, columns=['SOLAR_COST', 'GREEN_COST'])
    return cost_df


if __name__ == "__main__":
    massing_df = pandas.read_csv('DataSets/3DMassing_2018_WGS84_fixed.csv')
    # cost = []
    # for item in massing_df['SHAPE_AREA']:
    #     cost.append(install_cost_solar(item))
    # massing_df['SOLAR_COST'] = pandas.Series(cost)
    costdf = create_cost_df(massing_df['SHAPE_AREA'])
    massing_df['SOLAR_COST'] = costdf['SOLAR_COST']
    massing_df['GREEN_COST'] = costdf['GREEN_COST']
    print(massing_df)
