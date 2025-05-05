-- 11. No table for a meeting
-- Creates a view listing students that need a meeting
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH));