SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTRING(NAME, -3), ID;

-- SUBSTR(), SUBSTRING() 함수
/*
MySQL : SUBSTR(), SUBSTRING()
Oracle : SUBSTR()
SQL Server : SUBSTRING()

SUBSTR(str, pos, len)

출처: https://araikuma.tistory.com/521 [프로그램 개발 지식 공유]
*/