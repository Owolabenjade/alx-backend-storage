-- 9. Optimize search and score
-- Creates an index on the first letter of name and score
CREATE INDEX idx_name_first_score
ON names (name(1), score);