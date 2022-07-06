SELECT C.HACKER_ID, H.NAME, COUNT(C.CHALLENGE_ID)
FROM CHALLENGES C
LEFT OUTER JOIN HACKERS H
ON C.HACKER_ID = H.HACKER_ID
GROUP BY C.HACKER_ID
-- 오류 group by 이상함 (ONLY FULL GROUP BY) ? 무슨 뜻이지

SELECT C.HACKER_ID, H.NAME, COUNT(C.HACKER_ID) CHALLENGES_CREATED
FROM CHALLENGES C
LEFT OUTER JOIN HACKERS H
ON C.HACKER_ID = H.HACKER_ID
GROUP BY C.HACKER_ID, H.NAME
ORDER BY 3, 1
-- GROUP BY절에 입력한 컬럼을 반드시 SELECT절에 입력해줄 필요는 없지만, SELECT 절에 이용할 컬럼은 반드시 GROUP BY에 입력해주어야 한다는 점

-- 중복된 값 중 max값 아닌 것은 어떻게 지우지?
SELECT C.HACKER_ID, H.NAME, COUNT(*) CHALLENGES_CREATED
FROM CHALLENGES C
LEFT OUTER JOIN HACKERS H
ON C.HACKER_ID = H.HACKER_ID
GROUP BY C.HACKER_ID, H.NAME
HAVING CHALLENGES_CREATED IN (SELECT sub1.challenges_created
                              FROM (SELECT hacker_id, COUNT(*) AS challenges_created
                                    FROM Challenges
                                    GROUP BY Challenges.hacker_id) sub1
                              GROUP BY sub1.challenges_created
                              HAVING COUNT(*) = 1)
    OR CHALLENGES_CREATED IN (SELECT MAX(sub2.challenges_created)
                              FROM (SELECT COUNT(*) AS challenges_created
                                    FROM Challenges
                                    GROUP BY Challenges.hacker_id) sub2)
ORDER BY 3, 1;