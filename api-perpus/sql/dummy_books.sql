-- Dummy book records for the library database
-- This SQL can be executed to add 10 new books to the biblio table with different authors and publishers

-- First, let's make sure we have the required master data
-- Add languages if they don't exist
INSERT IGNORE INTO mst_language (language_id, language_name, input_date) 
VALUES 
('en', 'English', CURDATE()),
('id', 'Indonesia', CURDATE());

-- Add publishers if they don't exist
INSERT IGNORE INTO mst_publisher (publisher_id, publisher_name, input_date) 
VALUES 
(1, 'Sample Publisher', CURDATE()),
(2, 'Gramedia Pustaka Utama', CURDATE()),
(3, 'Mizan Publishing', CURDATE()),
(4, 'Erlangga', CURDATE()),
(5, 'Republika Publishers', CURDATE());

-- Add authors if they don't exist
INSERT IGNORE INTO mst_author (author_id, author_name, authority_type, input_date) 
VALUES 
(1, 'Muhammad Yahya A.', 'p', CURDATE()),
(2, 'Andrea Hirata', 'p', CURDATE()),
(3, 'Tere Liye', 'p', CURDATE()),
(4, 'Pramoedya Ananta Toer', 'p', CURDATE()),
(5, 'Dee Lestari', 'p', CURDATE()),
(6, 'Helvy Tiana Rosa', 'p', CURDATE()),
(7, 'John Doe', 'p', CURDATE());

-- Add GMD (General Material Designation) if it doesn't exist
INSERT IGNORE INTO mst_gmd (gmd_id, gmd_code, gmd_name, input_date) 
VALUES 
(1, 'BK', 'Book', CURDATE()),
(2, 'TH', 'Thesis', CURDATE());

-- Add locations if they don't exist
INSERT IGNORE INTO mst_location (location_id, location_name, input_date, last_update)
VALUES 
('L01', 'Main Library', CURDATE(), CURDATE()),
('L02', 'Reference Section', CURDATE(), CURDATE()),
('L03', 'Children Section', CURDATE(), CURDATE());

-- Add collection types if they don't exist
INSERT IGNORE INTO mst_coll_type (coll_type_id, coll_type_name, input_date, last_update)
VALUES 
(1, 'Regular Collection', CURDATE(), CURDATE()),
(2, 'Reference', CURDATE(), CURDATE()),
(3, 'Special Collection', CURDATE(), CURDATE());

-- Add item statuses if they don't exist
INSERT IGNORE INTO mst_item_status (item_status_id, item_status_name, no_loan, input_date, last_update)
VALUES 
('AV', 'Available', 0, CURDATE(), CURDATE()),
('LO', 'On Loan', 1, CURDATE(), CURDATE()),
('MA', 'Missing', 1, CURDATE(), CURDATE());

-- Now insert 10 different book records

-- Book 1
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Laskar Pelangi',
    'First Edition',
    '978-979-3062-79-2',
    2,  -- Gramedia Pustaka Utama
    '2005',
    '528 pages ; 20 cm',
    'Laskar Pelangi Series',
    'LP 001',
    'id',  -- language_id
    '895.92',
    'Novel tentang anak-anak dari Belitung yang bercita-cita tinggi.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_1 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_1, 2, 1); -- Andrea Hirata

-- Add item for Book 1
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
    @book_id_1,
    'LP.001.AND.2005',
    1,  -- Regular Collection
    'BK00002',
    'INV002',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 2
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Bumi Manusia',
    'First Edition',
    '978-979-1234-56-7',
    3,  -- Mizan Publishing
    '1980',
    '450 pages ; 21 cm',
    'Tetralogi Buru Series',
    'BM 001',
    'id',  -- language_id
    '895.92',
    'Kisah perjuangan Minke dalam perlawanan terhadap kolonialisme.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_2 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_2, 4, 1); -- Pramoedya Ananta Toer

-- Add item for Book 2
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
    @book_id_2,
    'BM.001.PRA.1980',
    1,  -- Regular Collection
    'BK00003',
    'INV003',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 3
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Hujan',
    'First Edition',
    '978-602-7876-54-3',
    3,  -- Mizan Publishing
    '2017',
    '320 pages ; 19 cm',
    '',
    'HU 001',
    'id',  -- language_id
    '895.92',
    'Novel tentang persahabatan dan cinta di tengah bencana.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_3 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_3, 3, 1); -- Tere Liye

-- Add item for Book 3
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
    @book_id_3,
    'HU.001.TER.2017',
    1,  -- Regular Collection
    'BK00004',
    'INV004',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 4 (Same author as Book 3, different publisher)
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Bintang',
    'Second Edition',
    '978-602-7876-67-8',
    5,  -- Republika Publishers
    '2018',
    '350 pages ; 19 cm',
    '',
    'BI 001',
    'id',  -- language_id
    '895.92',
    'Sebuah novel fantasi tentang petualangan di luar angkasa.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_4 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_4, 3, 1); -- Tere Liye (same author as Book 3)

