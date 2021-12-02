from zipfile import ZipFile, is_zipfile
import time

file_name = "geschenk.zip"

for i in range(1):
    with ZipFile(file_name) as zip:
        zip.printdir()
        print(zip.namelist())
        # zip.extractall()
        with zip.open(zip.namelist()[0]) as innerZip:
            zip.printdir()
            print(innerZip)
            z = ZipFile(innerZip)
            z.printdir()
            print(is_zipfile(innerZip))


def unzip(input_zip: ZipFile):

    starttimer = time.time()
    timer = starttimer

    for i in range(1, 2500):

        if i % 50 == 0:
            print("Counter: ", i, "\n Time: ", time.time() - timer)
            starttime = time.time()

        innerFile = input_zip.open(input_zip.namelist()[0])

        if is_zipfile(innerFile):

            # after every 200th iteration, save the current zip and use this further to speed up the operations
            if i % 200 == 0:
                input_zip.extractall('temp')
                name = 'temp/' + input_zip.namelist()[0]
                input_zip.close()
                input_zip = ZipFile(name)
                print("Zip Name: ", name)
            else:
                input_zip.close()
                input_zip = ZipFile(innerFile)
        else:
            print("\n\nAB HIER")
            input_zip.printdir()
            print("Namelist: ", input_zip.namelist())
            print("Time: ", time.time() - starttimer)
            print("Text of the .txt file: ", innerFile.read())
            break



def rec_unzip(input_zip: ZipFile, counter=0):

    if counter % 50 == 0:
        print("Counter: ", counter, "\n Time: ", time.time())


    with input_zip.open(input_zip.namelist()[0]) as innerZip:
        if is_zipfile(innerZip):
            rec_unzip(ZipFile(innerZip), counter + 1)
        else:
            print("\n\nAB HIER")
            input_zip.printdir()
            print("Namelist: ", input_zip.namelist())


# print(rec_unzip(ZipFile(file_name)))
# print(rec_unzip(ZipFile('test3.zip')))

# unzip(ZipFile('test3.zip'))
unzip(ZipFile(file_name))
