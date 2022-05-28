-- 중앙값 구하기
-- oracle (median 함수)
-- mysql : percent_rank() over (order by column) percent from table

SELECT ROUND(LAT_N, 4)
FROM (
  SELECT LAT_N, PERCENT_RANK() 
  OVER (ORDER BY LAT_N) PERCENT
  FROM STATION
) X
WHERE PERCENT = 0.5;

-- ORACLE

SELECT ROUND(MEDIAN(LAT_N,4)
FROM STATION;