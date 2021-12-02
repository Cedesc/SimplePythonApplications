from zipfile import ZipFile, is_zipfile
import time


def unzip(input_zip: ZipFile, zip_save_folder_name: str = 'temp', result_save_folder_name: str = 'temp'):
    """
    Functionality: Unzip zipped zips
    Requirement: Each ZIP contains only one file
    Improvement suggestion:
        Delete temporary saved zips after another zip was saved and save zips after less than 200 iterations.
    """

    startTimer = time.time()
    timer = startTimer

    # to prevent that the loop won't end, the maximum is set on 2500 (geschenk.zip has 2021 inner zips)
    for i in range(1, 2500):

        # after every 50 iteration: show intermediate status
        if i % 50 == 0:
            print("Counter: ", i, "\n Time: ", time.time() - timer)
            timer = time.time()

        innerFile = input_zip.open(input_zip.namelist()[0])

        # check if the inner file is a zip file or not
        if is_zipfile(innerFile):

            # after every 200th iteration: save current zip and use this saved zip for further operations to speed up
            if i % 200 == 0:
                input_zip.extractall(zip_save_folder_name)
                # save the path of the saved zip for further operation
                name = 'temp/' + input_zip.namelist()[0]
                input_zip.close()
                input_zip = ZipFile(name)
                print("  Current saved zip: ", name)
            else:
                input_zip.close()
                input_zip = ZipFile(innerFile)
        else:
            # print the last zip folder and the total time that the function has taken
            print("\n\nLAST ZIP FOLDER")
            input_zip.printdir()
            print(" Total Time: ", time.time() - startTimer)
            # extract the inner file
            input_zip.extractall(result_save_folder_name)
            break


if __name__ == '__main__':
    # unzip(ZipFile('test3.zip'))
    unzip(ZipFile('geschenk.zip'))
