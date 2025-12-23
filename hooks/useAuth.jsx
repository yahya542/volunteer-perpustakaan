import { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

export function useAuth() {
  const [isSignedIn, setIsSignedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const token = await AsyncStorage.getItem('token');
        setIsSignedIn(!!token); // true jika token ada, false jika null/undefined
      } catch (e) {
        console.error("Gagal memuat token:", e);
        setIsSignedIn(false);
      } finally {
        setIsLoading(false);
      }
    };
    checkAuth();
  }, []);

  // Fungsi placeholder untuk login/logout
  const signIn = async (token) => {
    await AsyncStorage.setItem('token', token);
    setIsSignedIn(true);
  };
  
  const signOut = async () => {
    await AsyncStorage.removeItem('token');
    setIsSignedIn(false);
  };

  return { isSignedIn, isLoading, signIn, signOut };
}