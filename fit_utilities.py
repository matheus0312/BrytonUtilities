import fitparse


def decode_fit(fit_path):
    fit_file = fitparse.FitFile(fit_path)
    for record in fit_file.get_messages():

        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        for data in record:

            # Print the name and value of the data (and the units if it has any)
            if data.units:
                print(" * {}: {} ({})".format(data.name, data.value, data.units))
            else:
                print(" * {}: {}".format(data.name, data.value))

        print("---")