-- Completed Loans (Items that have been returned)
-- This SQL file inserts sample data into the loan_history table for items that have been borrowed and returned
-- These loans have is_return = 1 and a return_date value

-- Insert completed loans directly into loan_history table
-- These represent loans that have been completed (returned)
INSERT INTO loan_history (
    loan_id,
    item_code,
    biblio_id,
    title,
    call_number,
    classification,
    gmd_name,
    language_name,
    location_name,
    collection_type_name,
    member_id,
    member_name,
    member_type_name,
    loan_date,
    due_date,
    renewed,
    is_lent,
    is_return,
    return_date,
    input_date,
    last_update
) VALUES 
-- Completed Loan 1: Member borrowed and returned an existing item
(101, 'BK00004', 4, 'Design Patterns', 'DP.001.DES.1994', '005.1', 'Book', 'English', 'Main Library', 'Reference',
 'M003', 'Budi Santoso', 'Standard Member', '2025-10-15', '2025-10-29', 0, 1, 1, '2025-10-28', NOW(), NOW()),

-- Completed Loan 2: Member borrowed and returned an existing item
(102, 'BK00005', 5, 'Introduction to Algorithms', 'IA.001.INT.2009', '005.1', 'Book', 'English', 'Main Library', 'Reference',
 '1234567891111111', 'testing', 'Standard Member', '2025-11-01', '2025-11-15', 1, 1, 1, '2025-11-14', NOW(), NOW()),

-- Completed Loan 3: Another member borrowed and returned an existing item
(103, 'BK00006', 6, 'Refactoring', 'RF.001.REF.2018', '005.1', 'Book', 'English', 'Main Library', 'Reference',
 'M004', 'Siti Nurhaliza', 'Standard Member', '2025-11-20', '2025-12-04', 0, 1, 1, '2025-12-03', NOW(), NOW());

-- Insert additional members for our completed loans (if not exists)
INSERT IGNORE INTO member (
    member_id, member_name, gender, birth_date, member_type_id, member_address, 
    member_email, member_since_date, register_date, expire_date, input_date, last_update
) VALUES 
('M003', 'Budi Santoso', 1, '1985-08-22', 1, 'Jl. Sudirman No. 45', 
 'budi.santoso@example.com', '2024-06-01', '2024-06-01', '2025-06-01', NOW(), NOW()),
('M004', 'Siti Nurhaliza', 0, '1992-03-10', 1, 'Jl. Gatot Subroto No. 78', 
 'siti.nurhaliza@example.com', '2025-03-15', '2025-03-15', '2026-03-15', NOW(), NOW());

-- Verify the insertion
SELECT 'Completed loans added successfully!' AS message;
SELECT COUNT(*) AS completed_loans_count FROM loan_history WHERE is_return = 1;