-- Convert hbtn_0c_0 database to UTF8
ALTER DATABASE
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert first_table table to UTF8
ALTER TABLE first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert name field in first_table to UTF8
ALTER TABLE first_table MODIFY name
TEXT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
