SELECT 
    日付,
    品目 as 商品名,
    支出 as 金額,
    お店
FROM
    zaim
WHERE
    "品目" == "{shohin}"
ORDER BY
    支出 ASC
LIMIT
    3
;