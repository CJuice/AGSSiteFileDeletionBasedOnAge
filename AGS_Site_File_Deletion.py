"""
Examine any directory provided as an argument and look for .agssite files to delete.

Designed for Matt Sokol on 5/7/18 by CJuice
To be run via VisualCron and used for cleanup of backup files.
Revisions:
"""
def main():
    import sys
    import os
    import datetime

    directories_to_skip = ["portal"]
    directory_to_examine = sys.argv[1]
    now = datetime.datetime.now()
    TEN_DAYS_TIME = datetime.timedelta(days=10)

    try:
        for dirs, dirname, files in os.walk(directory_to_examine):
            if os.path.basename(dirs) in directories_to_skip:
                continue
            for file in files:
                full_file_path = os.path.join(dirs,file)
                time_file_last_modified = os.path.getmtime(full_file_path)
                duration_since_file_last_modified = now - datetime.datetime.fromtimestamp(time_file_last_modified)
                is_older_than_ten_days = duration_since_file_last_modified >= TEN_DAYS_TIME
                if file.endswith(".agssite") and is_older_than_ten_days:
                    os.remove(full_file_path)
                    print("{} has been removed".format(full_file_path))
    except IOError as io_err:
        print(io_err)
        exit()
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()