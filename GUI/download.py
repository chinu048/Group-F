def save(path,rows,time,file_name= "sourcemeter_record.csv"):
    labels = ['Voltage', 'Current', 'Resistance','delete','delete']
    import pandas as pd
    df = pd.DataFrame.from_records(rows,columns = labels)
    size = len(labels)
    df.insert(size, 'time', time)
    df = df.drop('delete',1)


    import os
    df.to_csv(os.path.join(path,file_name),mode = 'w')
