-- 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;
-- SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS (WHERE NAME IS NOT NULL); <- 굳이 따지자면 NOT NULL 옵션은 필요없는 것이다.

-- 중복제거함수: DISTINCT
-- COUNT(*): NULL 포함
-- COUNT(COLUMN NAME): NULL 제거