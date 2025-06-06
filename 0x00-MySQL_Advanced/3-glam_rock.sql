-- 3. Old school band
-- Lists all bands with Glam rock as main style, ranked by longevity
SELECT band_name, 
       IFNULL(2022 - formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;