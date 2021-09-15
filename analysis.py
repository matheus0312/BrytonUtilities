import fit_decode

def analyze_fit_files(analysis_mode):
    if analysis_mode == 'fit':
        fit_path=os.path.join(os.path.dirname(__file__) + '/files/fit/')

        print('Analyzing fit files in '+ fit_path)
        files = os.listdir(fit_path)
        for file in files:
            print('\n'+file)
            fit_file = fit_decode.decode_fit(fit_path + file)