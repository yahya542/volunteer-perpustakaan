import React, { useEffect, useState } from 'react';

interface Book {
  biblio_id: number;
  title: string;
  publish_year: string;
  isbn_issn: string | null;
  publisher_id: number | null;
  gmd_id: number | null;
}

const Books: React.FC = () => {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        // Untuk saat ini, kita akan menggunakan data dummy karena API belum berjalan
        // Ketika API berjalan, ganti dengan fetch ke API
        const response = await fetch('http://localhost:8000/api/biblio/');
        if (!response.ok) {
          throw new Error('Failed to fetch books');
        }
        const data = await response.json();
        setBooks(data);
        setLoading(false);
      } catch (err) {
        // Untuk demo, kita akan menggunakan data dummy
        const dummyData: Book[] = [
          {
            biblio_id: 1,
            title: 'Sample Book Title',
            publish_year: '2023',
            isbn_issn: '978-1234567890',
            publisher_id: 1,
            gmd_id: 1
          },
          {
            biblio_id: 2,
            title: 'Another Book Title',
            publish_year: '2022',
            isbn_issn: '978-0987654321',
            publisher_id: 2,
            gmd_id: 1
          }
        ];
        setBooks(dummyData);
        setLoading(false);
      }
    };

    fetchBooks();
  }, []);

  if (loading) {
    return <div>Loading books...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Books Management</h1>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Title</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Year</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>ISBN/ISSN</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.biblio_id}>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{book.biblio_id}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{book.title}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{book.publish_year}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{book.isbn_issn || 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Books;