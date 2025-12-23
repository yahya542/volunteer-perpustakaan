-- Current Loans (Items currently borrowed)
-- This SQL file inserts sample data into the loan table for items that are currently borrowed
-- These loans have is_return = 0 and return_date = NULL

-- Insert current loans (not yet returned)
INSERT INTO loan (
    item_code,
    member_id,
    loan_date,
    due_date,
    renewed,
    loan_rules_id,
    is_lent,
    is_return,
    input_date,
    last_update
) VALUES 
-- Loan 1: Member '1234567891111111' borrowed item 'BK00001'
('BK00001', '1234567891111111', '2025-12-01', '2025-12-15', 0, 1, 1, 0, NOW(), NOW()),

-- Loan 2: Member '1234567891111111' borrowed another existing item
('BK00002', '1234567891111111', '2025-12-05', '2025-12-19', 1, 1, 1, 0, NOW(), NOW()),

-- Loan 3: Different member borrowed an existing item
('BK00003', 'M002', '2025-11-28', '2025-12-12', 0, 1, 1, 0, NOW(), NOW());

-- Insert member for loan 3 (if not exists)
INSERT IGNORE INTO member (
    member_id, member_name, gender, birth_date, member_type_id, member_address, 
    member_email, member_since_date, register_date, expire_date, input_date, last_update
) VALUES 
('M002', 'Ahmad Rifai', 1, '1990-05-15', 1, 'Jl. Merdeka No. 123', 
 'ahmad.rifai@example.com', '2025-01-01', '2025-01-01', '2026-01-01', NOW(), NOW());

-- Verify the insertion
SELECT 'Current loans added successfully!' AS message;
SELECT COUNT(*) AS current_loans_count FROM loan WHERE is_return = 0;