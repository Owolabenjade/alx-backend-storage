-- 7. Average score
-- Creates a stored procedure to compute and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score
    SELECT AVG(score) INTO avg_score 
    FROM corrections 
    WHERE corrections.user_id = user_id;
    
    -- Update the user's average_score
    UPDATE users 
    SET average_score = avg_score 
    WHERE id = user_id;
END$$
DELIMITER ;