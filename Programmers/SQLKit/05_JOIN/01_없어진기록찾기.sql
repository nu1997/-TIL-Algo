-- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_OUTS AS B
LEFT JOIN ANIMAL_INS AS A
ON B.ANIMAL_ID = A.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL;

SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS
ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL;

/*
https://stackoverflow.com/questions/6638520/1052-column-id-in-field-list-is-ambiguous
SELECT 문 안에 B테이블을 참조해주어야한다.
SELECT ANIMAL_ID, NAME
FROM ...
은 작동하지 않는다
*/