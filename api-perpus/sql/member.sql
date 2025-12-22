-- Member table data only
-- This file contains only member data for the library system

USE perpus;

-- Clear existing data (optional)
-- DELETE FROM member;

-- Insert sample members into the member table
INSERT INTO member (member_id, member_name, gender, birth_date, member_type_id, member_address, member_mail_address, member_email, postal_code, inst_name, is_new, member_image, pin, member_phone, member_fax, member_since_date, register_date, expire_date, member_notes, is_pending, mpasswd, last_login, last_login_ip, input_date, last_update, birth_place, ktp_image) VALUES
('1234567890123456', 'John Doe', 1, '1990-01-15', 1, 'Jl. Sudirman No. 123, Jakarta', NULL, 'john.doe@example.com', '12345', 'Universitas Indonesia', NULL, NULL, NULL, '081234567890', NULL, '2025-09-17', '2025-09-17', '2026-09-17', NULL, 0, '$2y$10$examplehashforpassword1', NULL, NULL, '2025-09-17', '2025-09-17', 'Jakarta', NULL),
('3528012345678910', 'Yahya Saputra', 1, '1990-05-15', 1, 'Jl. Pahlawan No. 45, Surabaya', NULL, 'yahya.saputra@example.com', '67890', 'Institut Teknologi Sepuluh Nopember', NULL, NULL, NULL, '081298765432', NULL, '2025-09-18', '2025-09-18', '2026-09-18', NULL, 0, '$2y$10$examplehashforpassword2', NULL, NULL, '2025-09-18', '2025-09-18', 'Surabaya', NULL),
('12121212212121212', 'Dimas Putra', 1, '2004-12-12', 1, 'Jl. Merdeka No. 78, Malang', NULL, 'dimas.putra@example.com', '54321', 'Universitas Brawijaya', NULL, NULL, NULL, '0898774848393', NULL, '2025-09-18', '2025-09-18', '2026-09-18', NULL, 0, '$2y$10$examplehashforpassword3', NULL, NULL, '2025-09-18', '2025-09-18', 'Malang', NULL),
('9876543210987654', 'Sarah Johnson', 2, '1995-08-22', 1, 'Jl. Diponegoro No. 33, Bandung', NULL, 'sarah.johnson@example.com', '98765', 'Universitas Padjadjaran', NULL, NULL, NULL, '085678901234', NULL, '2025-09-19', '2025-09-19', '2026-09-19', NULL, 0, '$2y$10$examplehashforpassword4', NULL, NULL, '2025-09-19', '2025-09-19', 'Bandung', NULL);

-- Notes:
-- 1. member_id: Unique 16-digit identifier (NIK)
-- 2. gender: 1 = Male, 2 = Female
-- 3. member_type_id: 1 = Standard member type
-- 4. is_pending: 0 = Active member, 1 = Pending verification
-- 5. mpasswd: Hashed password (using bcrypt format)
-- 6. expire_date: Membership expiration date
-- 7. All members have active status (is_pending = 0) and can login