import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const Layout: React.FC = () => {
  return (
    <div style={{ display: 'flex' }}>
      <nav style={{ width: '200px', padding: '20px', backgroundColor: '#f0f0f0' }}>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/users">Users</Link></li>
          <li><Link to="/books">Books</Link></li>
        </ul>
      </nav>
      <main style={{ flex: 1, padding: '20px' }}>
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;