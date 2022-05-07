-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT
FROM ANIMAL_OUTS 
-- WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR;


-- WHERE HOUR(DATETIME) OK
-- WHERE HOUR FAIL
-- HAVING HOUR OK
-- HAVING HOUR(DATETIME) FAIL

-- -> 이유는?


---------------------- * * * * * * --------------------
-- SQL (날짜 데이터에서 일부만 추출하기
-- YEAR : 연도 추출
-- MONTH : 월 추출
-- DAY : 일 추출 (DAYOFMONTH와 같은 함수)
    -- DAYOFMONTH(기준 날짜)
-- HOUR : 시 추출
-- MINUTE : 분 추출
-- SECOND : 초 추출


-- 출처: https://extbrain.tistory.com/60 [확장형 뇌 저장소]