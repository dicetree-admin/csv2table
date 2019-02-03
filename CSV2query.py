query = """
LOAD DATA LOCAL INFILE "D:/temp/maria_test.csv"
INTO TABLE test.maria_test
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
;



SELECT table_schema, SUM((data_length+index_length)/1024/1024/1024) GB FROM information_schema.tables GROUP BY 1;

SELECT SUM((data_length+index_length)/1024/1024/1024) GB FROM information_schema.tables;

SELECT SUM(data_length+index_length)/1024/1024 used_MB, SUM(data_free)/1024/1024 free_MB FROM information_schema.tables;



CREATE TABLE PRG_CONFIG (
     `ID` INT NOT NULL AUTO_INCREMENT,
     `NAME` VARCHAR(50) NULL DEFAULT '',
     `VALUE` VARCHAR(50) NULL DEFAULT '',
     PRIMARY KEY (ID)
)COLLATE='utf8_bin';








"""