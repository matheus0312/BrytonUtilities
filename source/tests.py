import fit_decode


def test_fit_file(fit_path):

    test_result = fit_decode.decode_fit(fit_path)

    print(test_result)