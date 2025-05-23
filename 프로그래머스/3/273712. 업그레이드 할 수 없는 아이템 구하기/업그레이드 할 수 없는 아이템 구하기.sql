-- 코드를 작성해주세요
SELECT
    ii.ITEM_ID,
    ii.ITEM_NAME,
    ii.RARITY
FROM
    ITEM_INFO ii
    INNER JOIN ITEM_TREE it
        ON ii.ITEM_ID=it.ITEM_ID
WHERE 1=1
    AND it.ITEM_ID NOT IN(SELECT PARENT_ITEM_ID
                          FROM ITEM_TREE
                          WHERE PARENT_ITEM_ID IS NOT NULL
                          GROUP BY PARENT_ITEM_ID)
ORDER BY
    ii.ITEM_ID DESC