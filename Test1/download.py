

def save(rows =[[],[],[],[],[]],time=[]):
    file_name = "sourcemeter_records.csv"
    labels = ['Voltage', 'Current', 'Resistance','delete','delete']
    import pandas as pd
    rows =[[4.999286, 0.01532606, 326.1951, 3164.438, 4220932.0],
            [4.999286, 0.01532769, 326.1604, 3164.547, 4220932.0],
            [4.999285, 0.01532821, 326.1494, 3164.646, 4220932.0],
            [4.999283, 0.01532852, 326.1425, 3164.754, 4220932.0],
            [4.999287, 0.01532875, 326.1378, 3164.854, 4220932.0],
            [4.999283, 0.01532892, 326.134, 3164.953, 4220932.0],
             [4.999285, 0.01532901, 326.1323, 3165.063, 4220932.0],
              [4.999282, 0.01532914, 326.1294, 3165.162, 4220932.0]]

    time = [0.2593965530395508, 0.3641393184661865, 0.4692206382751465, 0.5838475227355957, 0.6891882419586182, 0.8029129505157471, 0.9073398113250732, 1.0125727653503418]
    df = pd.DataFrame.from_records(rows,columns = labels)
    size = len(labels)
    df.insert(size, 'time', time)
    df = df.drop('delete',1)


    import glob
    import pandas as pd

    files_present = glob.glob(file_name)

    if not files_present:
        df.to_csv(file_name, mode ='w')
    else:
        print ('WARNING: This file already exists!')


    # df.to_csv(file_name)

save()