-- Add item for Book 4
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
    @book_id_4,
    'BI.001.TER.2018',
    1,  -- Regular Collection
    'BK00005',
    'INV005',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 5 (Same publisher as Book 1, different author)
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Supernova',
    'First Edition',
    '978-979-3062-88-4',
    2,  -- Gramedia Pustaka Utama (same publisher as Book 1)
    '2001',
    '400 pages ; 20 cm',
    '',
    'SU 001',
    'id',  -- language_id
    '895.92',
    'Novel fiksi ilmiah tentang perjalanan antariksa.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_5 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_5, 5, 1); -- Dee Lestari (different author)

-- Add item for Book 5
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
    @book_id_5,
    'SU.001.DEE.2001',
    1,  -- Regular Collection
    'BK00006',
    'INV006',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 6
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Filosofi Kopi',
    'Third Edition',
    '978-602-8898-12-3',
    4,  -- Erlangga
    '2010',
    '250 pages ; 18 cm',
    '',
    'FK 001',
    'id',  -- language_id
    '895.92',
    'Kumpulan cerita pendek tentang kehidupan dan filosofi.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_6 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_6, 6, 1); -- Helvy Tiana Rosa

-- Add item for Book 6
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
    @book_id_6,
    'FK.001.HEL.2010',
    1,  -- Regular Collection
    'BK00007',
    'INV007',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 7
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Ganesha',
    'First Edition',
    '978-602-8898-45-1',
    4,  -- Erlangga
    '2012',
    '280 pages ; 18 cm',
    '',
    'GA 001',
    'id',  -- language_id
    '895.92',
    'Novel tentang perjalanan spiritual seorang remaja.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_7 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_7, 6, 1); -- Helvy Tiana Rosa (same author as Book 6)

-- Add item for Book 7
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
    @book_id_7,
    'GA.001.HEL.2012',
    1,  -- Regular Collection
    'BK00008',
    'INV008',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 8
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'The Art of Computer Programming',
    'Fourth Edition',
    '978-0-201-89683-1',
    1,  -- Sample Publisher
    '2020',
    '3168 pages ; 24 cm',
    '',
    'TA 001',
    'en',  -- language_id
    '005.1',
    'Comprehensive monograph covering many important algorithms in computer science.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_8 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_8, 7, 1); -- John Doe

-- Add item for Book 8
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
    @book_id_8,
    'TA.001.JOH.2020',
    2,  -- Reference
    'BK00009',
    'INV009',
    CURDATE(),
    'L02',  -- Reference Section
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 9 (Same author and publisher as original sample)
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Menjadi Manusia yang Bermanfaat',
    'Second Edition',
    '978-0-201-03802-4',
    1,  -- Sample Publisher (same as original)
    '2023',
    '150 pages ; 20 cm',
    '',
    'MB 001',
    'id',  -- language_id
    '158.1',
    'Buku motivasi tentang bagaimana menjadi manusia yang bermanfaat bagi sesama.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_9 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_9, 1, 1); -- Muhammad Yahya A. (same author as original)

-- Add item for Book 9
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
    @book_id_9,
    'MB.001.YAH.2023',
    1,  -- Regular Collection
    'BK00010',
    'INV010',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Book 10
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
    classification,
    notes,
    opac_hide,
    promoted,
    frequency_id,
    input_date,
    last_update
) VALUES (
    1,  -- gmd_id (Book)
    'Sang Pemimpi',
    'First Edition',
    '978-979-3062-82-2',
    2,  -- Gramedia Pustaka Utama
    '2006',
    '400 pages ; 20 cm',
    'Laskar Pelangi Series',
    'SP 001',
    'id',  -- language_id
    '895.92',
    'Sebuah novel tentang perjuangan mengejar cita-cita tinggi.',
    0,  -- opac_hide (visible)
    1,  -- promoted
    0,  -- frequency_id
    NOW(),
    NOW()
);

SET @book_id_10 = LAST_INSERT_ID();

INSERT IGNORE INTO biblio_author (biblio_id, author_id, level) 
VALUES (@book_id_10, 2, 1); -- Andrea Hirata (same author as Book 1)

-- Add item for Book 10
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
    @book_id_10,
    'SP.001.AND.2006',
    1,  -- Regular Collection
    'BK00011',
    'INV011',
    CURDATE(),
    'L01',  -- Main Library
    'AV',   -- Available
    0,
    NOW(),
    NOW()
);

-- Verify the insertion
SELECT '10 books added successfully!' AS message;