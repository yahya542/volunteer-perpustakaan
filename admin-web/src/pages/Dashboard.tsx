import React, { useEffect, useState } from 'react';

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState({
    totalBooks: 0,
    totalUsers: 0,
    totalLoans: 0,
    activeReservations: 0
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate fetching dashboard statistics
    const fetchStats = async () => {
      try {
        // For demo purposes, we'll use dummy data
        // In a real application, you would fetch from your API
        setTimeout(() => {
          setStats({
            totalBooks: 1247,
            totalUsers: 892,
            totalLoans: 342,
            activeReservations: 28
          });
          setLoading(false);
        }, 500);
      } catch (error) {
        console.error('Error fetching stats:', error);
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return <div>Loading dashboard...</div>;
  }

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginTop: '20px' }}>
        <div style={{ backgroundColor: '#e3f2fd', padding: '20px', borderRadius: '8px', textAlign: 'center' }}>
          <h2>{stats.totalBooks}</h2>
          <p>Total Books</p>
        </div>
        <div style={{ backgroundColor: '#e8f5e9', padding: '20px', borderRadius: '8px', textAlign: 'center' }}>
          <h2>{stats.totalUsers}</h2>
          <p>Total Users</p>
        </div>
        <div style={{ backgroundColor: '#fff3e0', padding: '20px', borderRadius: '8px', textAlign: 'center' }}>
          <h2>{stats.totalLoans}</h2>
          <p>Active Loans</p>
        </div>
        <div style={{ backgroundColor: '#fce4ec', padding: '20px', borderRadius: '8px', textAlign: 'center' }}>
          <h2>{stats.activeReservations}</h2>
          <p>Reservations</p>
        </div>
      </div>
      
      <div style={{ marginTop: '40px' }}>
        <h2>Recent Activity</h2>
        <ul>
          <li>New book added: "The Art of Computer Programming"</li>
          <li>User John Doe borrowed "Introduction to Algorithms"</li>
          <li>Reservation made for "Design Patterns" by Jane Smith</li>
          <li>Book returned: "Clean Code" by Bob Johnson</li>
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;