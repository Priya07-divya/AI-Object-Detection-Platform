CREATE DATABASE IF NOT EXISTS object_detection_db;
USE object_detection_db;
CREATE TABLE IF NOT EXISTS detection_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    object_name VARCHAR(100) NOT NULL,
    confidence DECIMAL(6,5) NOT NULL,
    detected_at DATETIME NOT NULL
);
-- View events: SELECT * FROM detection_events ORDER BY detected_at DESC;
