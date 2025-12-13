-- Sample book record for the library database
-- This SQL can be executed to add a new book to the biblio table

-- First, let's make sure we have the required master data
-- Add a language if it doesn't exist
INSERT IGNORE INTO mst_language (language_id, language_name, input_date) 
VALUES ('en', 'English', CURDATE());

-- Add a publisher if it doesn't exist
INSERT IGNORE INTO mst_publisher (publisher_id, publisher_name, input_date) 
VALUES (1, 'Sample Publisher', CURDATE());

-- Add a GMD (General Material Designation) if it doesn't exist
INSERT IGNORE INTO mst_gmd (gmd_id, gmd_code, gmd_name, input_date) 
VALUES (1, 'BK', 'Book', CURDATE());

-- Now insert the sample book record
INSERT INTO biblio (
    gmd_id,
    title,
    edition,
    isbn_issn,
    publisher_id,
    publish_year,
    collation,
    series_title,
    call_number,
    language_id,
    source,
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Hidupku Sebening Air mata Ibu',
    '3 tahun Edition',
    '978-0-201-03801-7',
    1,  -- publisher_id
    '202',
    'xxii, 63 pages ; 20 cm',
    'biografi islami',
    'QA76.6 .K57 2024',
    'en',  -- language_id
    NULL,
    '005.7',
    'menceritakan sebuah biografi si penulis muhammad yahya a.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

-- Also add a sample item for this book
INSERT INTO item (
    biblio_id,
    call_number,
    coll_type_id,
    item_code,
    inventory_code,
    received_date,
    location_id,
    item_status_id,
    source,
    input_date,
    last_update
) VALUES (
    LAST_INSERT_ID(),  -- Use the ID of the book we just inserted
    'SA.005 .K57 2022',
    1,  -- coll_type_id
    'BK000002',
    'INV002',
    CURDATE(),
    'L01',  -- location_id
    'AV',   -- item_status_id
    0,
    NOW(),
    NOW()
);

-- Verify the insertion
SELECT 'Book added successfully with ID: ' AS message, LAST_INSERT_ID() AS book_id;