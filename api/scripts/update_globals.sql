-- 1. Update global stats
INSERT INTO global_rating_stats (id, num_ratings, sum_love_ratings, mean_love_rating, sum_shit_ratings, mean_shit_rating)
SELECT
    1 AS id,
    COUNT(r.id) AS num_ratings,
    COALESCE(SUM(r.love_score), 0) AS sum_love_ratings,
    COALESCE(AVG(r.love_score), 0) AS mean_love_rating,
    COALESCE(SUM(r.shit_score), 0) AS sum_shit_ratings,
    COALESCE(AVG(r.shit_score), 0) AS mean_shit_rating
FROM ratings r
ON CONFLICT (id) DO UPDATE SET
    num_ratings = EXCLUDED.num_ratings,
    sum_love_ratings = EXCLUDED.sum_love_ratings,
    mean_love_rating = EXCLUDED.mean_love_rating,
    sum_shit_ratings = EXCLUDED.sum_shit_ratings,
    mean_shit_rating = EXCLUDED.mean_shit_rating;


-- 2. Update book-level stats
WITH book_stats AS (
    SELECT
        r.book_id,
        COUNT(r.id) AS num_ratings,
        COALESCE(SUM(r.love_score), 0) AS sum_love_ratings,
        COALESCE(SUM(r.shit_score), 0) AS sum_shit_ratings,
        COALESCE(AVG(r.love_score), 0) AS avg_love_rating,
        COALESCE(AVG(r.shit_score), 0) AS avg_shit_rating
    FROM ratings r
    GROUP BY r.book_id
)
UPDATE books b
SET
    number_of_ratings = bs.num_ratings,
    sum_of_love_ratings = bs.sum_love_ratings,
    sum_of_shit_ratings = bs.sum_shit_ratings,
    average_love_rating = bs.avg_love_rating,
    average_shit_rating = bs.avg_shit_rating
FROM book_stats bs
WHERE b.id = bs.book_id;
