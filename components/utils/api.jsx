import AsyncStorage from '@react-native-async-storage/async-storage';

const BASE_URL = 'https://0b8763b66148.ngrok-free.app/';

// 🔐 Login
export const loginUser = async (username, password) => {
  const res = await fetch(`${BASE_URL}/auth/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });

  const data = await safeParse(res);
  return { ok: res.ok, status: res.status, data };
};

// 👤 Ambil nama user dari /auth/users/
export const getUserInfo = async (token, username) => {
  const res = await fetch(`${BASE_URL}/auth/users/`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });

  const text = await res.text();
  console.log('🔍 Raw /auth/users/ response:', text);

  try {
    const data = JSON.parse(text);
    const currentUser = data.find(user => user.username === username);
    return currentUser?.realname || null;
  } catch {
    throw new Error('Response bukan JSON, kemungkinan error HTML');
  }
};


// 📦 Simpan session
export const saveUserSession = async ({ token, username, realname }) => {
  await AsyncStorage.setItem('token', token);
  await AsyncStorage.setItem('username', username);
  if (realname) await AsyncStorage.setItem('realname', realname);
};

// 🧠 Helper: safe JSON/text parsing
const safeParse = async (res) => {
  try {
    return await res.json();
  } catch {
    return await res.text();
  }
};