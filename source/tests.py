import fit_decode


def test_output_fit(fit_path):

    fit_result = fit_decode.decode_fit(fit_path)

    print(fit_result)