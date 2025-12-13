import React, { useEffect, useState } from 'react';

interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

const Users: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate fetching users data
    const fetchUsers = async () => {
      try {
        // For demo purposes, we'll use dummy data
        // In a real application, you would fetch from your API
        const dummyUsers: User[] = [
          {
            id: 1,
            username: 'john_doe',
            email: 'john@example.com',
            first_name: 'John',
            last_name: 'Doe'
          },
          {
            id: 2,
            username: 'jane_smith',
            email: 'jane@example.com',
            first_name: 'Jane',
            last_name: 'Smith'
          },
          {
            id: 3,
            username: 'bob_johnson',
            email: 'bob@example.com',
            first_name: 'Bob',
            last_name: 'Johnson'
          }
        ];
        
        setUsers(dummyUsers);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching users:', error);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return <div>Loading users...</div>;
  }

  return (
    <div>
      <h1>Users Management</h1>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Username</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Email</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Full Name</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.id}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.username}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.email}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>
                {user.first_name} {user.last_name}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Users;