-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I
INNER JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
ORDER BY I.ANIMAL_ID;


/*
FROM ANIMAL_INS AS I -> 여기에 where 쓸려고 했는데
중성화의 특성상 하지않은상태에서 한상태로만 갈 수 있다는 것을 이용하면(양방향변화불가능)
where절을 한번만 써도된다. 반대의 경우는 어떻게 풀어야할까?
*/