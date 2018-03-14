import os.path

save_path = '/home/amey/Desktop'
content = [[1, 2], [2, 3], [4, 5]]

def save(content,save_path):

    completeName = os.path.join(save_path, "failure.csv")

    with open(completeName, "w") as f:
        for row in content:
            for column in row:
                f.write('%d;' % column)
            f.write('\n')
            
    with open(completeName, "r") as f:
        for line in f:
            print (line)

# save(content,save_path)
