import sys
from dataclasses import dataclass
# import sqlparse - available if you need it!
import sqlparse
database_file_path = sys.argv[1]
command = sys.argv[2]
if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:
        # You can use print statements as follows for debugging, they'll be visible when running tests.
        # print("Logs from your program will appear here!")
        # Skip the first 16 bytes of the header
        database_file.seek(16)
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")
        print(f"number of tables: {sum(line.count(b"CREATE TABLE") for line in database_file)}")
else:
    print(f"Invalid command: {command}")