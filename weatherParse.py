import csv


def extract_weather_data(filename: str) -> tuple:
    """
    Extract Data from a CSV File
    Creates a Dict with First Column as Index
    Creates List with Column Headers
    :param filename: String
    :return: Tuple with 2 items, the dict and the column headers in that order
    """
    with open('DataSets/BrightSunshine.csv', mode='r') as csv_file:
        weather_data = csv.reader(csv_file, delimiter=',')
        weather_data_dict = dict()
        row_count = 0
        for row in weather_data:
            if row_count > 0:
                weather_data_dict[row[0]] = row[1:]
            else:
                header = row
            row_count += 1
        return dict, header


if __name__ == "__main__":
    print(extract_weather_data('DataSets/BrightSunshine.csv'))
